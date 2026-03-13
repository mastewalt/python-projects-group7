'''
2)  Write a program that:
•   Has a predefined dictionary of groceries with prices.
•   Lets the user "add" items by typing their names.
•   For each valid item, asks for the quantity.
•   Keeps adding to the cart until the user types "checkout".
•   Displays a final bill: each item, quantity, subtotal, and total.
'''


menu = {
        "Bottled Water": 2.00,
        "Soda": 3.00,
        "Potato": 4.00,
        "Rice": 5.00,
        "Broccoli": 6.00
    }

order_list = {}
total_cost = 0.0
print("Welcome to the Grocery store!")

# 2. Display the menu
def displayName(lst ):
    print("Here is our menu:")
    print("--------------------------------")
    print("Item No. | Item Name     | Price")
    print("--------------------------------")
    for key, val in lst.items():
        print(f"{key} | {val}")
    print("--------------------------------")


while True:
    displayName(menu)
    choice = input("Enter the name to add to your order, or type 'checkout' to finish: ").strip().title()

    if choice == 'Checkout':
        break
    if choice not in menu.keys():
        print("Invalid name. Please try again or type 'checkout' to finish")
        continue
    elif choice in menu.keys():
        quantity = int(input("Enter How many items you want to add :"))

        selected_item = choice
        order_list[choice] = order_list.get(choice, 0) + quantity
        total_cost += (menu[choice] * quantity)
        

# 4. Finally print a receipt
print("\n--------------------------------")
print("--------- YOUR RECEIPT ---------")
print("--------------------------------")
for key, val in order_list.items():
    print(f"{key} X {val} sub total ${val * menu[key]}")
print("--------------------------------")
print(f"Total Cost:         ${total_cost:.2f}")
print("--------------------------------")
print("Thank you for your purchase!") 
print("pick time for next time and let's try all")