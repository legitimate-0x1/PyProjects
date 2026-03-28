# Made by Sovf!

from flask import Flask, request
import hashlib, base64

HashAlgorithms = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA256": hashlib.sha256,
    "SHA512": hashlib.sha512
}

HashAlgorithmNames = []

for Index, Value in enumerate(HashAlgorithms):
    HashAlgorithmNames.append(Value)

def Hash(Value, HashAlgorithm):
    Func = HashAlgorithms.get(HashAlgorithm.upper())
    if Func != None:
        return Func(base64.b64encode(Value.encode())).hexdigest()

    return ""

App = Flask(__name__)

@App.route("/")
def info():
    return {"Status": True, "Version": 1, "HashAlgorithms": HashAlgorithmNames}

@App.route("/hash")
def hashf():
    Value, HashAlgorithm = request.args.get("value"), request.args.get("hashalg")
    
    return {"Hash": Hash(Value, HashAlgorithm)}
    
if __name__ == "__main__":
    App.run(debug = True)
