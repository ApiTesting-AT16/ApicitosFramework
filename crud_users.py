from utils.requestresponse import APIresponses


class CrudUser:

    def get_user(self, url_base, token):

        url = f'{url_base}/wp-json/wp/v2/users'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    def create_user(self, url_base, token, input_data):

        url = f'{url_base}/wp-json/wp/v2/users'

        payload = input_data
        headers = { "Authorization": token }
        response = APIresponses().post(url, payload, headers)

        return response

    def delete_user(self, url_base, token, id_post):

        url = f'{url_base}/wp-json/wp/v2/users/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)

        return response

    def update_user(self, url_base, token, input_data, id_post):

        new_url = f'{url_base}/wp-json/wp/v2/users/{id_post}'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)

        return response
