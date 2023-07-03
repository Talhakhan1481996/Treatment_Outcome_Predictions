import unittest
import requests
from unittest.mock import Mock
from extract import get_api_data

class TestGetApiData(unittest.TestCase):
    def test_get_api_data(self):
        # Mock the requests.get function
        requests.get = Mock()

        # Define the mock response object
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.status_code = 200

        # Set the mock response for requests.get
        requests.get.return_value = mock_response

        # Call the function to be tested
        result = get_api_data("https://xloop-dummy.herokuapp.com")

        # Assertions
        requests.get.assert_called_once_with("https://xloop-dummy.herokuapp.com")
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(result, {"key": "value"})

if __name__ == '__main__':
    unittest.main()
