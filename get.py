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

        if not url.startswith("https://"):
            url = "https://" + url
            
    num_requests = int(input("Enter the number of requests you want to send: "))
    num_threads = int(input("Enter the number of threads you want to use: "))

    use_random_data = input("Use random data? (yes/no)")
    if use_random_data.lower() == 'yes':
        data_length = int(input("Enter the number of characters for the random data: "))
    else:
        data = input("Enter the data you want to send: ")
    
    def send_request(idx):
        if use_random_data.lower() == 'yes':
            data = 'comicly' + ''.join(random.choices(string.ascii_letters + string.digits, k=data_length))
        else:
            data = data
        payload = {"data": data}
        headers = {}

        response = requests.request("GET", url, headers=headers, params=payload)
        try:
            response_json = response.json()
        except ValueError as e:
            response_json = {}
            print(f"Request {idx} error: {e}")

        print(f"Request {idx} status: {response.status_code} {data} sent to {url}")
        return response_json

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
