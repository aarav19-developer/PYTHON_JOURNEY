# MEMBERSHIP OPERATORS :-
                      #  used to test whether a value or variable is found in a sequence (string,list, tuple, set or dictionary).
                    # 1. in
                    # 2. not in 

word = "Apple"

letter = input("Guess a letter in the secret word: ").capitalize()

if letter in word:
    print(letter)
else:
    print("not found")

if letter not in word:
    print("not found")
else:
    print(letter)

# -----------------NXT ONE-----------------#

