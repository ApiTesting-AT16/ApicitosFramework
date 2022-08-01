import os
import json
from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_media import CrudMedia
from helpers.login import Login

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


def test_create_media():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_media/create_media.json', "r")
    input_data = json.loads(file.read())
    crud_media = CrudMedia()
    response = crud_media.create_media(URL, TOKEN, input_data[0], input_data[1].get("file"))
    print(input_data[0].get('file'))
    # Successfully response
    assert_that(response.status_code).is_equal_to(201)
