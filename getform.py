import requests
import json
import threading
import random
import string
import os

use_default_url = "no"

while True:
    use_default_url = input("Default url? (yes/no)")

    if use_default_url.lower() == 'yes':
        url = "https://api.smooch.io/sdk/v2/apps/5f978e31e2edbd000c1a0224/conversations/50dce923c9b6a0ac78dc07d0/messages"
    else:
        url = input("Enter the URL you want to send a GET request to: ")

        if not url.startswith("https://"):
            url = "https://" + url

    num_requests = int(input("Enter the number of friends you want to send: "))
    num_threads = int(input("Enter the number of threads you want to use: "))

    use_random_data = input("Use random data? (yes/no)")
    if use_random_data.lower() == 'yes':
        data_length = int(input("Enter the number of characters for the random data: "))
        data = 'comicly' + ''.join(random.choices(string.ascii_letters + string.digits, k=data_length))
    else:
        use_text_file = input("Use text file? (y/n)")

        if use_text_file.lower() == 'y':
            path = input("What is the path to the text file you want to use? ")
            if os.path.isfile(path) and path.endswith('.txt'):
                with open(path, 'r') as file:
                    customdata = file.read()
            else:
                print("The file does not exist or is not a text file")
                repeat = input("Do you want to run the program again? (y/n) ")
                if repeat.lower() != 'y':
                    break
                else:
                    continue
        else:
            customdata = input("What data do you want to use? ")

    def send_request(idx):
        payload = {"data": customdata}
        headers = {}

        response = requests.request("GET", url, headers=headers, params=payload)

        try:
            response_json = response.json()
        except ValueError as e:
            response_json = {}
            print(f"Request {idx} error: {e}")

        print(f"Request {idx} status: {response.status_code} sent to {url}")
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
