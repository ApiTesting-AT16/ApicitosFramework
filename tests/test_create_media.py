import os
import json
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


def test_create_media():
    Login().login(USER, PASSWORD)
    file = open('../testdata/create_media/create_media.json', "r")
    input_data = json.loads(file.read())
    print("Hola reynel ", input_data[1])
    crud_media = CrudMedia()
    response = crud_media.create_media(URL, TOKEN, input_data[0], input_data[1].get("file"))
    #response = crud_media.create_media(URL, TOKEN, input_data, 3)
    data = json.loads(response.text)
    # Successfully response
    assert_that(response.status_code).is_equal_to(201)
    #assert_that(data["alt_text"]).contains(input_data['alt_text'])
    # See if data sent is the same
    data = json.loads(response.text)


