import os
import json
import allure
from dotenv import load_dotenv
from crud_users import CrudUser
from crud_comment import CrudComment

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


@allure.step('Get Id user list')
def get_id_user_list(input_data):
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
    return idslist


@allure.step('Get Id comment list')
def get_id_comment_list(input_data):
    i = 1
    lenpage = 1
    idslist=[]
    while lenpage >= 1:
        crud_comment = CrudComment()
        response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"), i, 1)
        data = json.loads(response.text)
        lenpage = len(data)
        if lenpage == 0:
            pass
        else:
            idslist.append(data[0].get("id"))
        i += 1
    return idslist


@allure.step('Get Length User')
def get_length_user(input_data):
    Lin = 0
    i = 1
    lenpage = 1
    while lenpage >= 1:
        crud_user = CrudUser()
        response = crud_user.get_user(URL, TOKEN, input_data.get("orderby"), i,
                                      input_data.get("per_page"))
        data = json.loads(response.text)
        lenpage = len(data)
        Lin += lenpage
        i += 1
    return Lin


@allure.step('Get Length Comments')
def get_length_comment(input_data):
    Lin = 0
    i = 1
    lenpage = 1
    while lenpage >= 1:
        crud_comment = CrudComment()
        response = crud_comment.get_comment(URL, TOKEN, input_data.get("orderby"), i,
                                      input_data.get("per_page"))
        data = json.loads(response.text)
        lenpage = len(data)
        Lin += lenpage
        i += 1
    return Lin
