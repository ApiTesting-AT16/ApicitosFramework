import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_create_posts():

    response = requests.get(URL)
    print(response.json())
    assert_that(response.status_code).is_equal_to(401)

    payload = {'username': 'esteban56',
               'name': 'Esteban',
               'email': 'esteban@gmail.com',
               'password': '123456'}

    headers = {
        'Authorization': TOKEN
    }
    response = requests.post(URL, headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(201)


test_create_posts()
