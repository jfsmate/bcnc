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
        
    def test_albums_data(self):

        response = requests.get(self.api_url)
        
        self.assertEqual(response.status_code, 200, "Error en la solicitud a la API")
        
        data = response.json()

        self.assertTrue(len(data) > 0, "No se obtuvieron datos de la API")

        for i in range(min(5, len(data))):
            expected_title = f"{self.albums[i]['title']}"
            self.assertEqual(data[i]["title"], expected_title, f"Error en el elemento {i + 1}")

if __name__ == "__main__":
    unittest.main()