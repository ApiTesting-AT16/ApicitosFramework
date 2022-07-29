from utils.requestresponse import APIresponses
from dotenv import load_dotenv
import os
load_dotenv()
FOLDER = os.getenv('FOLDERFILE')

class CrudMedia:

    def get_media(self, base_url, token):

        url = f'{base_url}/wp-json/wp/v2/media'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    def create_media(self, base_url, token, input_data, file, type_file):

        url = f'{base_url}/wp-json/wp/v2/media'

        payload = input_data
        files = [
            ('file', (
            f'{file}', open(f'{FOLDER}{file}', 'rb'),
            f'{type_file}'))
        ]
        headers = {"Authorization": token}
        response = APIresponses().post_file(url, payload, headers, files)

        return response

    def delete_media(self, base_url, token, id_post):

        url = f'{base_url}/wp-json/wp/v2/media/{id_post}'

        headers = {"Authorization": token}
        response = APIresponses().delete(url, headers)

        return response

    def update_media(self, base_url, token, input_data, id_post):

        new_url = f'{base_url}/wp-json/wp/v2/media/{id_post}'

        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post(new_url, payload, headers)

        return response
