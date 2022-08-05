import os
import json
import allure
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login
from helpers.idslist import get_length_user
from utils.schema_validator import validator_schema
from helpers.name_generator import User_Data

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/create_user.json')
    User_Data().aleatory_email('create_user/create_user.json')
    User_Data().aleatory_name('create_user/create_user.json')
    User_Data().aleatory_first_name('create_user/create_user.json')
    User_Data().aleatory_last_name('create_user/create_user.json')
    User_Data().aleatory_roles('create_user/create_user.json')
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


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_duplicate_email():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/email_duplicate.json')
    User_Data().aleatory_name('create_user/email_duplicate.json')
    User_Data().aleatory_first_name('create_user/email_duplicate.json')
    User_Data().aleatory_last_name('create_user/email_duplicate.json')
    User_Data().aleatory_roles('create_user/email_duplicate.json')
    file = open('./testdata/create_user/email_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(500)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_duplicate_username():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_email('create_user/username_duplicate.json')
    User_Data().aleatory_name('create_user/username_duplicate.json')
    User_Data().aleatory_first_name('create_user/username_duplicate.json')
    User_Data().aleatory_last_name('create_user/username_duplicate.json')
    User_Data().aleatory_roles('create_user/username_duplicate.json')
    file = open('./testdata/create_user/username_duplicate.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(500)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_create_invalid_token():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/create_user5.json')
    User_Data().aleatory_email('create_user/create_user5.json')
    User_Data().aleatory_name('create_user/create_user5.json')
    User_Data().aleatory_first_name('create_user/create_user5.json')
    User_Data().aleatory_last_name('create_user/create_user5.json')
    User_Data().aleatory_roles('create_user/create_user5.json')
    file = open('./testdata/create_user/create_user5.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, "TOKEN", input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_create_invalid_email():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/invalid_email.json')
    User_Data().aleatory_name('create_user/invalid_email.json')
    User_Data().aleatory_first_name('create_user/invalid_email.json')
    User_Data().aleatory_last_name('create_user/invalid_email.json')
    User_Data().aleatory_roles('create_user/invalid_email.json')
    file = open('./testdata/create_user/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.MINOR)
def test_create_number_id():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/create_user2.json')
    User_Data().aleatory_email('create_user/create_user2.json')
    User_Data().aleatory_name('create_user/create_user2.json')
    User_Data().aleatory_first_name('create_user/create_user2.json')
    User_Data().aleatory_last_name('create_user/create_user2.json')
    User_Data().aleatory_roles('create_user/create_user2.json')
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    Lin= get_length_user(input_data)
    file = open('./testdata/create_user/create_user2.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Successfully response
    assert_that(response.status_code).is_equal_to(201)
    data = json.loads(response.text)
    id = data.get("id")
    # Successfully response
    assert_that(Lin <= id).is_true()


@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.MINOR)
def test_create_number_post():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data_in = json.loads(file.read())
    # Length before post
    Lin = get_length_user(input_data_in)
    User_Data().aleatory_username('create_user/create_user3.json')
    User_Data().aleatory_email('create_user/create_user3.json')
    User_Data().aleatory_name('create_user/create_user3.json')
    User_Data().aleatory_first_name('create_user/create_user3.json')
    User_Data().aleatory_last_name('create_user/create_user3.json')
    User_Data().aleatory_roles('create_user/create_user3.json')
    file = open('./testdata/create_user/create_user3.json', "r")
    input_data = json.loads(file.read())
    # Post
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Length after post
    assert_that(response.status_code).is_equal_to(201)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data_out = json.loads(file.read())
    Lout = get_length_user(input_data_out)
    # Successfully response
    assert_that(Lin+1 == Lout).is_true()


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.NORMAL)
def test_post_schema():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/create_user4.json')
    User_Data().aleatory_email('create_user/create_user4.json')
    User_Data().aleatory_name('create_user/create_user4.json')
    User_Data().aleatory_first_name('create_user/create_user4.json')
    User_Data().aleatory_last_name('create_user/create_user4.json')
    User_Data().aleatory_roles('create_user/create_user4.json')
    file = open('./testdata/create_user/create_user4.json', "r")
    schema = open('./testdata/create_user/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Successfully response
    assert_that(response.status_code).is_equal_to(201)
    is_valid = validator_schema(output_data, response.as_dict)
    # Successfully response
    assert_that(is_valid[0], description=is_valid[1].errors).is_true()


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_empty_username():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_email('create_user/empty_username.json')
    User_Data().aleatory_name('create_user/empty_username.json')
    User_Data().aleatory_first_name('create_user/empty_username.json')
    User_Data().aleatory_last_name('create_user/empty_username.json')
    User_Data().aleatory_roles('create_user/empty_username.json')
    file = open('./testdata/create_user/empty_username.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_empty_email():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/empty_email.json')
    User_Data().aleatory_name('create_user/empty_email.json')
    User_Data().aleatory_first_name('create_user/empty_email.json')
    User_Data().aleatory_last_name('create_user/empty_email.json')
    User_Data().aleatory_roles('create_user/empty_email.json')
    file = open('./testdata/create_user/empty_email.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
def test_empty():
    Login().login(USER, PASSWORD)
    User_Data().aleatory_username('create_user/empty.json')
    User_Data().aleatory_email('create_user/empty.json')
    file = open('./testdata/create_user/empty.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.create_user(URL, TOKEN, input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(400)

