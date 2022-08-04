import os
import json
import pytest
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from helpers.login import Login
from crud_comment import CrudComment
from utils.schema_validator import validator_schema

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope="module")
def preconditions():
    file = open('./testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    return response


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.acceptance
def test_valid_update(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify if response is 200
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.black_box
@pytest.mark.acceptance
@pytest.mark.sanity
def test_data_sent(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify if data sent is the same
    data = json.loads(response.text)
    assert_that(data["author_name"]).contains(input_data['author_name'])
    assert_that(data["author_email"]).contains(input_data['author_email'])
    assert_that(data["status"]).contains(input_data['status'])


@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
def test_update_status_default(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/status.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify if status change to approved when is filled with invalid data
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')


@pytest.mark.black_box
@pytest.mark.negative
@pytest.mark.security
def test_update_invalid_token(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, "TOKEN", input_data, id_comment)
    # Verify the response is 401 when is added with an invalid authorization token
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.black_box
@pytest.mark.negative
def test_update_invalid_id(preconditions):
    Login().login(USER, PASSWORD)
    invalid_id = 100
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, invalid_id)
    # Validate the response is 404 when is added with a invalid id
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.black_box
@pytest.mark.negative
def test_update_invalid_post_id(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/invalid_post_id.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Validate the response is 403 when is assigned to invalid post id
    assert_that(response.status_code).is_equal_to(403)


@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
def test_update_empty(preconditions):
    Login().login(USER, PASSWORD)
    input_data = ''
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify when is sent empty input data the response is not emphy
    data = json.loads(response.text)
    assert_that(data).is_not_empty()


@pytest.mark.black_box
@pytest.mark.negative
def test_update_invalid_email(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)


@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
def test_valid_update_and_get(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    # Verify if response is 200
    assert_that(response.status_code).is_equal_to(200)
    # Verify if the comment was updated correctly
    get = crud_comment.get_comment_by_id(URL, TOKEN, id_comment)
    data = json.loads(response.text)
    data_get = json.loads(get.text)
    assert_that(data["author_name"]).contains(data_get['author_name'])
    assert_that(data["status"]).contains(data_get["status"])


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.black_box
@pytest.mark.acceptance
def test_schema_of_update_comment(preconditions):
    Login().login(USER, PASSWORD)
    file = open('./testdata/update_comment/update_valid_comment.json', "r")
    schema = open('./testdata/update_comment/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.update_comment(URL, TOKEN, input_data, id_comment)
    is_valid = validator_schema(output_data, response.as_dict)
    # Verify if response is valid comparing with the schema
    assert_that(is_valid, description=is_valid[1].errors).is_true()
