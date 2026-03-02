# Made by Sovf!

import hashlib

HashAlgorithmsTbl = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "sha3_224": hashlib.sha3_224,
    "sha3_256": hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_512": hashlib.sha3_512,
}

HashAlgorithmInfo = ""

for Index in HashAlgorithmsTbl:
    HashAlgorithmVal = Index.upper()
    HashAlgorithmInfo += HashAlgorithmVal
    HashAlgorithmInfo += (Index == "sha3_512" and ".\n" or ", ")

print("Welcome to Hasher! Type 'help' as Hash Algorithm to see hashing algorithms.\n")

while True:
    HashAlgorithm = input("Hash Algorithm: ").lower()

    if HashAlgorithm == "help":
        print(HashAlgorithmInfo)
    else:
        Input = input("String: ").encode()

        print(HashAlgorithm.upper(), "Hashed:", HashAlgorithmsTbl[HashAlgorithm](Input).hexdigest(), "\n")
