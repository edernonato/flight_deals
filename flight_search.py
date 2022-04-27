import requests
from notification_manager import NotificationManager
from flight_data import FlightData
search_flight_endpoint = "https://tequila-api.kiwi.com/v2/search"

headers = {
    "apikey": "8Vhi75Eyghsr9iItPtxbdeGj0XpucxkU"
}


class FlightSearch:

    def __init__(self, city):
        self.city_name = city[0]
        self.price = city[2]
        self.code = city[1]

    def get_flight_data(self):
        params = {
            "fly_from": "BRA",
            "fly_to": self.code,
            "date_from": "03/05/2022",
            "date_to": "04/09/2022",
            "return_from": "17/05/2022",
            "return_to": "18/09/2022",
            "curr": "BRL"
        }
        response = requests.get(url=search_flight_endpoint, params=params, headers=headers)
        data = response.json()['data']
        flight_data = FlightData(data, (self.city_name, self.code, self.price))
