import os
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_get_users():

    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
