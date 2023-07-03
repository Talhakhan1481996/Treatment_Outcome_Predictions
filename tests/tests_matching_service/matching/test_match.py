import requests, os, unittest, redis, json
from unittest.mock import Mock, patch
from matching import get_report_category, matching_councillors
from base_logger import logger
from redis_connector import get_redis_client

class TestFunctions(unittest.TestCase):
    def test_get_report_category(self):
        # Mock the requests.get function
        requests.get = Mock()

        # Define the mock response object
        mock_response = Mock()
        mock_response.json.return_value = {"category": "example_category"}
        mock_response.status_code = 200

        # Set the mock response for requests.get
        requests.get.return_value = mock_response

        # Call the function to be tested
        result = get_report_category(12345)

        # Assertions
        url = f"{os.getenv('BASE_URL')}/report/12345"
        requests.get.assert_called_once_with(url)
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(result, "example_category")

if __name__ == '__main__':
    unittest.main()
