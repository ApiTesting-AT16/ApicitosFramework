import requests
from dataclasses import dataclass


@dataclass
class Responses:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIresponses:

    def _format_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}
        headers = response.headers
        return Responses(status_code, text, as_dict, headers)

    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return self._format_responses(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self._format_responses(response)

    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=headers)
        return self._format_responses(response)

    def delete(self, url, headers):
        response = requests.delete(url, headers=headers)
        return self._format_responses(response)

