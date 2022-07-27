import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
import json
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID = os.getenv('ID_COMMENT')


def test_update_comment():

    file = open('../testdata/update_comment.json', "r")
    input_data = json.loads(file.read())
    crud_comment = CrudComment()
    response = crud_comment.update_comment(URL, TOKEN, input_data, ID)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(data["status"]).contains('approved')

