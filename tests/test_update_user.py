import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_update_posts():

    response = requests.get((URL+'wp-json/wp/v2/users/13'))
    print(response.json())
    assert_that(response.status_code).is_equal_to(401)

    payload = {'name': 'estebitan',
               'email': 'estebanquito@gmail.com'}

    headers = {
        'Authorization': TOKEN
    }
    response = requests.post(URL+'wp-json/wp/v2/users/13', headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)
