import os
import json
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID = os.getenv('ID_USER')


def test_update_user():

    file = open('../testdata/update_user.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudUser()
    response = crud_users.update_user(URL, TOKEN, input_data, ID)
    assert_that(response.status_code).is_equal_to(200)
