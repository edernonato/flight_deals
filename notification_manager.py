import smtplib
from user_data import GetUsers

email = "edernonato47teste@hotmail.com"
password = "Eder@teste321"
SMTP = "smtp-mail.outlook.com"
PORT = 587


users = GetUsers()

user_list = users.request_users()


class NotificationManager:

    def __init__(self, flight_data):
        self.city_name = flight_data[0]
        self.city_code = flight_data[1]
        self.price = flight_data[2]
        self.departure = flight_data[3]
        self.arrival = flight_data[4]
        self.send_email()

    def send_email(self):
        connection = smtplib.SMTP(SMTP, PORT)
        connection.starttls()
        connection.login(email, password)
        for user in user_list:
            connection.sendmail(from_addr=email,
                                to_addrs=user["email"],
                                msg=f"Subject: Low price Alert! {self.city_name} \n\n"
                                    f" Only R${self.price} to fly from Brazil-BRA to {self.city_name}-{self.city_code},"
                                    f" from {self.departure} to {self.arrival}")



