import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
import pytest

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_create_posts():

    payload = {'username': 'S100',
               'name': 'Sandro',
               'email': 'sandro@gmail.com',
               'password': '123456'}

    headers = {
        'Authorization': TOKEN
    }
    response = requests.post(URL+'wp-json/wp/v2/users', headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(201)
