#Standard library imports
import os

#Third-Part imports
import requests 
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("WORKOUT_APP_ID")
API_KEY = os.getenv("WORKOUT_API_KEY")
EXERCISE_URL = "https://app.100daysofpython.dev"

exercise_data = {

    "query": "ran 3 miles",
    "weight_kg": 70,                
    "height_cm": 175,             
    "age": 30,                      
    "gender": "male",

}

headers = {
    "Content-type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

response = requests.post(url=f"{EXERCISE_URL}/v1/nutrition/natural/exercise", json = exercise_data, headers=headers )
response.raise_for_status
print(response.text)