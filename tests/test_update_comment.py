import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
import json
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID = os.getenv('ID')


def test_update_posts():

    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, '1', 'IVAN', 'Ivancito@gmail.com', 'aaa123', 'approved', ID)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')

