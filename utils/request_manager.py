from http import HTTPStatus
from json import JSONDecodeError
import os
import requests
from assertpy import assert_that
from utils.json_reader import JsonReader
from utils.custom_logger import CustomLogger

LOGGER = CustomLogger()


class RequestsManager:
    __instance = None

    def __init__(self, config_file=""):
        self.__config = JsonReader.get_json('/../configuration.json')
        __environment = JsonReader.get_json('/../environment.json')
        env_selected = self.__config.get("environment", "develop")
        self.__env_users = __environment.get(env_selected).get("users")
        self.headers = {"Authorization": __environment["headers"]}
        self.url = __environment.get(env_selected).get("api-url")
        self.key = self.__env_users.get("admin").get("key")
        self.token = self.__env_users.get("admin").get("token")
        self.response = None

    @staticmethod
    def get_instance():
        """ This method get a instance of the RequestsManager class.
        Returns:
            Request Manager -- return a instance of RequestsManager class.
        """
        if RequestsManager.__instance is None:
            RequestsManager.__instance = RequestsManager()
        return RequestsManager.__instance


    def send_request(self,http_method,endpoint_route, payload=None, **kwargs):
        """ Send request
        Parameters
        http_sethod:str
        HTTP Method
        endpoint route1str.
        Application's endpoint
        payload Dict,optional
            Requests'body,by default None
        Returns
        response
        ------------
        request response
        """
        LOGGER.logger().info(f"REQUEST:{http_method},to:{self.url}{endpoint_route}")
        self.response = requests.request(
            method=http_method,
            url=f"{self.url}{endpoint_route}",
            headers=self.headers,
            #params={"key": kwargs.get("key", self.key), "token": kwargs.get("token", self.token)},
            data=None if payload is None else payload
        )
        try:
            assert_that(self.response.status_code).is_equal_to(HTTPStatus.OK.value)
            LOGGER.logger().info(
                f"-->Status Code:\"{self.response.status_code}\"")
        except AssertionError as err:
            LOGGER.logger().error(f"-->{err}")
        try:
            return self.response.json(), self.response.status_code
        except JSONDecodeError:
            response_text = {"text": self.response.text}
            return response_text, self.response.status_code
