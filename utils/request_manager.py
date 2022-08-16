from http import HTTPStatus
from json import JSONDecodeError
import requests
from assertpy import assert_that
from utils.custom_logger import CustomLogger

LOGGER = CustomLogger(__name__)

class RequestsManager:
    def send_request(self, http_method, endpoint_route, payload=None, **kwargs):
        LOGGER.info(f"REQUEST:{http_method},to:{self.url}{endpoint_route}")
        self.response = requests.request(
            method=http_method,
            url=f"{self.url}{endpoint_route}",
            headers=self.headers,
            params={"key": kwargs.get("key", self.key), "token": kwargs.get("token", self.token)},
            data=None if payload is None else payload
        )
        try:
            assert_that(self.response.status_code).is_equal_to(HTTPStatus.OK.value)
            LOGGER.info(
                f"-->Status Code:\"{self.response.status_code}\"")
        except AssertionError as err:
            LOGGER.error(f"-->{err}")
        try:
            return self.response.json(), self.response.status_code
        except JSONDecodeError:
            response_text = {"text": self.response.text}
            return response_text, self.response.status_code
