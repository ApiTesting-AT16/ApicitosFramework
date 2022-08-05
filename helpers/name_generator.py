import namegenerator
import fileinput
import random


class User_Data:

    @staticmethod
    def aleatory_email(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "email":'):
                number_email = random.randint(1, 999)
                new_line = line.replace(line,
                                          f'  "email": "{namegenerator.gen()}{number_email}@gmail.com",')
                print(new_line)
            else:
                print(line, end='')
        return 'change email'

    @staticmethod
    def aleatory_username(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "username":'):
                new_line = line.replace(line,
                                          f'  "username": "{namegenerator.gen().split("-")[2]}{namegenerator.gen().split("-")[1]}{namegenerator.gen().split("-")[0]}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change username'

    @staticmethod
    def aleatory_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "name":'):
                new_line = line.replace(line,
                                          f'  "name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change name'

    @staticmethod
    def aleatory_first_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "first_name":'):
                new_line = line.replace(line,
                                          f'  "first_name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change first_name'

    @staticmethod
    def aleatory_last_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "last_name":'):
                new_line = line.replace(line,
                                        f'  "last_name": "{namegenerator.gen().split("-")[1]}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change last_name'

    @staticmethod
    def aleatory_roles(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "roles":'):
                roles = ['administrator', 'subscriber']
                new_line = line.replace(line,
                                          f'  "roles": "{random.choice(roles)}"')
                print(new_line)
            else:
                print(line, end='')
        return 'change role'


class Comment_Data:

    @staticmethod
    def aleatory_author_email(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "author_email":'):
                number_email = random.randint(1, 999)
                new_line = line.replace(line,
                                        f'  "author_email": "{namegenerator.gen()}{number_email}@gmail.com",')
                print(new_line)
            else:
                print(line, end='')
        return 'change author_email'

    @staticmethod
    def aleatory_author_name(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "author_name":'):
                new_line = line.replace(line,
                                        f'  "author_name": "{namegenerator.gen().split("-")[2]}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change author_name'

    @staticmethod
    def aleatory_content(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "content":'):
                new_line = line.replace(line,
                                        f'  "content": "{namegenerator.gen()}",')
                print(new_line)
            else:
                print(line, end='')
        return 'change content'

    @staticmethod
    def aleatory_status(load):
        for line in fileinput.FileInput(f"./testdata/{load}", inplace=1):
            if line.startswith(f'  "status":'):
                status = ['approved', 'hold', 'spam', 'trash']
                new_line = line.replace(line,
                                        f'  "status": "{random.choice(status)}"')
                print(new_line)
            else:
                print(line, end='')
        return 'change status'
