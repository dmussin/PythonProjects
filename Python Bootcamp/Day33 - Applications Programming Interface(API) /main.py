# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# # Data from API URL
# # data = response.json()["iss_position"]["longitude"]
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)




# --------------------------------


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.139769
MY_LONG = 14.519833


# ISS
def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.

    if iss_longitude - MY_LAT <= 5 or iss_latitude - MY_LAT >= -5 \
            and iss_longitude - MY_LONG <= 5 or iss_longitude - MY_LONG >= -5:
        return True
    else:
        return False

# Sunrise and Sunset

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunrise)
# print(sunset)

time_now = datetime.now()
# print(time_now.hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(120)
    if position() == True and time_now.hour >= sunset or time_now.hour <= sunrise:
        # smtplib set up
        my_email = "python.musin@gmail.com"
        password = "ffvjputzmmtqvokq"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure Connection
            connection.starttls()
            #Log in
            connection.login(user=my_email, password=password)
            # Send Email
            connection.sendmail(from_addr=my_email, to_addrs="dan4ik77@mail.ru",
                                msg="Subject:Day33 - ISS🌚 \n\n Look Up!")