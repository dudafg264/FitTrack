import requests
import os
from datetime import datetime

# Fetch environment variables for API keys and Google Sheets API URL
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
SHEET_API = os.environ.get('SHEET_API')

# Set the headers for Nutritionix API requests
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

# Ask the user for the exercises they did
exercise_entry = {
    "query": input("Tell me which exercises you did: ")
}

# URL for the Nutritionix API to get exercise data
api_url_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Send POST request to Nutritionix API to get exercise data
exercise_response = requests.post(url=api_url_exercise, headers=headers, json=exercise_entry)
exercise_data = exercise_response.json()

# Loop through the exercises and prepare data for Google Sheets
for exercise in exercise_data["exercises"]:
    body = {
        "workout": {
            "date": datetime.now().strftime('%Y-%m-%d'),  # Get today's date
            "exercise": exercise["name"].capitalize(),  # Capitalize the exercise name
            "time": datetime.now().time().strftime('%H:%M:%S'),  # Get current time
            "duration": exercise["duration_min"],  # Duration in minutes
            "calories": exercise["nf_calories"]  # Calories burned
        }
    }

    # Send workout data to Google Sheets API
    response_sheets = requests.post(url=SHEET_API, headers=headers, json=body)

    # Check if the data was added successfully
    if response_sheets.status_code == 200:
        print("Your workout was added successfully!")
    else:
        print(f"Failed to add workout. Status code: {response_sheets.status_code}")
