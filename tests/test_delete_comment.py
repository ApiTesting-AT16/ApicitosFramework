import os
import json
import allure
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_comment import CrudComment
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope="module")
def preconditions():
    file = open('./testdata/delete_comment/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    return response


@pytest.mark.regression
@pytest.mark.blackbox
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_comment(preconditions):
    Login().login(USER, PASSWORD)
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.delete_comment(URL, TOKEN, id_comment)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
