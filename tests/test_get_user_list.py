import os
import json
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser
from helpers.login import Login
from cerberus import Validator

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


def test_get_user():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)
    # See if data sent is the same
    data = json.loads(response.text)
    assert_that(len(data) <= input_data.get("per_page")).is_true()


def test_get_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, "TOKEN", input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    # Error response
    assert_that(response.status_code).is_equal_to(401)


def test_get_schema():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    schema = open('../testdata/get_user/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    pprint(output_data)
    pprint(response.as_dict)
    # Error response
    assert_that(response.status_code).is_equal_to(200)
    validator = Validator(output_data, require_all=False)
    print(validator)
    is_valid = validator.validate(response.as_dict[0])
    assert_that(is_valid, description=validator.errors).is_true()


def test_different_id():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    Lin = 0
    i = 1
    lenpage = 1
    idslist=[]
    while lenpage >= 1:
        crud_user = CrudUser()
        response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), i, 1)
        data = json.loads(response.text)
        lenpage = len(data)
        if lenpage == 0:
            pass
        else:
            idslist.append(data[0].get("id"))
        i += 1
    print(idslist)
    assert_that(len(idslist) == len(set(idslist))).is_true()


def test_invalid_perpage():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  "a")
    # Successfully response
    assert_that(response.status_code).is_equal_to(400)


def test_invalid_page():
    Login().login(USER, PASSWORD)
    file = open('../testdata/get_user/get_user.json', "r")
    input_data = json.loads(file.read())
    crud_user = CrudUser()
    response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), "a",
                                  input_data.get("per_page"))
    # Successfully response
    assert_that(response.status_code).is_equal_to(400)
