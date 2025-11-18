import datetime as dt 
import sys
import random
import smtplib

"""
Objective: Send a motivational quote via email on the current weekday (you can change it to Monday afterwards)
"""
CURRENT_TIME = dt.datetime.now()
CURRENT_DAY = CURRENT_TIME.weekday()
QUOTES = "quotes.txt"
MY_EMAIL = "@gmail.com"
PASSWORD = ""

def get_a_quote():
    """This function retrieves a list of quotes from quotes.txt"""
    try:
        with open(QUOTES,"r") as file:
            try:
                quotes = file.readlines()
                random_quote = random.choice(quotes)
                return random_quote
            except IndexError as e:
                print(f"File is empty {e}")
                sys.exit(1)
                
    except FileNotFoundError as e:
        print("Quotes file not found... exiting")
        sys.exit(1)

def send_motivational_quote(quote):
    """This function sends a email with the motivational quote"""
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        try:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="@gmail.com",
                msg=f"Subject:Daily Motivational Quote\n\n{quote}")
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Failed to send email:{e}")

if CURRENT_DAY == 6:
    #Call quotes.txt to obtain a list of quotes. 
    quote = get_a_quote()
    #Send email
    send_motivational_quote(quote)
