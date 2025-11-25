#Standard library imports 
import os
from datetime import date, timedelta

#Third-party imports
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
PRICE_CHANGE_THRESHOLD = 5
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SID = os.getenv("TWILIO_SID")
TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

def get_todays_and_yesterdays_date()-> tuple[str, str]:
    """
    Retrieves today's date and yesterday's date weekends are excluded.

    Returns:
        todays_date = "%Y - %m -%d"
        yesterdays_date = "%Y - %m - %d" 
    """

    #Get current date and yesterdays date 
    today = date.today()
    todays_date = today.strftime("%Y-%m-%d")

    yesterday = today - timedelta(days=1)
    
    if yesterday.weekday() in [5, 6]: # 5 = Saturday , 6 = Sunday 
        # Calculate days to subtract to get to Friday
        days_to_subtract = yesterday.weekday() - 4 
        last_friday = yesterday - timedelta(days=days_to_subtract)
        adjust_date = last_friday
    else:
        adjust_date = yesterday
    
    yesterdays_date = adjust_date.strftime("%Y-%m-%d")

    return todays_date, yesterdays_date

def get_stock_fluctuation() -> bool:
    """
    Retrieves the current stock price from https://www.alphavantage.co/query and compares it to previous days.

    The function checks whether the stock price has increased or decreased
    between yesterday and today. If the change meets
    the defined threshold, related news articles will be retrieved.

    Returns:
        bool: True if the price change meets the threshold otherwise False.
    """

    parameters = {
        "function" : "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "apikey" : STOCK_API_KEY,
 
    }
    try: 
        response = requests.get(url=STOCK_ENDPOINT,params=parameters)
        response.raise_for_status()
        stock_data = response.json()
    except requests.exceptions.Timeout:
        print("Request timed out, attempting again.")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"A connection error has occurred {e}")
        return False

    todays_date, yesterdays_date = get_todays_and_yesterdays_date()

    #Get closing stock price for today/yesterdays day
    try:
        todays_stock_closing = float(stock_data["Time Series (Daily)"][todays_date]["4. close"])
        yesterdays_stock_closing = float(stock_data["Time Series (Daily)"][yesterdays_date]["4. close"])
    except KeyError as e:
        print("Key was not found check if key has changed in stock_data")
        return False

    #Compare today's stock price vs yesterday's price, if higher than 5% return true, else return false
    return abs(todays_stock_closing - yesterdays_stock_closing)/yesterdays_stock_closing * 100 > PRICE_CHANGE_THRESHOLD

def get_news()-> list[dict[str, str]]:
    """
    Fetches the first 3 articles urls, description, and title for Nvidia from https://newsapi.org/v2/everything

    Returns: A list of articles in a dict including the title and url
    """
    #Retrieve today's date and yesterday's date
    todays_date , yesterdays_date = get_todays_and_yesterdays_date()

    parameters = {
        "q" : COMPANY_NAME,
        "apiKey" :  NEWS_API_KEY,
        "from" : yesterdays_date,
        "to" :todays_date,
        "language" : "en",
        "sortBy" : "popularity",
    }
    try: 
        response = requests.get(url=NEWS_ENDPOINT, params=parameters)
        response.raise_for_status()
        news_articles = response.json()
    except requests.exceptions.Timeout:
        print("Request timed out, attempting again.")
        return []
    except requests.exceptions.ConnectionError as e:
        print(f"A connection error has occurred {e}")
        return []

    first_3_articles = news_articles["articles"][0:3]
    article_list = []

    for articles in first_3_articles:
        article_details = {
            "Title" : articles["title"],
            "URL" : articles["url"] 
        }
        article_list.append(article_details)
    return article_list

def send_whatsapp_message(articles:list):
    """
    Sends a whatsapp message of the title of articles and the URL
    """

    message_body = "Nvidia: \n"
    for news in articles:
        message_body += f"Headline: {news['Title']}\n"
        message_body += f"Brief: {news['URL']}\n"
    client = Client(SID,TOKEN)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=f"{message_body}",
        to=f"whatsapp:+{PHONE_NUMBER}"
    )
    print(message.body)

if __name__ == "__main__":

    fluctuation = get_stock_fluctuation()

    if fluctuation:
        articles = get_news()
        send_whatsapp_message(articles)
    else:
        print("Stock has not increased or decreased by 5% since yesterday")
