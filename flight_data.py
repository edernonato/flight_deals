from notification_manager import NotificationManager


class FlightData:

    def __init__(self, data, initial_data):
        self.data = data
        self.city_name = initial_data[0]
        self.code = initial_data[1]
        self.price = int(initial_data[2])
        self.send_data()

    def send_data(self):
        data_price = {}
        for country in range(len(self.data)):
            if int(self.data[country]['price']) <= self.price:
                data_price[self.city_name] = {self.data[country]['cityCodeTo']: self.data[country]['price'], }

                city_code = self.data[country]['cityCodeTo']
                new_price = self.data[country]['price']
                departure = self.data[country]['local_departure'].split('T')[0]
                arrival = self.data[country]['local_arrival'].split('T')[0]
                print(f"City :{self.city_name}, Code : {city_code}, Price : {new_price}, from {departure} to {arrival}")
                notify_data = (self.city_name, city_code, new_price, departure, arrival)
                notify = NotificationManager(notify_data)
