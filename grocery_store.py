"""2) Write a program that:
• Has a predefined dictionary of groceries with prices.
• Lets the user "add" items by typing their names.
• For each valid item, asks for the quantity.
• Keeps adding to the cart until the user types "checkout".
• Displays a final bill: each item, quantity, subtotal, and total."""

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
    
    paper_bags = {}

    print("Welcome to the store! (Type 'checkout' to finish)")
    print(f"Available items: {', '.join(inventory.keys())}")

    while True:
        # 2. Let the user "add" items
        item = input("\nEnter item name: ").strip().lower()
        
        if item == "checkout":
            break
        
        elif item in inventory:
            # 3. Ask for the quantity
             if item in inventory:
                   # 3. Ask for quantity and validate using isalnum()
                  qty = input(f"Enter quantity for {item}: ")
                # Use isalnum() to ensure the string is only numbers
                # (Note: does not handle decimals, only integers)

                  if qty.isalnum() and int(qty) > 0:
                      quantity = int(qty)
                      # Add to paper_bags or update existing
                      paper_bags[item] = paper_bags.get(item, 0) + quantity
                      print(f"Added {quantity} {item}(s) to paper_bags.")
             else:
                      print("Invalid quantity. Please enter a positive number.")
        else:
            print("Item not found in inventory. Please try again.")

    # 5. Display final bill
    print("\n--- Final Bill ---")
    total = 0
    print(f"{'Item':<10} | {'Qty':<5} | {'Subtotal':<10}")
    print("=" * 30)
    
    for item, quantity in paper_bags.items():
        price = inventory[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item.capitalize():<10} | {quantity:<5} | ${subtotal:.2f}")
        
    print("-" * 30)
    print(f"Total: ${total:.2f}")

grocery_store()
