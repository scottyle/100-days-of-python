import requests 
from twilio.rest import Client


MY_LAT = 10.375722
MY_LONG = -61.233559
API_KEY = "3ea2eb51194358c83a8b8d2dc01beafc"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : API_KEY,
    "cnt" : 4
}

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
    print("Bring an umbrella")
