import requests
import unittest

class TestJsonPlaceholderAPI(unittest.TestCase):
    def setUp(self):

        self.api_url = "https://jsonplaceholder.typicode.com/albums"
        self.albums = [{
                "userId": 1,
                "id": 1,
                "title": "quidem molestiae enim"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "sunt qui excepturi placeat culpa"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "omnis laborum odio"
            },
            {
                "userId": 1,
                "id": 4,
                "title": "non esse culpa molestiae omnis sed optio"
            },
            {
                "userId": 1,
                "id": 5,
                "title": "eaque aut omnis a"
            },]
        
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

        response = requests.get(self.api_url)
        
        self.assertEqual(response.status_code, 200, "Error request API")
        
        data = response.json()

        self.assertTrue(len(data) > 0, "No API data fetched")

        for i in range(min(5, len(data))):
            expected_title = f"{self.albums[i]['title']}"
            self.assertEqual(data[i]["title"], expected_title, f"Element error {i + 1}")

    # Point 2
    def get_access_token_client_credentials(self):

        token_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.client_credentials_token_url, data=token_data)
        return response.json().get("access_token")

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

if __name__ == "__main__":
    unittest.main()