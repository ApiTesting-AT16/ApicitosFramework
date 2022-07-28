import os
import json
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser


load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_create_user():

    file = open('../testdata/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudUser()
    response = crud_users.create_user(URL, TOKEN, input_data)
    assert_that(response.status_code).is_equal_to(201)
    #assert_that(jsonpath.jsonpath(response, '$.name')[0]).contains("Alvaro")