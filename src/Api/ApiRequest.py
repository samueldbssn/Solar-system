import json
import requests

import os
from dotenv import load_dotenv



class ApiRequest:

    def __init__(self, link):
        self.link = link
        load_dotenv()
        self.token = os.getenv("API_TOKEN")


    def request(self, params):
        """Send a request to an API using Bearer token authentication

        :param params: the parameters sent to the API
        :return: A hashmap with the results sent by the API
        """
        headers = {
            "Authorization": self.token
        }
        print(self.link, params, headers)
        return requests.get(self.link, params=params, headers=headers).json()
