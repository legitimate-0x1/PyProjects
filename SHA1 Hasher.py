# Made by Sovf!

import hashlib

print("Welcome to SHA1 Hasher!\n")

while True:
    print("SHA1 Hashed:", hashlib.sha1(input("String: ").encode()).hexdigest(), "\n")
