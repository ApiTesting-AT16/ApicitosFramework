import requests
from assertpy.assertpy import assert_that
from config import BASE_URL, ID
from pprint import pprint


def test_update_posts():

    response = requests.get((BASE_URL+ID))
    print(response.json())
    assert_that(response.status_code).is_equal_to(401)

    payload = {'name': 'marcelo'}

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsIm5hbWUiOiJhbGV4IiwiaWF0IjoxNjU4MjE0NDg0LCJleHAiOjE4MTU4OTQ0ODR9.n7Osm26MIlwna9y9YT-ZtWXYgdSu8PlCChOdnMWCLiI'
    }
    response = requests.post(BASE_URL+ID, headers=headers, data=payload)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)

test_update_posts()
