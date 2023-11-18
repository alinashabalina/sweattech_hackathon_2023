import requests


class PeriodService:
    url = "http://127.0.0.1:5000"
    create_day_endpoint = "/day/create"
    get_day_endpoint = "/day/info/"
    get_training_endpoint = "/day/recommend/"

    def __init__(self):
        pass

    def create_a_day(self, data):
        response = requests.post(self.url + self.create_day_endpoint, json=data)
        return response

    def get_a_day(self, day_id, user_id):
        response = requests.get(self.url + self.get_day_endpoint + str(user_id) + "/" + str(day_id))
        return response

    def get_a_recommendation(self, day_id, user_id):
        response = requests.get(self.url + self.get_training_endpoint + str(user_id) + "/" + str(day_id))
        return response
