import os
import requests
import fileinput
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
        for token in fileinput.FileInput("../.env", inplace=1):
            if token.startswith("ACCESS_TOKEN = 'Bearer "):
                new_token = token.replace(token,
                                          f"ACCESS_TOKEN = '{response.json().get('token_type')} {response.json().get('jwt_token')}'")
                print(new_token)
            else:
                print(token, end='')
        return response.json()
