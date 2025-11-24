import requests 
from twilio.rest import Client
import json
import os 


MY_LAT = 43.653225
MY_LONG = -79.383186
API_KEY = os.environ.get("OWM_API_KEY")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
SID = os.environ.get("SID")
TOKEN = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : API_KEY,
    "cnt" : 4
}

account_sid = SID
auth_token = TOKEN


response = requests.get(url=OWN_Endpoint,params=parameters)
response.raise_for_status()
http_code = response.status_code

weather_data = response.json()

"""
[ - Opens the list comprehension
weather["id"] - This is the expression - the value you want to collect/extract. It comes FIRST, even though logically it happens last.
for data in weather_data["list"] - This is your outer loop - it runs first and gives you each data item.
for weather in data["weather"] - This is your inner loop - for each data from step 3, this loops through the weather items inside it.
if weather["id"] < 700 - This is your if condition that create the expression only if true
] - Closes the list comprehension

"""

if any(weather["id"] < 700 for data in weather_data["list"] for weather in data["weather"]):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+16474679254"
    )


    print(message.body)