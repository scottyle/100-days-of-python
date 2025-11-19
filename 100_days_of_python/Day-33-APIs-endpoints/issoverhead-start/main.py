import requests
from datetime import datetime
import smtplib

MY_LAT = 43.653225 
MY_LONG = -79.383186 
MY_EMAIL = "@gmail.com"
PASSWORD = ""

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def return_iss_position():
    """
    Function calls the ISS API to return the ISS Latitude and ISS Longtitude 
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

def get_sunrise_and_sunset():
    """
    Function returns the sunrise and sunset 
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset

def send_notification():
    """
    Function sends a notification to target email, 
    """
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        try:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="@gmail.com",
                msg=f"Subject:Lookup\n\nThe space station is right above you.")
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Failed to send email:{e}")

iss_latitude,iss_longitude = return_iss_position()
time_now = datetime.now()
#Assume time is in UTC 
hour = time_now.hour

#Check if your position is within +5 or -5 degrees of the ISS position and it is currently dark
if (-5 <= MY_LAT - iss_latitude <= 5) and (-5 <= MY_LONG - iss_longitude <= 5):
    #Check if it is currently dark: 
    sunrise,sunset = get_sunrise_and_sunset()
    if sunrise <= hour <= sunset:
        send_notification()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



