import requests
import json
import threading
import random
import string

use_default_url = "no"

while True:

    use_default_url = input("Default url? (yes/no)")

    if use_default_url.lower() == 'yes':
        url = "https://10e2e771-9e34-46b0-808b-25ed04bf8973.mock.pstmn.io/getpy"
    else:
        url = input("Enter the URL you want to send a GET request to: ")

    num_requests = int(input("Enter the number of requests you want to send: "))
    num_threads = int(input("Enter the number of threads you want to use: "))

    def send_request(idx):
        data = 'apple' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        payload = {"data": data}
        headers = {}

        response = requests.request("GET", url, headers=headers, params=payload)
        with open('responses.txt', 'a') as file:
            file.write(str(response.json()))
        print(f"Request {idx} status: {response.status_code} {data}")
        return response.json()

    threads = []
    for i in range(num_requests):
        thread = threading.Thread(target=send_request, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    repeat = input("Do you want to run the program again? (y/n) ")
    if repeat.lower() != 'y':
        break