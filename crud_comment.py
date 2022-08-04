from utils.requestresponse import APIresponses


class CrudComment:

    def get_comment(self, base_url, token, orderby, page, per_page):

        url = f'{base_url}/wp-json/wp/v2/comments?orderby={orderby}&page={page}&per_page={per_page}'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    def get_comment_by_id(self, base_url, token, id_post):

        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    def create_comment(self, base_url, token, input_data):

        url = f'{base_url}/wp-json/wp/v2/comments'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(url, payload, headers)

        return response

    def delete_comment(self, base_url, token, id_post):

        url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)

        return response

    def update_comment(self, base_url, token, input_data, id_post):

        new_url = f'{base_url}/wp-json/wp/v2/comments/{id_post}'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)

        return response
