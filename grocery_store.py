""""
2)	Write a program that:
•	Has a predefined dictionary of groceries with prices.
•	Lets the user "add" items by typing their names.
•	For each valid item, asks for the quantity.
•	Keeps adding to the cart until the user types "checkout".
•	Displays a final bill: each item, quantity, subtotal, and total."""
#This program or project is just to show a simple grocery items billing system in python
# it use a predefined dictionary to store availabe grocery and the price.

def grocery_store():
    # 1. Predefined dictionary of groceries with prices
    inventory = {
        "juice": 2.00,
        "rice": 5.00,
        "apple": 0.50,
        "banana": 0.25,
        "milk": 3.00,
        "bread": 2.50,
        "eggs": 4.00
    }
    
    bag = {}

    print("Welcome to the store! (Type 'checkout' to finish)")
    print(f"Available items: {', '.join(inventory.keys())}")

    while True:
        # 2. Let the user "add" items
        item = input("\nEnter item name: ").lower()
        
        if item == "checkout":
            break
        
        elif item in inventory:
            # 3. Ask for the quantity
            try:               #The try block lets you test a block of code for errors.
                quantity = int(input(f"How many {item}s? "))
                if quantity > 0:
                    bag[item] = bag.get(item, 0) + quantity
                    print(f"Added {quantity} {item}(s).")
                else:
                    print("Please enter a positive quantity?.")
            except ValueError:
                print("Invalid quantity. Please enter a number?.")

        #The except block lets you handle the error.

        else:
            print("Item not in inventory.")

    # 5. Display final bill
    print("\n--- Final Bill ---")
    total = 0
    print(f"{'Item':<10} | {'Qty':<5} | {'Subtotal':<10}")
    print("-" * 30)
    
    for item, quantity in bag.items():
        price = inventory[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item.capitalize():<10} | {quantity:<5} | ${subtotal:.2f}")
        
    print("-" * 30)
    print(f"Total: ${total:.2f}")

grocery_store()