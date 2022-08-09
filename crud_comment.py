import allure
from utils.requestresponse import APIresponses


class CrudComment:

    @allure.step('request get comment')
    def get_comment(self, base_url, token, orderby, page, per_page):
        url = f'{base_url}/wp-json/wp/v2/comments?orderby={orderby}&page={page}&per_page={per_page}'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request get comment by id')
    def get_comment_by_id(self, base_url, token, id_post):
        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request post comment')
    def create_comment(self, base_url, token, input_data):
        url = f'{base_url}/wp-json/wp/v2/comments'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(url, payload, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request delete user')
    def delete_comment(self, base_url, token, id_post):
        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'
        allure.attach(str(url), 'URL', allure.attachment_type.TEXT)
        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response

    @allure.step('request put user')
    def update_comment(self, base_url, token, input_data, id_post):
        new_url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'
        allure.attach(str(new_url), 'URL', allure.attachment_type.TEXT)
        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)
        allure.attach(str(response.text), 'Result', allure.attachment_type.TEXT)
        return response
