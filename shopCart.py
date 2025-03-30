
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food name(press x to exit): ")
    if food.lower() == "x":
        break
    else:
     price = float(input(f"Enter the price of {food}: $"))
    foods.append(food)
    prices.append(price)

    for food in foods:
        print(f"{food}: ${price}")
    total += price
    print(f"Total: ${total}")
    