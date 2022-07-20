import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_read_posts():

    response = requests.delete(URL+'/7?reassign=0&force=true')
    print(response.json())
    assert_that(response.status_code).is_equal_to(401)

    headers = {
        'Authorization': TOKEN
    }
    response = requests.delete(URL+'/7?reassign=0&force=true', headers=headers)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)


test_read_posts()
