import requests
from twilio.rest import Client

MY_LAT = 50.139769
MY_LONG = 14.519833
API_KEY = "7e9c87e8780a5b90b8b2fe39e5068592"

# Twilio creds
account_sid = "AC2773e572f6feb9470c4e9a7eddf05007"
auth_token = "***TWILIO TOKEN****"


parameters = {
    "lat": 46.347141,
    "lon": 48.026459,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()


# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # Twilio Client
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+16089797209",
        to="+420776427177"
    )

    print(message.status)
