import requests
import random
import string

url = 'https://httpbin.org/post'

username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
email = f"{''.join(random.choices(string.ascii_letters + string.digits, k=8))}@dispostable.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=15))

data = {
    'username': username,
    'email': email,
    'password': password
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Successfully signed up!')
else:
    print('Sign up failed with status code:', response.status_code)

with open('data/signupdata.txt', 'w') as f:
    f.write(f"website_url= {url}\n")
    f.write(f"request status= {response.status_code}\n")
    f.write(f"username= {username}\n")
    f.write(f"email= {email}\n")
    f.write(f"password= {password}\n")
