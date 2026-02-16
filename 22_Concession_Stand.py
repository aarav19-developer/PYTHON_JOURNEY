# CONCESSION STAND PROGRAM:-

menu = {
    "popcorn" :  1.00,
    "hot dog" :  2.00,
    "pretzel" :  2.00,
    "asst candy" :  1.00,
    "soda" :  1.00,
    "bottled Water" :  1.00 
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
    elif food in menu:
        cart.append(food)
    else:
        print("Item not found")

print("\n---------------- YOUR ORDER ----------------")
for food in cart:
    total += menu[food]
    print(food, end=" ")

print()
print(total)

