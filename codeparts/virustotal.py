import requests

url = "https://www.virustotal.com/api/v3/files"
filepath = input("Enter the file path: ")
files = {"file": (filepath, open(filepath, "rb"), "text/html")}
headers = {
    "accept": "application/json",
    "x-apikey": "30f62db894e2b021dd06e0c1eee1676803a58c9ffbd924759c28af9536472821"
}

response = requests.post(url, files=files, headers=headers)
json_response = response.json()

id = json_response["data"]["id"]
print("File analysis ID:", id)

url = f"https://www.virustotal.com/api/v3/analyses/{id}"
headers = {
    "accept": "application/json",
    "x-apikey": "30f62db894e2b021dd06e0c1eee1676803a58c9ffbd924759c28af9536472821"
}

response = requests.get(url, headers=headers)
response_content = response.content.decode("utf-8")

with open("responses/vtresponse.txt", "a") as f:
    f.write(f"id={id}\n\n")
    f.write(f"file={filepath}\n\n")
    f.write(response_content)
    f.write("\n\n")

print("Response saved to vtresponses.txt")
