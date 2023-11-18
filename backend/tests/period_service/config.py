import requests


class PeriodService:
    url = "http://127.0.0.1:5000"
    create_day_endpoint = "/day/create"
    get_day_endpoint = "/day/info/"
    get_training_endpoint = "/day/recommend/"
    create_training_endpoint = "/training/create"

    def __init__(self):
        pass

    def create_a_day(self, data):
        response = requests.post(self.url + self.create_day_endpoint, json=data)
        return response

    def create_a_training(self, data):
        response = requests.post(self.url + self.create_training_endpoint, json=data)
        return response

    def get_a_day(self, date, user_id):
        response = requests.get(self.url + self.get_day_endpoint + str(user_id) + "/" + str(date))
        return response

    def get_a_recommendation(self, date, user_id):
        response = requests.get(self.url + self.get_training_endpoint + str(user_id) + "/" + str(date))
        return response
