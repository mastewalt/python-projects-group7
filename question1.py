# 1. Menu dictionary
menu = {
    1: {"name": "Chips", "price": 4.50},
    2: {"name": "Soda", "price": 3.00},
    3: {"name": "Candy Bar", "price": 2.25},
    4: {"name": "Bottled Water", "price": 2.00}
}

order_list = []
total_cost = 0.0


# 2. Display the menu
def displayMenu(lst):
    print("Welcome to the Snack Bar!")
    print("Here is our menu:")
    print("--------------------------------")
    print("Item No. | Item Name     | Price")
    print("--------------------------------")

    for item_num, item_info in lst.items():
        print(f"{item_num:<8} | {item_info['name']:<13} | ${item_info['price']:.2f}")

    print("--------------------------------")

displayMenu(menu)

# 3. Ordering loop
while True:
    

    choice = input("Enter the item number to add to your order, or type 'done' to finish: ").strip().lower()

    if choice == "done":
        break

    elif choice.isdigit() and int(choice) in menu:

        selected_item = menu[int(choice)]
        order_list.append(selected_item)

        total_cost += selected_item["price"]

        print(f"Added {selected_item['name']} to your order. Current total: ${total_cost:.2f}")

    else:
        print("Invalid item number. Please try again or type 'done' to finish")


# 4. Print receipt
print("\n--------------------------------")
print("--------- YOUR RECEIPT ---------")
print("--------------------------------")

for item in order_list:
    print(f"{item['name']:<18} ${item['price']:.2f}")

print("--------------------------------")
print(f"Total Cost:         ${total_cost:.2f}")
print("--------------------------------")
print("Thank you for your purchase!")
