from utils.requestresponse import APIresponses
import allure


class CrudComment:
    @allure.step('Get Comments')
    def get_comment(self, base_url, token, orderby, page, per_page):

        url = f'{base_url}/wp-json/wp/v2/comments?orderby={orderby}&page={page}&per_page={per_page}'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    @allure.step('Get Comments by ID')
    def get_comment_by_id(self, base_url, token, id_post):

        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    @allure.step('Create Comments')
    def create_comment(self, base_url, token, input_data):

        url = f'{base_url}/wp-json/wp/v2/comments'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(url, payload, headers)

        return response

    @allure.step('Delete Comment')
    def delete_comment(self, base_url, token, id_post):

        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)

        return response

    @allure.step('Update Comment')
    def update_comment(self, base_url, token, input_data, id_post):

        new_url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)

        return response
