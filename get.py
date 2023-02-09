import requests
import json
import threading

while True:
    use_default_url = input("Do you want to use the default URL (yes/no)? ")

    if use_default_url.lower() == 'yes':
        url = "https://10e2e771-9e34-46b0-808b-25ed04bf8973.mock.pstmn.io/getpy"
    else:
        url = input("Enter the URL you want to send a GET request to: ")

    num_requests = int(input("Enter the number of requests you want to send: "))
    num_threads = int(input("Enter the number of threads you want to use: "))

    def send_request():
        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(f"Request status: {response.status_code}")
        return response.json()

    def write_response_to_file(response_json):
        with open('getresponses.txt', 'a') as file:
            file.write(json.dumps(response_json))
            file.write('\n')

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=write_response_to_file, args=(send_request(),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    repeat = input("Do you want to run the program again? (y/n) ")
    if repeat.lower() != 'y':
        break