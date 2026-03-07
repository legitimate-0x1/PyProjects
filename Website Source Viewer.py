# Made by Sovf!

import urllib.request

HTTPsURLTbl = ["http://", "https://", "www."]

def AddHTTPs(URL):
    URL = URL.lower()

    for Index in HTTPsURLTbl:
        URL = URL.replace(Index, "")

    URL = "https://" + URL

    return URL

def HttpGet(URL):
    try:
        return urllib.request.urlopen(AddHTTPs(URL)).read().decode("utf-8")
    except:
        return "An error occurred!"

while True:
    print("Website Source:", HttpGet(str(input("Website URL: "))), "\n")
