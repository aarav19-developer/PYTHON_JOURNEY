import random

low = 1 
high = 100
options = ("rock","paper","scissors")
cards = ["1","2","3","4","5","6","7","8","9","J","K","A"]
# number = random.randint(low,high)
# number = random.random()  # will return floating point number between 0 and 1.
# number = random.choice(options)
# print(number)
random.shuffle(cards)
print(cards)