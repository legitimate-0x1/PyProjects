# Made by Sovf!

print("Welcome to Letter by Letter!\n")

while True:
    Input = input("String: ")

    print("\n")

    for Index in range(1, len(Input) + 1):
        print(Input[:Index])

    print("\n")
