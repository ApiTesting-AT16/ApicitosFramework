import os
import json
import allure
from assertpy.assertpy import assert_that
import pytest
from helpers.login import Login
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.name_generator import User_Data
from utils.request_manager import RequestsManager

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture
def preconditions():
    User_Data().aleatory_username('delete_user/create_user.json')
    User_Data().aleatory_email('delete_user/create_user.json')
    User_Data().aleatory_name('delete_user/create_user.json')
    User_Data().aleatory_first_name('delete_user/create_user.json')
    User_Data().aleatory_last_name('delete_user/create_user.json')
    User_Data().aleatory_roles('delete_user/create_user.json')
    file = open('./testdata/delete_user/create_user.json', "r")
    input_data = json.loads(file.read())
    request = RequestsManager()
    response = request.send_request(URL, TOKEN, input_data)
    return response


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.black_box
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user(preconditions):
    Login().login(USER, PASSWORD)
    query_param = "?reassign=1&force=true"
    crud_user = CrudUser()
    data = json.loads(preconditions.text)
    id_user = data["id"]
    request = RequestsManager()
    response = request.send_request('delete', TOKEN, id_user, query_param)
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
