# Made by Sovf!

import hashlib

print("Welcome to SHA256 Hasher!\n")

while True:
    print("SHA256 Hashed:", hashlib.sha256(input("String: ").encode()).hexdigest(), "\n")
