while True:

    string = input("Enter your sentence - ").lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set()

    for i in string:
        if i.isalpha():
            letters.add(i)

    missing = alphabet - letters

    if len(missing) == 0:
        print("This is a Pangram :) ")
    else:
        print("This is not a Pangram :(")