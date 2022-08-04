import os
import json
import random
from pprint import pprint
from helpers.idslist import get_id_user_list
import pytest
from assertpy.assertpy import assert_that
from cerberus import Validator
from dotenv import load_dotenv


from crud_users import CrudUser
from helpers.login import Login

load_dotenv()
ID = os.getenv('ID_USER')
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

@pytest.fixture(scope="function")
def preconditions():
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    result = get_id_user_list(input_data)

    return result

@pytest.mark.acceptance
def test_update_user(preconditions):

    file = open('./testdata/update_user/update_user.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudUser()
    data = preconditions
    id_users = data[random.randint(1, len(data)-1)]
    response = crud_users.update_user(URL, TOKEN, input_data, id_users)
    assert_that(response.status_code).is_equal_to(400)
    data = json.loads(response.text)
    assert_that(data["email"]).contains(input_data['email'])
    assert_that(data["name"]).contains(input_data['name'])
    assert_that(data["first_name"]).contains(input_data['first_name'])
    assert_that(data["last_name"]).contains(input_data['last_name'])
    assert_that(data["roles"][0]).contains(input_data['roles'])


@pytest.mark.acceptance
def test_update_schema(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_user/update_user.json', "r")
    schema = open('./testdata/update_user/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_user = CrudUser()
    data = preconditions
    id_users = data[random.randint(1, len(data)-1)]
    response = crud_user.update_user(URL, TOKEN, input_data, id_users)
    # Error response
    assert_that(response.status_code).is_equal_to(200)
    validator = Validator(output_data, require_all=False)
    print(validator)
    is_valid = validator.validate(response.as_dict)
    assert_that(is_valid, description=validator.errors).is_true()


@pytest.mark.negative
def test_update_invalid_token(preconditions):

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_user/update_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    data = preconditions
    id_users = data[random.randint(1, len(data)-1)]
    response = crud_user.update_user(URL, "TOKEN", input_data, id_users)
    # Verify the response is 401 when is added with an invalid authorization token
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
def test_update_invalid_id():

    Login().login(USER, PASSWORD)
    invalid_id = 100
    file = open('./testdata/update_user/update_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.update_user(URL, TOKEN, input_data, invalid_id)
    # Validate the response is 404 when is added with a invalid id
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.negative
def test_update_invalid_email(preconditions):

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_user/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    data = preconditions
    id_users = data[random.randint(1, len(data)-1)]
    response = crud_user.update_user(URL, TOKEN, input_data, id_users)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.negative
def test_empty(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_user/empty.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    data = preconditions
    id_users = data[random.randint(1, len(data)-1)]
    response = crud_user.update_user(URL, TOKEN, input_data, id_users)
    # Successfully response
    assert_that(response.status_code).is_equal_to(400)
