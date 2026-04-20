"""
Module: Inventory Manager Pro
Purpose: A CLI system to manage stock levels using CSV persistence.
Logic: Features data validation, automated file creation, and a restock
       alert system for low-inventory items.
Standard: Seriously_Codical
"""

import csv

file_path = "../../../assets/inventory.csv"

def load_from_csv():
    """
    Retrieves data from the CSV file. If the file is missing, the 'pass'
    ensures the program starts with an empty list instead of crashing.
    """
    inventory = []
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Ensure the quantity is treated as an integer for math logic
                item = row[0]
                qty = int(row[1])
                inventory.append([item, qty])
    except FileNotFoundError:
        pass
    return inventory

def save_to_csv(inventory):
    """Overwrites the CSV with the current list state."""
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in inventory:
            writer.writerow(row)

def select_option():
    print("== INVENTORY MANAGER ==")
    print("1. See inventory")
    print("2. Update stock")
    print("3. New item")
    print("4. Check if <3 units")
    print("5. Quit")

def validate_user_option():
    try:
        user_option = input("Option(1-5): ")
        if not user_option.isdigit():
            raise ValueError
        else:
            return user_option
    except ValueError:
        print("Invalid value")
    except Exception as e:
        print(f"Error: {e}")

def see_inventory():
    print("============================")
    print("====== INVENTORY ======")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Formatting: capitalizes item and aligns columns for readability
                print(f"{row[0].capitalize():<15} : {row[1]}")
    except FileNotFoundError:
        print("File not found")
    print("============================")

def update_stock(inventory):
    user_item = input("Item: ").strip().lower()
    # Guard against duplicate entries to maintain data integrity
    for item in inventory:
        if item[0] == user_item:
            try:
                user_quantity = int(input("New Qty: "))

                if user_quantity < 0:
                    print("Qty can't be negative")
                else:
                    item[1] = user_quantity
                    save_to_csv(inventory)
                    print("Updated successfully!")
                return
            except ValueError:
                print("Invalid input: Please enter a number.")
                return
    else:
        print("Item not in inventor.")

def new_item(inventory):
    user_new_item = input("New Item: ").strip().lower()
    for item in inventory:
        if item[0] == user_new_item:
            print("Item already in inventory")
            return
    try:
        user_new_qty = int(input("Qty: "))
        if user_new_qty < 0:
            print("Qty can't be negative")
        else:
            inventory.append([user_new_item, user_new_qty])
            save_to_csv(inventory)
            print("Added to records!")
    except ValueError:
        print("Invalid input: Quantity must be a number.")

def check_3_units(inventory):
    print("=============================")
    print("RESTOCK ALERTS (Below 3 units)")
    for item in inventory:
        if item[1] < 3:
            print(f"{item[0]} : {item[1]}")
            found = True
    if not found:
        print("All stock levels are healthy!")
    print("=============================")

# --- Execution Logic ---
inventory = load_from_csv()

# Default data injection for first-time users
if not inventory:
    inventory = [["apples", 10],
                 ["bananas", 2],
                 ["mangoes", 15],
                 ["peaches", 1],
                 ["pomegranates", 9]]
    save_to_csv(inventory)


select_option()

while True:
    selected_option = validate_user_option()

    if selected_option is None:
        continue

    if selected_option == "1":
        see_inventory()

    elif selected_option == "2":
        update_stock(inventory)

    elif selected_option == "3":
        new_item(inventory)

    elif selected_option == "4":
        check_3_units(inventory)

    elif selected_option == "5":
        print("Closing manager...")
        break