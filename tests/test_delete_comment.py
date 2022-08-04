import os
import json
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@pytest.fixture(scope="function")
def preconditions():
    file = open('./testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    return response


@pytest.mark.acceptance
def test_delete_comment(preconditions):
    crud_comment = CrudComment()
    data = json.loads(preconditions.text)
    id_comment = data["id"]
    response = crud_comment.delete_comment(URL, TOKEN, id_comment)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
