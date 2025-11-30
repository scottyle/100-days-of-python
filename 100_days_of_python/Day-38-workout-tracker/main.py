#Standard library imports
import os

#Third-Part imports
import requests 
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("WORKOUT_APP_ID")
API_KEY = os.getenv("WORKOUT_API_KEY")
SHEETY_URL = "https://api.sheety.co/56e6cb3fefaa69b61b1dc5bb0c57e5a5/myWorkouts/workouts"
EXERCISE_URL = "https://app.100daysofpython.dev"
WEIGHT_KG = 67.5
HEIGHT_CM = 175 
AGE = 31 
GENDER = "male" 

today = datetime.today()
todays_date = today.strftime("%d/%m/%Y")
todays_time = today.strftime("%H:%M:%S")

exercise_input = input("Tell me which exercises you did: ")



headers = {
    "Content-type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

def add_workout_to_google_sheet(workout_details:dict):
    """Takes the input of workout details and creates a entry to My Workouts"""
    
    response = requests.post(url=SHEETY_URL, json = workout_details)

def get_workout_details():
    """"""

    exercise_data = {

    "query": exercise_input,
    "weight_kg": WEIGHT_KG,                
    "height_cm": HEIGHT_CM,             
    "age": AGE,                      
    "gender": GENDER,

    }   
    
    response = requests.post(url=f"{EXERCISE_URL}/v1/nutrition/natural/exercise", json = exercise_data, headers=headers )
    response.raise_for_status
    data = response.json()
    print(response.text)

breakpoint()


