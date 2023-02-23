import random
import string
import hashlib

while True:
    def algorithm():
        print("Baking cookie and putting it in the oven...")
        unhashed_cookie = 'c' + ''.join(random.choices(string.ascii_letters + string.digits, k=31))
        hash_object = hashlib.sha256(unhashed_cookie.encode())
        hashedcookie_str = hash_object.hexdigest()
        hashed_cookie = hashedcookie_str
        print("Cookie finished baking!")
        return hashed_cookie

    def getcookie(hashed_cookie):
        print("Your cookie is", hashed_cookie)

    hashed_cookie = algorithm()
    getcookie(hashed_cookie)

    input("Press enter to run the program again, otherwise close the window.\n")
