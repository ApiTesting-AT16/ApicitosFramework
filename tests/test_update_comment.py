import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
import json

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_update_posts():

    payload = {'content': 'Hello, my name is Esteban A.',
               'status': 'approved'}

    headers = {
        'Authorization': TOKEN
    }
    response = requests.post(URL+'wp-json/wp/v2/comments/4', headers=headers, data=payload)
    post = response.json()
    pprint(post)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')
    # Data is not empty
    assert_that(response.json()).is_not_empty()
