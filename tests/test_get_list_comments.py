import os
from assertpy.assertpy import assert_that
import pytest
from dotenv import load_dotenv
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@pytest.mark.acceptance
def test_get_list_comments():

    crud_comment = CrudComment()
    response = crud_comment.get_comment(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
