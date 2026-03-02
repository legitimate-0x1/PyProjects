# Made by Sovf!

import time

print("Welcome to Stopwatch!\n")

while True:
    T1 = time.time()
    Input = input("Type something to see elapsed time: ")
    print("Time elapsed: ", time.time() - T1, "\n")
