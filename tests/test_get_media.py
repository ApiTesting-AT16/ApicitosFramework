import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_media import CrudMedia
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


def test_get_media():

    crud_comment = CrudMedia()
    response = crud_comment.get_media(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
