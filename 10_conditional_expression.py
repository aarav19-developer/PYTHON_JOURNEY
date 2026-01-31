# Conditional Expession:-  A one line shortcut for the if-else statement( ternary operator).
                         # Print or assign one of two values based on a condition.
                         # X if condition else Y.

# STRING METHODS:- 
# 1. .find() - used to find anything position index when it first times appeared.
# 2. .rfind() - used to find anything position index when it second times appeared.
# 3. .capitalize() - used to capitalized only first letter in the statement.
# 4. .upper() - used to capitalized all the letter in the statement.
# 5. .lower() - used to lower case all the letter in the statement.
# 6. .isdigit() - used to tell us if the string contains only digits or not & returns the answer in the form of True or False.
# 7. .isalpha() - used to tell us if the string contains only alphabets or not & returns the answer in the form of True or False.
# 8. .count() - used to find the counting of the specific value which we have to entered in the ().
# 9. .replace() - used to replace word (" old word", "new word").

# TASK:
# validate user input exercise.
# 1. username is no more than 12 characters.
# 2. username must not contains spaces.
# 3. username must not contain digits.

username= input("enter username: ")
if len(username) > 12:
    print(len(username),"error")
elif  not username.find(" ") == -1:
    print(" do not use space in the username")
elif username.isdigit():
    print("do not use digit in the username")
else:
    print(f"Welcome to the python {username}")