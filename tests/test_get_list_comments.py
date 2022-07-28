import os
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


def test_get_list_comments():

    crud_comment = CrudComment()
    response = crud_comment.get_comment(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)


def test_get_invalid_token():
    Login().login(USER, PASSWORD)
    crud_comment = CrudComment()
    response = crud_comment.get_comment(URL, "TOKEN")
    # Error response
    assert_that(response.status_code).is_equal_to(401)
