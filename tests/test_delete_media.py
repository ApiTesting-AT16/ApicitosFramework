import os
import json
import pytest
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


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
def test_delete_media(preconditions):
    query_param = "?reassign=1&force=true"
    crud_media = CrudMedia()
    data = json.loads(preconditions.text)
    id_media = data["id"]
    response = crud_media.delete_media(URL, TOKEN, id_media, query_param)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
