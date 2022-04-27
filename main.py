from data_manager import DataManager
from flight_search import FlightSearch


sheety = DataManager()
lowest_data_prices = sheety.sheety_request()

for city_tuple in range(len(lowest_data_prices)):
    flight = FlightSearch(lowest_data_prices[city_tuple])
    flight.get_flight_data()

