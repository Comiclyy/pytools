import requests

url = "http://localhost:3000/test"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status_code}")
