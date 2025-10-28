import unittest, uvicorn
#from matching import matching_councillors
from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
#from fastapi import FastAPI
from main import app, get_councillors, get_specific_councillors

class TestCouncillors(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch("main.matching_councillors")
    def test_get_councillors(self, mock_matching_councillors):
        # Mock the matching_councillors function to return a sample result
        sample_result = [
            {"name": "John Doe", "avr_rating": 4.5},
            {"name": "Jane Smith", "avr_rating": 3.8},
        ]
        mock_matching_councillors.return_value = sample_result

        # Send a request to the endpoint
        response = self.client.get(f"/councillors/123/")

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.json(), sample_result)

        # Check if the matching_councillors function was called with the correct arguments
        mock_matching_councillors.assert_called_once_with(123)

    @patch("main.matching_councillors")
    def test_get_specific_councillors(self, mock_matching_councillors):
        # Mock the matching_councillors function to return a sample result
        sample_result = [
            {"name": "John Doe", "avr_rating": 4.5},
            {"name": "Jane Smith", "avr_rating": 3.8},
        ]
        mock_matching_councillors.return_value = sample_result

        # Send a request to the endpoint
        response = self.client.get(f"/councillors/123/2")

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.json(), sample_result)

        # Check if the matching_councillors function was called with the correct arguments
        mock_matching_councillors.assert_called_once_with(123,2)

if __name__ == "__main__":
    unittest.main()

# class TestCouncillorsAPI(unittest.TestCase):

#     @mock.patch("main.matching_councillors")
#     def test_get_councillors(self, mock_matching_councillors):
#         # Mock the matching_councillors function
#         mock_matching_councillors.return_value = [
#             {"councillor_id": 1, "name": "John Doe", "avr_rating": 4.5},
#             {"councillor_id": 2, "name": "Jane Smith", "avr_rating": 3.8}
#         ]
        
#         client = TestClient()
#         response = client.get("/councillors/12345/")
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), [
#             {"councillor_id": 1, "name": "John Doe", "avr_rating": 4.5},
#             {"councillor_id": 2, "name": "Jane Smith", "avr_rating": 3.8}
#         ])
#         mock_matching_councillors.assert_called_once_with(12345)

    # @mock.patch("main.matching_councillors")
    # def test_get_specific_councillors(self, mock_matching_councillors):
    #     # Mock the matching_councillors function
    #     mock_matching_councillors.return_value = [
    #         {"councillor_id": 1, "name": "John Doe", "avr_rating": 4.5},
    #         {"councillor_id": 2, "name": "Jane Smith", "avr_rating": 3.8}
    #     ]
        
    #     client = TestClient(app)
    #     response = client.get("/councillors/12345/10")
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), [
    #         {"councillor_id": 1, "name": "John Doe", "avr_rating": 4.5},
    #         {"councillor_id": 2, "name": "Jane Smith", "avr_rating": 3.8}
    #     ])
    #     mock_matching_councillors.assert_called_once_with(12345, 10)


# if __name__ == "__main__":
#     unittest.main()
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)