menu = {'pizza': 300,
        'burger': 100,
        'salad': 120}

cart = []

total = 0

print("Menu:")
for key, value in menu.items():
    print(f'{key.capitalize()}: ${value:.2f}')

while True:
    choice = input('Enter the item you want to add to your cart (to exit enter X): ').lower()
    if choice == 'x':
        break
    elif choice in menu:
        while True:
            qty_input = input(f'Enter quantity for {choice.capitalize()}: ')
            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
                break
            else:
                print("Please enter a valid positive integer for quantity.")
        cart.append((choice, quantity))
    else:
        print("Item not in menu. Please enter a valid item.")

if not cart:
    print("Your cart is empty.")
else:
    print("\nItems in your cart:")
    for item, qty in cart:
        total += menu[item] * qty
        print(f'{item.capitalize()} x{qty} - ${menu[item] * qty:.2f}')
    print(f'\nTotal: ${total:.2f}')
