# Made by Sovf!

import hashlib

print("Welcome to SHA512 Hasher!\n")

while True:
    print("SHA512 Hashed:", hashlib.sha512(input("String: ").encode()).hexdigest(), "\n")
