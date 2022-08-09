import json
import os
import namegenerator
import allure
import fileinput
import random
from dotenv import load_dotenv
from crud_users import CrudUser
load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


class User_Data:

    @staticmethod
    @allure.step('Generate Email')
    def aleatory_email(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "email":'):
                number_email = random.randint(1, 999)
                new_line = line.replace(line,
                                          f'  "email": "{namegenerator.gen()}{number_email}@gmail.com",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change email'

    @staticmethod
    @allure.step('Generate Username')
    def aleatory_username(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "username":'):
                new_line = line.replace(line,
                                          f'  "username": "{namegenerator.gen().split("-")[2]}{namegenerator.gen().split("-")[1]}{namegenerator.gen().split("-")[0]}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change username'

    @staticmethod
    @allure.step('Generate Name')
    def aleatory_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "name":'):
                new_line = line.replace(line,
                                          f'  "name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change name'

    @staticmethod
    @allure.step('Generate First Name')
    def aleatory_first_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "first_name":'):
                new_line = line.replace(line,
                                          f'  "first_name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change first_name'

    @staticmethod
    @allure.step('Generate Last Name')
    def aleatory_last_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "last_name":'):
                new_line = line.replace(line,
                                        f'  "last_name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change last_name'

    @staticmethod
    @allure.step('Generate Role')
    def aleatory_roles(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "roles":'):
                roles = ['administrator', 'subscriber']
                new_line = line.replace(line,
                                          f'  "roles": "{random.choice(roles)}"')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change role'

    @staticmethod
    @allure.step('Generate duplicate user')
    def aleatory_duplicate_username(load):
        i = 1
        lenpage = 1
        idslist = []
        while lenpage >= 1:
            crud_user = CrudUser()
            response = crud_user.get_user(URL, TOKEN, "id", i, 1)
            data = json.loads(response.text)
            lenpage = len(data)
            if lenpage == 0:
                pass
            else:
                idslist.append(data[0].get("slug"))
            i += 1
        username = random.choice(idslist)
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "username":'):
                new_line = line.replace(line, f'  "username": "{username}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change username'

    @staticmethod
    @allure.step('Generate duplicate email')
    def aleatory_duplicate_email(load, duplicate):
        for line in fileinput.FileInput(f"./testdata/{duplicate}", inplace=1):
            if line.startswith(f'  "email":'):
                email_line = line
                print(line, end='')
            else:
                print(line, end='')
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "email":'):
                new_line = line.replace(line, email_line)
                print(new_line, end='')
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change email'


class Comment_Data:

    @staticmethod
    @allure.step('Generate Author Email')
    def aleatory_author_email(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "author_email":'):
                number_email = random.randint(1, 999)
                new_line = line.replace(line,
                                        f'  "author_email": "{namegenerator.gen()}{number_email}@gmail.com",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change author_email'

    @staticmethod
    @allure.step('Generate Author Name')
    def aleatory_author_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "author_name":'):
                new_line = line.replace(line,
                                        f'  "author_name": "{namegenerator.gen().split("-")[2]}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change author_name'

    @staticmethod
    @allure.step('Generate Content')
    def aleatory_content(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "content":'):
                new_line = line.replace(line,
                                        f'  "content": "{namegenerator.gen()}",')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change content'

    @staticmethod
    @allure.step('Generate Status')
    def aleatory_status(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "status":'):
                status = ['approved', 'hold', 'spam', 'trash']
                new_line = line.replace(line,
                                        f'  "status": "{random.choice(status)}"')
                print(new_line)
            else:
                print(line, end='')
        allure.attach(str(new_line), 'Result', allure.attachment_type.TEXT)
        return 'change status'
