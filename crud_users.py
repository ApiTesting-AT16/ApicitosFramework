from utils.requestresponse import APIresponses
import allure


class CrudUser:

    @allure.step('request get user')
    def get_user(self, url_base, token, orderby, page, per_page):
        url = f'{url_base}/wp-json/wp/v2/users?orderby={orderby}&page={page}&per_page={per_page}'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request post user')
    def create_user(self, url_base, token, input_data):
        url = f'{url_base}/wp-json/wp/v2/users'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(url, payload, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request delete user')
    def delete_user(self, url_base, token, id_post, query_param):
        url = f'{url_base}/wp-json/wp/v2/users/{id_post}{query_param}'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request put user')
    def update_user(self, url_base, token, input_data, id_post):
        new_url = f'{url_base}/wp-json/wp/v2/users/{id_post}'
        allure.attach(str(new_url), 'URL', allure.attachment_type.TEXT)
        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response
