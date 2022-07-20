import requests
from assertpy.assertpy import assert_that
from config import BASE_URL, TOKEN
from pprint import pprint


def test_get_posts():

    response = requests.get(BASE_URL)
    print(response.json())
    assert_that(response.status_code).is_equal_to(401)

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsIm5hbWUiOiJhbGV4IiwiaWF0IjoxNjU4MjE0NDg0LCJleHAiOjE4MTU4OTQ0ODR9.n7Osm26MIlwna9y9YT-ZtWXYgdSu8PlCChOdnMWCLiI'
    }
    response = requests.get(BASE_URL, headers=headers)
    pprint(response.json())
    assert_that(response.status_code).is_equal_to(200)

test_get_posts()
