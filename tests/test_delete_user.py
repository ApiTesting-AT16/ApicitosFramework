import os

import pytest
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')

@pytest.mark.acceptance
@pytest.mark.black_box
def test_delete_user():

    query_param = "3?reassign=1&force=true"
    crud_user = CrudUser()
    response = crud_user.delete_user(URL, TOKEN, query_param)
    # Successfully response
    assert_that(response.status_code).is_equal_to(404)

@pytest.mark.negative
@pytest.mark.black_box
def test_delete_user_invalid_id():

    query_param = "50?reassign=1&force=true"
    crud_user = CrudUser()
    response = crud_user.delete_user(URL, TOKEN, query_param)
    # Successfully response
    assert_that(response.status_code).is_equal_to(404)
