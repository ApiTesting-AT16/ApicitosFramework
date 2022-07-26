import os
import allure
import requests
import fileinput
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')


class Login:
    @staticmethod
    @allure.step('Get Token')
    def login(username, password):
        url = "{}/wp-json/api/v1/token".format(URL)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = f"username={username}&password={password}"
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            for token in fileinput.FileInput("./.env", inplace=1):
                if token.startswith("ACCESS_TOKEN = 'Bearer "):
                    new_token = token.replace(token, f"ACCESS_TOKEN = '{response.json().get('token_type')} {response.json().get('jwt_token')}'")
                    print(new_token)
                else:
                    print(token, end='')
        else:
            pass
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response.json()

