# Made by Sovf!

import hashlib

print("Welcome to SHA224 Hasher!\n")

while True:
    print("SHA224 Hashed:", hashlib.sha224(input("String: ").encode()).hexdigest(), "\n")
