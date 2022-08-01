import os
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_delete_media():

    query_param = "9?reassign=1&force=true"
    crud_media = CrudMedia()
    response = crud_media.delete_media(URL, TOKEN, query_param)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
