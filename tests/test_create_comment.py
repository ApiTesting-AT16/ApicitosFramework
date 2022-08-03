import os
import json
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@pytest.mark.acceptance
def test_create_comment():

    file = open('./testdata/create_comment.json', "r")
    input_data = json.loads(file.read())
    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, input_data)
    assert_that(response.status_code).is_equal_to(201)
