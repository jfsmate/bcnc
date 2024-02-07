import requests
import unittest
import json
from api.api import get_albums

step2 = False

class TestJsonPlaceholderAPI(unittest.TestCase):
    def setUp(self):

        self.api_url = "https://jsonplaceholder.typicode.com/albums"

        with open("config/fixture.json", "r") as file:
            self.albums = json.load(file)
        
        self.client_credentials_token_url = "https://example.com/token"
        self.client_id = "your_client_id"
        self.client_secret = "your_client_secret"
        
        self.authorization_code_token_url = "https://example.com/token"
        self.authorization_code_redirect_uri = "https://example.com/callback"
        self.authorization_code_client_id = "your_client_id"
        self.authorization_code_client_secret = "your_client_secret"
        self.authorization_code_code = "your_authorization_code"
        
    # Point 1
    def test_albums_data(self):

        data = get_albums()
                

        self.assertTrue(data != False, "No API data fetched")

        for i in range(min(5, len(data))):
            expected_title = f"{self.albums[i]['title']}"
            self.assertEqual(data[i]["title"], expected_title, f"Element error {i + 1}")

    
    #Point 2
    @unittest.skip("Se salta este text por las faltas de credenciales")
    def get_access_token_client_credentials(self):

        token_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.client_credentials_token_url, data=token_data)
        return response.json().get("access_token")

    @unittest.skip("Se salta este text por las faltas de credenciales")
    def get_access_token_authorization_code(self):
    
        token_data = {
            "grant_type": "authorization_code",
            "client_id": self.authorization_code_client_id,
            "client_secret": self.authorization_code_client_secret,
            "redirect_uri": self.authorization_code_redirect_uri,
            "code": self.authorization_code_code
        }
        response = requests.post(self.authorization_code_token_url, data=token_data)
        return response.json().get("access_token")

    @unittest.skip("Se salta este text por las faltas de credenciales")
    def test_albums_client_credentials(self):
        
        access_token = self.get_access_token_client_credentials()

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(self.api_url, headers=headers)

        self.assertEqual(response.status_code, 200, "API request fails with client credentials granted")

        data = response.json()

        self.assertTrue(len(data) > 0, "No API data fetched")

        for i in range(min(5, len(data))):
            expected_title = f"{self.albums[i]['title']}"
            self.assertEqual(data[i]["title"], expected_title, f"Element error {i + 1}")

    @unittest.skip("Se salta este text por las faltas de credenciales")
    def test_albums_data_authorization_code(self):

        access_token = self.get_access_token_authorization_code()

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(self.api_url, headers=headers)

        self.assertEqual(response.status_code, 200, "API request failed with authorization grant")

        data = response.json()

        self.assertTrue(len(data) > 0, "No API data fetched")

        for i in range(min(5, len(data))):
            expected_title = f"{self.albums[i]['title']}"
            self.assertEqual(data[i]["title"], expected_title, f"Element error {i + 1}")

if __name__ == '__main__':
    unittest.main()