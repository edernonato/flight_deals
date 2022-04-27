import requests


sheety_endpoint ="https://api.sheety.co/b07d1c7a09b737068db5e62ed70bccf0/flightDeals/prices"
BEARER_TOKEN = "hdsaflk;jhadsfjlk;h;jlk3h24532141l23;1352ASD1F3132"

sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.sheety_endpoint = sheety_endpoint
        self.BEARER_TOKEN = BEARER_TOKEN
        self.data_dict = {}
        self.data_list = []

    def sheety_request(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = response.json()["prices"]

        for city in data:
            self.data_list.append([city["city"], city["iataCode"], city["lowestPrice"]])
            self.data_dict[city["iataCode"]] = city["lowestPrice"]

        return self.data_list
