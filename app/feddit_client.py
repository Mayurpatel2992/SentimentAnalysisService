import requests

def fetch_comments(subfeddit):
    url = f"http://localhost:8080/api/v1/subfeddit/{subfeddit}/comments"
    response = requests.get(url)
    return response.json()[:25] if response.ok else []
