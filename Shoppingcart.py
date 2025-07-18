Foods = []
prices = []
total = 0 


while True: 
    food = input("Enter a food you want to buy (Exit = X): ")
    if food.upper() == "X":
        break
    else :
        price = float(input(f"Enter the Price of the {food}: "))
        Foods.append(food)
        prices.append(price)

print ("\nYou have bought the following foods:")
for i in range(len(Foods)):
    print (f"{i+1}. {Foods[i]}")
    print (f"\nYou have spent a total of: ${sum(prices)}\n")
