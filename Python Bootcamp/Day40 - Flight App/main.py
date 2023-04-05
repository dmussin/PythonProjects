
# 4. Pass the data back to the hello.py file, so that you can print the data from hello.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Getting data from datamanager class
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_CODE = "PRG"

# Cheking if there is no iataCode then it used Flight Search API to get the code
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# Dates
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        print(f"THis is {emails}")
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only {flight.price}USD to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:

            message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}." \
               f"{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}." \
               f"{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_email(emails, message, link)