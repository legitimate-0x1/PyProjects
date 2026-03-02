# Made by Sovf!

import urllib.request

print("Welcome to Website Updown Checker!\n")

while True:
    URL = input("URL: ").replace("https://", "").replace("http://", "").replace("www.", "")
    URL = "https://" + URL

    try:
        with urllib.request.urlopen(URL) as Answ:
            print((Answ.status == 200 and "Alive!" or "Dead!") + "\n")
    except:
        print("Invalid URL or non HTTPS!\n")
