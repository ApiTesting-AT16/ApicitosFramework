import os

import jsonpath
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
import pytest

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID_POST = os.getenv('ID')

def test_create_posts():

    payload = {'username': 'Alvaro',
               'name': 'Sandro',
               'email': 'sandro@gmail.com',
               'password': '123456'}

    headers = {
        'Authorization': TOKEN
    }
    crud_post = CrudPost()
    response = crud_post.retrieve_post(URL, TOKEN, ID_POST)
    pprint(response.json())
    responseJson = json.loads(response.text)
    print(responseJson)
    print('/n esta es la longitud de response/n')
    print(len(responseJson))
    assert_that(response.status_code).is_equal_to(201)
    assert_that(jsonpath.jsonpath(responseJson, '$.name')[0]).contains("Alvaro")