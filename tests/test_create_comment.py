import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_create_comment():

    payload = {'post': '1',
               'author_name': 'Carme Torrez',
               'author_email': 'carmen@gmail.com',
               'content': 'Commentary posting...',
               'status': 'approved'}

    headers = {
        'Authorization': TOKEN
    }
    response = requests.post(URL+'wp-json/wp/v2/comments', headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(201)
