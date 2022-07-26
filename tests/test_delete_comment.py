import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID = os.getenv('ID')


def test_read_posts():

    crud_comment = CrudComment()
    response = crud_comment.delete_comment(URL, TOKEN, ID)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
