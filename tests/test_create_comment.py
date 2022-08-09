import os
import json
import pytest
import allure
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_comment import CrudComment
from helpers.login import Login
from helpers.name_generator import Comment_Data
from utils.schema_validator import validator_schema

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify if response is 201 when is created the comment successfully")
def test_create_comment():
    Comment_Data().aleatory_author_email('create_comment/create_comment.json')
    Comment_Data().aleatory_author_name('create_comment/create_comment.json')
    Comment_Data().aleatory_content('create_comment/create_comment.json')
    Comment_Data().aleatory_status('create_comment/create_comment.json')
    Login().login(USER, PASSWORD)
    Comment_Data().aleatory_content('create_comment/create_comment.json')
    file = open('./testdata/create_comment/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    print(response)
    assert_that(response.status_code).is_equal_to(201)


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if status is approved when is created the comment successfully")
def test_create_status():
    Comment_Data().aleatory_author_email('create_comment/create_comment3.json')
    Comment_Data().aleatory_author_name('create_comment/create_comment3.json')
    Comment_Data().aleatory_content('create_comment/create_comment3.json')
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_comment/create_comment3.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    data = json.loads(response.text)
    print (data)
    assert_that(data["status"]).contains('approved')


@pytest.mark.negative
@pytest.mark.blackbox
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is 401 when is created with an invalid authorization token")
def test_get_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_comment/create_comment2.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, "TOKEN", input_data)
    # Error response
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
@pytest.mark.blackbox
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify if response is 409 when the comment created is duplicated")
def test_create_duplicate_comment():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_comment/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    print(response)
    assert_that(response.status_code).is_equal_to(409)


@pytest.mark.negative
@pytest.mark.blackbox
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is 400 when the email data is invalid")
def test_create_invalid_email():
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_comment/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, TOKEN, input_data)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify if response is valid comparing with the schema")
def test_get_schema():
    Comment_Data().aleatory_author_email('create_comment/create_comment.json')
    Comment_Data().aleatory_author_name('create_comment/create_comment.json')
    Comment_Data().aleatory_content('create_comment/create_comment.json')
    Comment_Data().aleatory_status('create_comment/create_comment.json')
    Login().login(USER, PASSWORD)
    file = open('./testdata/create_comment/create_comment.json', "r")
    schema = open('./testdata/create_comment/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, TOKEN, input_data)
    position = 1
    # Error response
    assert_that(response.status_code).is_equal_to(201)
    is_valid = validator_schema(output_data, response.as_dict)
    assert_that(is_valid[0], description=is_valid[1].errors).is_true()
