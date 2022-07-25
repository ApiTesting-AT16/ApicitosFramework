from utils.requestresponse import APIresponses


class CrudComment:

    def get_commet(self, URL, token):
        url = f'{URL}/wp-json/wp/v2/comments'
        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)
        return response

    def create_comment(self, URL, token, post, author_name, author_email, content, status):
        url = f'{URL}/wp-json/wp/v2/comments'
        payload = {'post': post,
                   'author_name': author_name,
                   'author_email': author_email,
                   'content': content,
                   'status': status}

        headers = { "Authorization": token }

        response = APIresponses().post(url, payload, headers)
        return response

    def delete_comment(self, URL, token, id_post):
        url = f'{URL}/wp-json/wp/v2/comments/{id_post}'

        headers = { "Authorization": token }

        response = APIresponses().delete(url, headers)

        return response

    def update_comment(self, URL, token, post, author_name, author_email, content, status, id_post):
        new_url = f'{URL}/wp-json/wp/v2/comments/{id_post}'

        payload = {'post': post,
                   'author_name': author_name,
                   'author_email': author_email,
                   'content': content,
                   'status': status}

        headers = {"Authorization": token}

        response = APIresponses().post(new_url, payload, headers)
        return response
