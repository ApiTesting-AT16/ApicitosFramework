import os
import json
import pytest
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from helpers.login import Login
from crud_comment import CrudComment
from cerberus import Validator

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
ID = os.getenv('ID_COMMENT')


@pytest.mark.acceptance
def test_valid_update():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if response is 200
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.acceptance
def test_data_sent():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if data sent is the same
    data = json.loads(response.text)
    assert_that(data["author_name"]).contains(input_data['author_name'])
    assert_that(data["author_email"]).contains(input_data['author_email'])
    assert_that(data["status"]).contains(input_data['status'])


@pytest.mark.acceptance
def test_update_status_default():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/status.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if status change to approved when is filled with invalid data
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')


@pytest.mark.negative
def test_update_invalid_token():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, "TOKEN", input_data, ID)
    # Verify the response is 401 when is added with an invalid authorization token
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
def test_update_invalid_id():

    Login().login(USER, PASSWORD)
    invalid_id = 100
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, invalid_id)
    # Validate the response is 404 when is added with a invalid id
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.negative
def test_update_invalid_post_id():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/invalid_post_id.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Validate the response is 403 when is assigned to invalid post id
    assert_that(response.status_code).is_equal_to(403)


@pytest.mark.acceptance
def test_update_empty():

    Login().login(USER, PASSWORD)
    input_data = ''
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify when is sent empty input data the response is not emphy
    data = json.loads(response.text)
    assert_that(data).is_not_empty()


@pytest.mark.negative
def test_update_invalid_email():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.acceptance
def test_valid_update_and_get():

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if response is 200
    assert_that(response.status_code).is_equal_to(200)
    # Verify if the comment was updated correctly
    get = crud_comment.get_comment_by_id(URL, TOKEN, ID)
    data = json.loads(response.text)
    data_get = json.loads(get.text)
    assert_that(data["author_name"]).contains(data_get['author_name'])
    assert_that(data["status"]).contains(data_get["status"])


@pytest.mark.acceptance
def test_schema_of_update_comment():
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    schema = open('./testdata/update_comment/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    validator = Validator(output_data, require_all=False)
    print(validator)
    is_valid = validator.validate(response.as_dict)
    # Verify if response is valid comparing with the schema
    assert_that(is_valid, description=validator.errors).is_true()
