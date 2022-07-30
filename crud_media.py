from dotenv import load_dotenv
import os
load_dotenv()
FOLDER = os.getenv('FOLDERFILE')

from utils.requestresponse import APIresponses


class CrudMedia:

    def get_media(self, base_url, token):

        url = f'{base_url}/wp-json/wp/v2/media'

        headers = {"Authorization": token}
        response = APIresponses().get(url, headers)

        return response

    def create_media(self, base_url, token, input_data, cont):
        for i in range(1, cont):

            url = f'{base_url}/wp-json/wp/v2/media'
            print("holaaa ", input_data[i]['imagen'])
            files = [
                ('file', (input_data[i]['imagen'], open('C:/Users/luzma/Pictures/Demo/'+input_data[i]['imagen'], 'rb')))
            ]
            payload = input_data[0]
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
        files = [
            ('file', ('OCRpract.jpg', open('/C:/Users/luzma/Pictures/Demo/OCRpract.jpg', 'rb'), 'image/jpeg'))
        ]
        payload = input_data
        headers = {"Authorization": token}
        response = APIresponses().post_file(new_url, headers, payload, files)

        return response

    def create_media(self, base_url, token, input_data, file):

        url = f'{base_url}/wp-json/wp/v2/media'

        payload = input_data
        files = [('file', (f'{file}', open(f'{FOLDER}{file}', 'rb')))]
        headers = {"Authorization": token}
        response = APIresponses().post_file(url, payload, headers, files)
        return response


