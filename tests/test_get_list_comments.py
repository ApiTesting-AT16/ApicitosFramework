import os
import json
import pytest

from assertpy.assertpy import assert_that
from dotenv import load_dotenv
from crud_comment import CrudComment
from helpers.login import Login
from helpers.idslist import get_id_comment_list
from utils.schema_validator import validator_schema


load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
@pytest.mark.regression
def test_get_list_comments():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    crud_comment = CrudComment()
    input_data = json.loads(file.read())
    response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"),
                                        input_data.get("page"),
                                        input_data.get("per_page"))
    # Successfully response
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
def test_get_status():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    crud_comment = CrudComment()
    input_data = json.loads(file.read())
    response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"),
                                        input_data.get("page"),
                                        input_data.get("per_page"))
    data = json.loads(response.text)
    print(data)
    assert_that(str(data[0])).contains('approved')


@pytest.mark.negative
@pytest.mark.blackbox
def test_get_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    crud_comment = CrudComment()
    input_data = json.loads(file.read())
    response = crud_comment.get_comment(URL, "TOKEN", input_data.get("orderby"),
                                        input_data.get("page"),
                                        input_data.get("per_page"))
    # Error response
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
@pytest.mark.blackbox
def test_update_invalid_id():
    Login().login(USER, PASSWORD)
    invalid_id = 100
    crud_comment = CrudComment()
    response = crud_comment.get_comment_by_id(URL, TOKEN, invalid_id)
    # Validate the response is 404 when is added with a invalid id
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.functional
@pytest.mark.sanity
@pytest.mark.blackbox
def test_different_id():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    input_data = json.loads(file.read())
    print(get_id_comment_list(input_data))
    assert_that(len(get_id_comment_list(input_data)) == len(set(get_id_comment_list(input_data)))).is_true()


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.blackbox
@pytest.mark.regression
def test_get_schema():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    schema = open('./testdata/get_comment/schema.json', "r")
    input_data = json.loads(file.read())
    output_data = json.loads(schema.read())
    crud_comment = CrudComment()
    response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"), input_data.get("page"),
                                  input_data.get("per_page"))
    #position = random.randint(0, int(input_data.get("per_page"))-1)
    position = 1
    # Error response
    assert_that(response.status_code).is_equal_to(200)
    is_valid = validator_schema(output_data, response.as_dict[position])
    assert_that(is_valid[0], description=is_valid[1].errors).is_true()
    



