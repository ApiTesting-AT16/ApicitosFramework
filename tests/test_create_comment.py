import os
import json
import pytest
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_comment import CrudComment
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.acceptance
def test_create_comment():

    file = open('../testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    print(response)
    assert_that(response.status_code).is_equal_to(201)


@pytest.mark.acceptance
def test_create_status():

    #Login().login(USER, PASSWORD)
    file = open('../testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, TOKEN, input_data)
    # See if status change to approved when is filled with invalid data
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')


@pytest.mark.negative
def test_get_invalid_token():
    #Login().login(USER, PASSWORD)
    crud_comment = CrudComment()
    response = crud_comment.get_comment(URL, "TOKEN")
    # Error response
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
def test_create_duplicate_comment():
    file = open('../testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    print(response)
    assert_that(response.status_code).is_equal_to(409)


@pytest.mark.negative
def test_update_invalid_email():
    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/invalid_email.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.create_comment(URL, TOKEN, input_data)
    # Verify when author email is filled with invalid param display a response 400
    assert_that(response.status_code).is_equal_to(400)

