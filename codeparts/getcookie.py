import json
import random
import string
import hashlib
import platform
import uuid
import socket
import datetime

# Get the HWID
hwid = str(uuid.getnode())

# Get the IP address
ip = socket.gethostbyname(socket.gethostname())

while True:
    def algorithm():
        print("Baking cookie and putting it in the oven...")
        unhashed_cookie = 'c' + ''.join(random.choices(string.ascii_letters + string.digits, k=21))
        hash_object = hashlib.sha256(unhashed_cookie.encode())
        hashed_cookie = hash_object.hexdigest()
        print("Cookie finished baking!")
        return hashed_cookie, unhashed_cookie

    def getcookie(hashed_cookie, unhashed_cookie):
        with open('/workspaces/requestspammer/data/cookie.json', 'w') as f:
            f.write(json.dumps({'hashed_cookie': hashed_cookie}) + '\n' + json.dumps({'unhashed_cookie': unhashed_cookie}))
        print("Cookie saved to /workspaces/requestspammer/data/cookie.json")

    hashed_cookie, unhashed_cookie = algorithm()
    getcookie(hashed_cookie, unhashed_cookie)

    input("Press enter to run the program again, otherwise close the window.\n")
