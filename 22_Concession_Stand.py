# CONCESSION STAND PROGRAM:-

menu = {
    "popcorn" :  1.00,
    "hot dog" :  2.00,
    "Pretzel" :  2.00,
    "Asst candy" :  1.00,
    "Soda" :  1.00,
    "Bottled Water" :  1.00 
}

cart = []
total = 0

print("---------------- MENU ----------------")
for key, value in menu.items():
    print(f"{key:10} : ${value}")
print("---------------- MENU ----------------")

while True:
    food = input("Select an item ( q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------- YOUR ORDER ----------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(total)

