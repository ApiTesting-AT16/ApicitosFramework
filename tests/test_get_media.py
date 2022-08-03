import os
import pytest
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@pytest.mark.acceptance
def test_get_media():

    crud_media = CrudMedia()
    response = crud_media.get_media(URL, TOKEN)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
