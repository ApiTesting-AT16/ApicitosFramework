import os
import json
from assertpy.assertpy import assert_that
import pytest
from cerberus import Validator
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.acceptance
def test_create_user():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/create_user.json', "r")
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
    assert_that(data["first_name"]).contains(input_data['first_name'])
    assert_that(data["last_name"]).contains(input_data['last_name'])
    assert_that(data["roles"][0]).contains(input_data['roles'])


@pytest.mark.negative
def test_duplicate_email():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/email_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(500)


@pytest.mark.negative
def test_duplicate_username():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/email_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(500)


@pytest.mark.negative
def test_create_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, "TOKEN", input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
def test_create_invalid_email():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.acceptance
def test_create_number_id():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    Lin=0
    i = 1
    lenpage=1
    while lenpage >= 1:
        crud_user = CrudUser()
        response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), i,
                                      input_data.get("per_page"))
        data = json.loads(response.text)
        lenpage = len(data)
        Lin += lenpage
        i += 1
    file = open('./testdata/create_user/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(201)
    data = json.loads(response.text)
    id = data.get("id")
    assert_that(Lin <= id).is_true()


@pytest.mark.acceptance
def test_create_number_post():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    Lin = 0
    i = 1
    lenpage = 1
    while lenpage >= 1:
        crud_user = CrudUser()
        response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), i,
                                      input_data.get("per_page"))
        data = json.loads(response.text)
        lenpage = len(data)
        Lin += lenpage
        i += 1
    file = open('./testdata/create_user/create_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # lenght after post
    assert_that(response.status_code).is_equal_to(201)
    Lout = 0
    j = 1
    lenpageout = 1
    while lenpageout >= 1:
        crud_user = CrudUser()
        response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), j,
                                      input_data.get("per_page"))
        data = json.loads(response.text)
        lenpageout = len(data)
        Lout += lenpageout
        j += 1
    print(Lin)
    print(Lout)
    assert_that(Lin+1 == Lout).is_true()


@pytest.mark.acceptance
def test_post_schema():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/create_user.json', "r")
    schema = open('./testdata/create_user/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(201)
    validator = Validator(output_data, require_all=False)
    print(validator)
    is_valid = validator.validate(response.as_dict)
    assert_that(is_valid, description=validator.errors).is_true()


@pytest.mark.negative
def test_empty_username():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/empty_username.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.negative
def test_empty_email():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/empty_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.negative
def test_empty():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_user/empty.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Successfully response
    assert_that(response.status_code).is_equal_to(400)
    # See if data sent is the same
