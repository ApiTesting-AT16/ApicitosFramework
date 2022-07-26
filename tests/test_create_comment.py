import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_create_comment():

    crud_users = CrudComment()
    response = crud_users.create_comment(URL, TOKEN, '1', 'IVAN', 'Ivancito@gmail.com', 'aaa12', 'approved')
    assert_that(response.status_code).is_equal_to(201)
