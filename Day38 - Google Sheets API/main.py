import requests
from datetime import *

# Nutritionix
APP_ID = "fff4d119377"
API_KEY = "9fd104d88c0d7e38a587cf24f44f16e519"

# Sheety
TOKEN = "***SHEETY TOKEN***)"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Request body
params = {
 "query": input("Tell me which exercise you did today: "),
 "gender":"male",
 "weight_kg":93,
 "height_cm":178,
 "age":31
}

# Post
response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
print(response.text)

data = response.json()
exercise = data["exercises"][0]["name"]


# Today's date nad current time
today = date.today()
now = datetime.now()
# Format
today_date = today.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

# Sheety endpoint
sheety_endpoint = "https://api.sheety.co/e2a39474e80ca8c14960851cf34d9a2e/workoutTracking/workouts"

request_body = {
    "workout": {
        "date": today_date,
        "time": current_time,
        "exercise": exercise.title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}

bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}

# Post to Sheety
response = requests.post(url=sheety_endpoint, json=request_body, headers=bearer_headers)
print(response.text)