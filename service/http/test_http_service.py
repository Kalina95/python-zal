import unittest
from unittest.mock import patch, Mock
from requests import Response
from service.http.http_service import HttpService

class TestHttpService(unittest.TestCase):

    @patch('requests.get')
    def test_get_success(self, mock_get):
        #given
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        service = HttpService(base_url="https://api.example.com", endpoint="test")

        #when
        result = service.get()

        #then
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/test")

    @patch('requests.get')
    def test_get_failure(self, mock_get):
        #given
        mock_response = Mock(spec=Response)
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        service = HttpService(base_url="https://api.example.com", endpoint="test")

        #when
        call_get = lambda : service.get()

        #then
        with self.assertRaises(Exception):
            call_get()

    @patch('requests.get')
    def test_get_with_invalid_url(self, mock_get):
        #given
        mock_response = Mock(spec=Response)
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        service = HttpService(base_url="https://api.example.com", endpoint="invalid")

        #when
        call_get = lambda : service.get()

        with self.assertRaises(Exception):
            call_get()