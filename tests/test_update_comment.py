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


def test_update_comment():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/update_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')


def test_update_invalid_token():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_comment/update_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, "TOKEN", input_data, ID)
    # Error response
    assert_that(response.status_code).is_equal_to(401)


def test_update_invalid_id():

    Login().login(USER, PASSWORD)
    invalid_id = 100
    file = open('../testdata/update_comment/update_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, invalid_id)
    # Error response
    assert_that(response.status_code).is_equal_to(404)
