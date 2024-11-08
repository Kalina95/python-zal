import json
from abc import ABC

import requests
from requests import Response

class HttpService(ABC):
    """
    An abstract HTTP service class for making GET requests to a specified endpoint.

    This class provides a base for HTTP communication, specifically for retrieving JSON data
    from a given API endpoint. It constructs the full URL from the provided base URL and endpoint,
    sends a GET request, and returns the response as JSON.
    """

    def __init__(self, base_url: str, endpoint: str) -> None:
        self.base_url: str = base_url
        self.endpoint: str = endpoint

    def get(self) -> json:
        url = f"{self.base_url}/{self.endpoint}"
        response: Response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
