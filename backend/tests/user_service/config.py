import requests
class UserService:
    url = "http://127.0.0.1:5001"
    create_user_endpoint = "/create"
    def __init__(self):
        pass

    def create_a_user(self, data):
        response = requests.post(self.url + self.create_user_endpoint, json=data)
        return response