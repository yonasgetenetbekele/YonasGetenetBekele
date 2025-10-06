#This is the concession stand program in python
menu = {"pizza": 3.00,
        "natches": 4.50,
        "Popcorn": 6.00,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = [ ]
total = 0
print ("--------MENU---------")
for key, value in menu.items ():
    print (f"{key:10}: ${value:.2f}")
print ("----------------------------")

while True:
    food = input ("Select an item (q to quit): ").lower()
    if food == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total +=  menu.get(food)
    print (food, end=" ")

print ()
print (f'Total is: ${total:.2f}')

