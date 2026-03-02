# Made by Sovf!

import hashlib

print("Welcome to MD5 Hasher!\n")

while True:
    print("MD5 Hashed:", hashlib.md5(input("String: ").encode()).hexdigest(), "\n")
