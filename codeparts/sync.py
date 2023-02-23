import requests

url = "https://b0d98d53-6454-42e1-aaaa-203122d6ef39.mock.pstmn.io"

hashcookie = input("Please enter your cookie (Hashed)\n")
key1 = input("Please enter your passphrase\n")

data = {
    "hashcookie": hashcookie,
    "key": key1
}


def sync():
    print("Syncing...")
    response = requests.post(url, data=data)
    print("Response status code:", response.status_code)
    print("Response content:", response.text)


sync()
