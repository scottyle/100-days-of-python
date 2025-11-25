#Standard library imports 
import os
import sys
from datetime import date, timedelta

#Third-party imports
from dotenv import load_dotenv
import requests

load_dotenv()

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
PRICE_CHANGE_THRESHOLD = 5

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
    between yesterday and the day before yesterday. If the change meets
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
    return abs(todays_stock_closing - yesterdays_stock_closing)/todays_stock_closing * 100 > PRICE_CHANGE_THRESHOLD

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

fluctuation = get_stock_fluctuation()

if fluctuation:
    get_news()
else:
    print("Stock is within margin of error")




## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

# response = requests.get(url=NEWS_ENDPOINT,params=parameters)
# response.raise_for_status()
# breakpoint()


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

