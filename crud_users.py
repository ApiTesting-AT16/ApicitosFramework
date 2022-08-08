from utils.requestresponse import APIresponses
import allure

class CrudUser:

    @allure.step('Get User')
    def get_user(self, url_base, token, orderby, page, per_page):

        url = f'{url_base}/wp-json/wp/v2/users?orderby={orderby}&page={page}&per_page={per_page}'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    @allure.step('Create User')
    def create_user(self, url_base, token, input_data):

        url = f'{url_base}/wp-json/wp/v2/users'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(url, payload, headers)

        return response

    @allure.step('Delete User')
    def delete_user(self, url_base, token, id_post, query_param):

        url = f'{url_base}/wp-json/wp/v2/users/{id_post}{query_param}'

        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)

        return response

    @allure.step('Update User')
    def update_user(self, url_base, token, input_data, id_post):

        new_url = f'{url_base}/wp-json/wp/v2/users/{id_post}'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)

        return response
