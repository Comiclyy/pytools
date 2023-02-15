import hashlib

# Prompt the user for input
user_input = input("Enter a string to hash: ")

# Hash the user's input using the SHA-256 algorithm
hash_object = hashlib.sha256(user_input.encode())

# Print the hash as a hexadecimal string and copy to clipboard
hash_str = hash_object.hexdigest()
print("Hash:", hash_str)
