import os
import json
import pytest
import allure
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login
from helpers.idslist import get_id_user_list
from utils.schema_validator import validator_schema
import random
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
@allure.description("Verify if response is 200 when is getting user successfully")
def test_get_user():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(len(data) <= input_data.get("per_page")).is_true()

@pytest.mark.black_box
@pytest.mark.negative
@pytest.mark.security
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is 401 when we send a invalid token")
def test_get_user_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, "TOKEN", input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify if schema of response is correctly when is getting user successfully")
def test_get_user_schema():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    schema = open('./testdata/get_user/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    position = random.randint(0, int(input_data.get("per_page"))-1)
    assert_that(response.status_code).is_equal_to(200)
    is_valid = validator_schema(output_data, response.as_dict[position])
    assert_that(is_valid[0], description=is_valid[1].errors).is_true()


@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that ID of users is different when is getting user successfully")
def test_get_user_different_id():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    print(get_id_user_list(input_data))
    assert_that(len(get_id_user_list(input_data)) == len(set(get_id_user_list(input_data)))).is_true()


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify that when we send a invalid Param Per_page send a response 400")
def test_get_user_invalid_perpage():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"), "a")
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.black_box
@pytest.mark.negative
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify that when we send a invalid Param Page send a response 400")
def test_get_user_invalid_page():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), "a",
                                  input_data.get("per_page"))
    assert_that(response.status_code).is_equal_to(400)
