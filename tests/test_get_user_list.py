import json
import os

import jsonpath
import requests
from assertpy.assertpy import assert_that, soft_assertions
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_get_posts():

    response = requests.get(URL+'wp-json/wp/v2/users')
    #print(response.json())
    assert_that(response.status_code).is_equal_to(401)
    headers = {
        'Authorization': TOKEN
    }
    response = requests.get(URL+'wp-json/wp/v2/users', headers=headers)
    #pprint(response.json())
    responseJson = json.loads(response.text)
    print(responseJson)
    print('/n esta es la longitud de response/n')
    print(len(responseJson))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        #for i in range(0, len(responseJson)):
        #    assert_that(jsonpath.jsonpath(responseJson[i], '$.name')).is_alpha()

    assert_that(jsonpath.jsonpath(responseJson[0], '$.name')).contains("Abraham")
    #assert_that(jsonpath.jsonpath(responseJson[0], '$.name')).is_alpha()
    print(type(jsonpath.jsonpath(responseJson[0], '$.name')))
    print(type(jsonpath.jsonpath(responseJson[0], '$.user_name')))

    schema={
            "id": {"type": "integrer"},
            "name": {"type": "string"},
            "url": {"type": "string"},
            "description": {"type": "string"},
            "link": {"type": "string"},
            "slug": {"type": "string"},
            "avatar_urls": {"type": "object"},
            "meta": {"type": "object"},
            "_links": {"type": "object"}
            }
