from utils.requestresponse import APIresponses


class CrudUser:

    def get_user(self, URL, token):
        url = f'{URL}/wp-json/wp/v2/users'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)
        return response

    def create_user(self, URL, token, username, name, email, password):
        url = f'{URL}/wp-json/wp/v2/users'
        payload = {'username': username,
                   'name': name,
                   'email': email,
                   'password': password}

        headers = { "Authorization": token }

        response = APIresponses().post(url, payload, headers)
        return response

    def delete_user(self, URL, token, id_post):
        url = f'{URL}/wp-json/wp/v2/users/{id_post}'

        headers = { "Authorization": token }

        response = APIresponses().delete(url, headers)
        return response

    def update_user(self, URL, token, name, email, password, id_post):
        print('hola reynel', URL)
        print('hola reynel 2 ', token)
        new_url = f'{URL}/wp-json/wp/v2/users/{id_post}'
        print('reynel 3 =: ', new_url)
        payload = {'name': name,
                   'email': email,
                   'password': password}

        headers = {"Authorization": token}

        response = APIresponses().post(new_url, payload, headers)
        return response
