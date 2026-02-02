# fruits = ["apple"," orange","banana","coconut"]
# vegetable = ["pea","tomato","carrot"]
# meats = ["chicken","fish","crabs"]

# groceries = [fruits,vegetable,meats]

# print(groceries[0]) # way to approach the first index 0 in groceries.
# print(groceries[0][1]) # way to approach the list element which is also in other list element.

groceries = [["apple","orange","banana","coconut"],
             ["pea","tomato","carrot"],
             ["chicken","fish","crabs"]]
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# TASK:
# Prepare 2D mobile phone dialer.

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()