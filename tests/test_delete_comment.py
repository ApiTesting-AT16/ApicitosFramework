import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_read_posts():

    headers = {
        'Authorization': TOKEN
    }
    response = requests.delete(URL+'wp-json/wp/v2/comments/6', headers=headers)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)
