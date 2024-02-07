import requests

def get_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    if response.status_code == 200:
        return response.json()
    else:
        return False
    