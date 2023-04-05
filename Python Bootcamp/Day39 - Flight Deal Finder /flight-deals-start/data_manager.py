import requests

# Sheety
TOKEN = "****SHEETY TOKEN***"

# Sheety endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/e2a39474e80ca8c14960851cf34d9a2e/flightDeals/prices"

BEARER_HEADERS = {
"Authorization": f"Bearer {TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __int__(self):
        # List of destination data
        self.destination_data = {}

    # Getting data from sheety
    def get_destination_data(self):

        response = requests.get(url=SHEETY_ENDPOINT, headers=BEARER_HEADERS)

        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # Sending the iataCode to Sheety
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=BEARER_HEADERS)
            print(response.text)