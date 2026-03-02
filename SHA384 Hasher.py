# Made by Sovf!

import hashlib

print("Welcome to SHA384 Hasher!\n")

while True:
    print("SHA384 Hashed:", hashlib.sha384(input("String: ").encode()).hexdigest(), "\n")
