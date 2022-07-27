import json
import os
import jsonpath
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
URL = os.getenv('BASE_URL')

def test_create_posts():
    Login().login(USER, PASSWORD)
    load_dotenv()
    TOKEN = os.getenv('ACCESS_TOKEN')
    crud_users = CrudUser()
    response = crud_users.get_user(URL, TOKEN)
    responseJson = json.loads(response.text)
    Lin = len(responseJson)
    crud_users = CrudUser()
    response = crud_users.create_user(URL, TOKEN, 'ecomer', 'ecomo', 'ecomo@gmail.com', 'Jala17')
    responseJson = json.loads(response.text)
    pprint(response.status_code)
    pprint(responseJson)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(jsonpath.jsonpath(responseJson, '$.name')).contains("ecomo")
    crud_users = CrudUser()
    response = crud_users.get_user(URL, TOKEN)
    responseJson = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    Lout = len(responseJson)
    #assert_that(Lout).is_equal_to(Lin+1)
    print(Lout)