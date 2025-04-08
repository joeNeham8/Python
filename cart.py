#Consession stand program

menu = {
    "puttu": 45.50,
    "appam": 25.00,
    "idiyappam": 15.00,
    "porotta": 12.25,
    "beef roast": 120.45,
    "oothappam": 15.50,
    "dosa": 20.00,
    "masala dosa": 75.35,
    "avil milk": 40.80,
    "fresh lime": 35.00,
}

cart=[]
total = 0.0

print("--------------MENU---------------")
for key , value in menu.items():
    print(f"{key:20} {value:.2f}")
print("----------------------------------")
print("")

while True:
    food = input("Select an item(q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)
print("")
print("-------YOUR ORDER-------")

for food in cart:
    total += menu.get(food)
    print(food, end="\n")
    
print(" ")    
print(f"Toatl =  {total:.2f}")
