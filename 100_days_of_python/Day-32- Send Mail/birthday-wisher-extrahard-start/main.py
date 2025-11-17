##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import sys
import random
import smtplib

CURRENT_MONTH = dt.datetime.today().month
CURRENT_DAY = dt.datetime.today().day

BIRTHDAYS_CSV = "birthdays.csv"

MY_EMAIL = "scottyle02test@gmail.com"
PASSWORD = "jzwv ypon kbxj wruk"

def open_birthdays_csv():
    """This function is used to open birthdays.csv and retrieve birthday information"""
    try:
        df = pd.read_csv(BIRTHDAYS_CSV)
        return df
    except FileNotFoundError as e: 
        print("Birthday.csv not found")
        sys.exit(1)
    except pd.errors.EmptyDataError as e:
        print(f"CSV is empty: {e}")
        sys.exit(1)

def check_if_birthday(birthday_info):
    """This function is used to check if today's date is equal to a birthday inside the csv, if so return data"""
    #Loop through the df to check if year/month/day is the same as today's date
    for index,info in birthday_info.iterrows():
        if (info["month"] == CURRENT_MONTH ) and (info["day"] == CURRENT_DAY):
            return info
        
    return pd.Series()
        
def get_birthday_message(matched_birthday):
    """This function is used to obtain the birthday message"""
    template_number = random.randint(1,3)
    try:
        with open(f"letter_templates/letter_{template_number}.txt","r") as file:
            template_name = "[NAME]"
            contents = file.read()
            revised_birthday_messsage = contents.replace(template_name,f"{matched_birthday['name']}")
            return revised_birthday_messsage
    except FileNotFoundError as e:
        print(f"No letter_template file found. {e}.... exiting")
        sys.exit(1)

def send_birthday_message(birthday_message):
    """This function sends a birthday message email"""
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        try:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="scottyle02@gmail.com",
                msg=f"Subject:Happy Birthday!\n\n{birthday_message}")
            print("Sent birthday email!")
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Failed to send email:{e}")

#Call function to open birthday info csv
birthday_info = open_birthdays_csv()
#Call function to return birthday information 
matched_birthday = check_if_birthday(birthday_info=birthday_info)  #What to do if theres two matching birthdays? 

#Check if there is a matched birthday 
if not matched_birthday.empty:
    birthday_message = get_birthday_message(matched_birthday=matched_birthday)
    send_birthday_message(birthday_message=birthday_message)
else:
    print("No ones birthday is today")
    sys.exit(1)
