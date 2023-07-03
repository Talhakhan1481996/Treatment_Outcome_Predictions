import unittest, uvicorn
from unittest import mock
from fastapi.testclient import TestClient
from matching import matching_councillors

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


if __name__ == "__main__":
    unittest.main()
