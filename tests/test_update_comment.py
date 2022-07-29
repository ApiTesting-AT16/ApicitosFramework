import os
import json
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from helpers.login import Login
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
ID = os.getenv('ID_COMMENT')


def test_valid_update():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if response is 200
    assert_that(response.status_code).is_equal_to(200)


def test_data_sent():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if data sent is the same
    data = json.loads(response.text)
    assert_that(data["author_name"]).contains(input_data['author_name'])
    assert_that(data["author_email"]).contains(input_data['author_email'])
    assert_that(data["status"]).contains(input_data['status'])


def test_update_status_default():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/status.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify if status change to approved when is filled with invalid data
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')


def test_update_invalid_token():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, "TOKEN", input_data, ID)
    # Verify the response is 401 when is added with an invalid authorization token
    assert_that(response.status_code).is_equal_to(401)


def test_update_invalid_id():

    Login().login(USER, PASSWORD)
    invalid_id = 100
    file = open('../testdata/update_comment/update_valid_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, invalid_id)
    # Validate the response is 404 when is added with a invalid id
    assert_that(response.status_code).is_equal_to(404)


def test_update_invalid_post_id():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/invalid_post_id.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Validate the response is 403 when is assigned to invalid post id
    assert_that(response.status_code).is_equal_to(403)


def test_update_empty():

    Login().login(USER, PASSWORD)
    invalid_id = 100
    input_data = ''
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, invalid_id)
    # Verify when is sent empty input data the response is not emphy
    data = json.loads(response.text)
    assert_that(data).is_not_empty()


def test_update_invalid_email():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)
