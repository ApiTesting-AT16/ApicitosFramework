import requests
import os
import json
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_media import CrudMedia

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
ID = os.getenv('ID_USER')

def test_update_media():

  file = open('../testdata/update_media/update_media.json', "r")
  input_data = json.loads(file.read())
  crud_media = CrudMedia()
  response = crud_media.update_media(URL, TOKEN, input_data, 8)
  assert_that(response.status_code).is_equal_to(200)

