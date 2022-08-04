import os
import pytest
from helpers.login import Login
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.sanity
@pytest.mark.acceptance
def test_get_media():
    Login().login(USER, PASSWORD)
    crud_media = CrudMedia()
    response = crud_media.get_media(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
