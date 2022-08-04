import os
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@pytest.mark.acceptance
def test_delete_comment():

    id_comment = "3"
    crud_comment = CrudComment()
    response = crud_comment.delete_comment(URL, TOKEN, id_comment)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
