import os
import json
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


def test_create_user():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_user/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Successfully response
    assert_that(response.status_code).is_equal_to(201)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(data["username"]).contains(input_data['username'])
    assert_that(data["email"]).contains(input_data['email'])
    assert_that(data["name"]).contains(input_data['name'])


def test_duplicate_email():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_user/email_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(500)


def test_duplicate_username():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_user/email_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(500)


def test_create_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_user/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, "TOKEN", input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(401)


def test_create_invalid_email():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_user/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)