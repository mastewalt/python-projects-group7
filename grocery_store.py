"""2) Write a program that:
• Has a predefined dictionary of groceries with prices.
• Lets the user "add" items by typing their names.
• For each valid item, asks for the quantity.
• Keeps adding to the cart until the user types "checkout".
• Displays a final bill: each item, quantity, subtotal, and total."""

def grocery_store():
    inventory = {
        "rice": 4.50,
        "potato": 3.75,

        
        "apple": 0.99,
        "banana": 0.50,
        "milk": 3.50,
        "bread": 2.50,
        "eggs": 4.00
    }

    paper_bags = {}
    print("Welcome to Grocery Store!")
    print("Available items:", ", ".join(inventory.keys()))
    print("Type 'checkout' to finish.")

    while True:
        item = input("\nEnter item name: ").strip().lower()

        if item == "checkout":
            break

        if item in inventory:
            qty_input = input(f"Enter quantity for {item}: ")

            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
                paper_bags[item] = paper_bags.get(item, 0) + quantity
                print(f"Added {quantity} {item}(s) to cart.")
            else:
                print("Invalid quantity. Please enter a whole number greater than 0.")
        else:
            print("Item not found. Please choose from the list above.")

    if not paper_bags:
        print("\nYour cart is empty. Have a nice day!")
        return

    print("\n" + "="*35)
    print("        FINAL RECEIPT")
    print("="*35)
    print(f"{'Item':<10} | {'Qty':<3} | {'Price':<6} | {'Subtotal'}")
    print("-" * 35)

    total = 0
    for item, quantity in paper_bags.items():
        price = inventory[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item.capitalize():<10} | {quantity:<3} | ${price:<5.2f} | ${subtotal:.2f}")

    print("-" * 35)
    print(f"{'TOTAL:':<23} | ${total:.2f}")
    print("="*35)

grocery_store()