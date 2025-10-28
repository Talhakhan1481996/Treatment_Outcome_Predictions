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

    # @patch("matching.get_report_category")
    # @patch("matching.get_redis_client")
    # def test_matching_councillors(
    #     self, mock_get_redis_client: Mock(), mock_get_report_category: Mock()
    # ) -> None:
    #     report_id = 123
    #     number_of_councillors = 5
    #     report_category = "Some Category"
    #     councillors_with_ratings = [
    #         json.dumps({"name": "John", "avr_rating": 4.5}),
    #         json.dumps({"name": "Jane", "avr_rating": 3.8}),
    #         json.dumps({"name": "Alice", "avr_rating": 4.2}),
    #         json.dumps({"name": "Bob", "avr_rating": 4.9}),
    #         json.dumps({"name": "Eve", "avr_rating": 4.0}),
    #     ]
    #     expected_top_councillors = [
    #         {"name": "John", "avr_rating": 4.5},
    #         {"name": "Jane", "avr_rating": 3.8},
    #         {"name": "Alice", "avr_rating": 4.2},
    #         {"name": "Bob", "avr_rating": 4.9},
    #         {"name": "Eve", "avr_rating": 4.0},
    #     ]
    #     mock_get_report_category.return_value = report_category
    #     mock_redis_client = Mock()
    #     mock_redis_client.get.return_value = json.dumps(councillors_with_ratings)
    #     mock_get_redis_client.return_value = mock_redis_client
        
    #     result = matching_councillors(report_id, number_of_councillors)
    #     mock_get_report_category.assert_called_once_with(report_id)
    #     mock_get_redis_client.assert_called_once_with()
    #     mock_redis_client.get.assert_called_once_with(report_category)
    #     self.assertEqual(result, expected_top_councillors)


if __name__ == '__main__':
    unittest.main()
