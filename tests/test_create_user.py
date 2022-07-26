import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser


load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID_POST = os.getenv('ID')


def test_create_posts():

    crud_users = CrudUser()
    response = crud_users.create_user(URL, TOKEN, 'Ivanuser', 'IVAN', 'Ivancito@gmail.com', 'aaa123')
    pprint(response.as_dict)
    pprint(response.text)
    pprint(response.status_code)
    pprint(response.headers)
    assert_that(response.status_code).is_equal_to(201)
    #assert_that(jsonpath.jsonpath(response, '$.name')[0]).contains("Alvaro")