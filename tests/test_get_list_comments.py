import os
import json
import pytest
import allure
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
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify if response is 200 when is getting comments successfully")
def test_get_list_comments():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    crud_comment = CrudComment()
    input_data = json.loads(file.read())
    response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"),
                                        input_data.get("page"),
                                        input_data.get("per_page"))
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify if response contains the status approved")
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
@pytest.mark.regression
@pytest.mark.security
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is 401 when is created with an invalid authorization token")
def test_get_invalid_token():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    crud_comment = CrudComment()
    input_data = json.loads(file.read())
    response = crud_comment.get_comment(URL, "TOKEN", input_data.get("orderby"),
                                        input_data.get("page"),
                                        input_data.get("per_page"))
    assert_that(response.status_code).is_equal_to(401)


@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is 404 when is getting a comment with an invalid ID")
def test_update_invalid_id():
    Login().login(USER, PASSWORD)
    invalid_id = 1000
    crud_comment = CrudComment()
    response = crud_comment.get_comment_by_id(URL, TOKEN, invalid_id)
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.functional
@pytest.mark.sanity
@pytest.mark.acceptance
@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if all ID of comments are different")
def test_different_id():
    Login().login(USER, PASSWORD)
    file = open('./testdata/get_comment/get_comment.json', "r")
    input_data = json.loads(file.read())
    print(get_id_comment_list(input_data))
    assert_that(len(get_id_comment_list(input_data)) == len(set(get_id_comment_list(input_data)))).is_true()


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
@allure.description("Verify if response is valid comparing with the schema")
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
    assert_that(response.status_code).is_equal_to(200)
    is_valid = validator_schema(output_data, response.as_dict[position])
    assert_that(is_valid[0], description=is_valid[1].errors).is_true()
