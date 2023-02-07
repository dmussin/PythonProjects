import requests

MY_LAT = 50.139769
MY_LONG = 14.519833
API_KEY = "7e9c87e8780a5b90b8b2fe39e5068592"

parameters = {
    "lat": 31.088900,
    "lon": 30.390039,
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
    print("Bring an umbrella")