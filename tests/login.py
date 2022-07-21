import requests
from assertpy.assertpy import assert_that
import os
from pprint import pprint

BASE_URL = str(os.getenv('BASE_URL'))


def test_login():
    url = f'{BASE_URL}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = "username=alex&password=aifanyear"
    response = requests.post(url, headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)
