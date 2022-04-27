import requests

sheety_endpoint = "https://api.sheety.co/b07d1c7a09b737068db5e62ed70bccf0/flightDeals/users"

BEARER_TOKEN = "hdsaflk;jhadsfjlk;h;jlk3h24532141l23;1352ASD1F3132"

sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}


class GetUsers:
    def __init__(self):
        self.endpoint = sheety_endpoint
        self.headers = sheety_headers
        self.token = BEARER_TOKEN
        self.request_users()

    def request_users(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        data = response.json()
        return data["users"]