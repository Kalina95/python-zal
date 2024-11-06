import json

import requests
from requests import Response


class HttpService:
    def __init__(self):
        self.base_url = ""
        self.endpoint = ""

    def get(self) -> json:
        url = f"{self.base_url}/{self.endpoint}"
        response: Response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
