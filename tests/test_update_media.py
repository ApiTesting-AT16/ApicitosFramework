import os
import json
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from helpers.login import Login
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
ID = os.getenv('ID_COMMENT')


def test_update_media():

    Login().login(USER, PASSWORD)
    file = open('../testdata/update_media.json', "r")
    input_data = json.loads(file.read())
    crud_media = CrudMedia()
    response = crud_media.update_media(URL, TOKEN, input_data, 5)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)