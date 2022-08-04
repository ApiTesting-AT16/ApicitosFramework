import os
import json
import pytest
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


@pytest.fixture(scope="function")
def preconditions():
    file = open('./testdata/create_media/create_media.json', "r")
    input_data = json.loads(file.read())
    crud_media = CrudMedia()
    response = crud_media.create_media(URL, TOKEN, input_data[0], input_data[1].get("file"))
    return response


@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.sanity
@pytest.mark.acceptance
def test_update_media(preconditions):

    Login().login(USER, PASSWORD)
    file = open('./testdata/update_media/update_media.json', "r")
    input_data = json.loads(file.read())
    crud_media = CrudMedia()
    data = json.loads(preconditions.text)
    id_media = data["id"]
    response = crud_media.update_media(URL, TOKEN, input_data, id_media)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)