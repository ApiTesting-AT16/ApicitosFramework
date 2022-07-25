import os
import requests
from dotenv import load_dotenv


load_dotenv()
URL = os.getenv('BASE_URL')


class Login:
    @staticmethod
    def login(username, password):
        url = "{}/wp-json/api/v1/token".format(URL)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = f"username={username}&password={password}"
        response = requests.post(url, headers=headers, data=payload)
        return response
