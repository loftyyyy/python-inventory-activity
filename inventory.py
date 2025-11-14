"""
Inventory Management Program
Stores item names in a list and prices in a dictionary.
Allows adding items and updating prices.
"""

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Item")
    print("2. Update Item Price")
    print("3. View All Items")
    print("4. Exit")
    print("="*40)

def add_item(item_names, item_prices):
    """
    Add a new item to the inventory.
    Prevents duplicate items.
    """
    item_name = input("Enter item name: ").strip()
    
    # Check for duplicates
    if item_name in item_names:
        print(f"Error: '{item_name}' already exists in inventory!")
        return
    
    # Get price with validation
    try:
        price = float(input("Enter item price: $"))
        if price < 0:
            print("Error: Price cannot be negative!")
            return
    except ValueError:
        print("Error: Invalid price format!")
        return
    
    # Add to inventory
    item_names.append(item_name)
    item_prices[item_name] = price
    print(f"Success: '{item_name}' added with price ${price:.2f}")

def update_price(item_names, item_prices):
    """
    Update the price of an existing item.
    Shows error if item doesn't exist.
    """
    item_name = input("Enter item name to update: ").strip()
    
    # Check if item exists
    if item_name not in item_names:
        print(f"Error: '{item_name}' does not exist in inventory!")
        return
    
    # Get new price with validation
    try:
        new_price = float(input("Enter new price: $"))
        if new_price < 0:
            print("Error: Price cannot be negative!")
            return
    except ValueError:
        print("Error: Invalid price format!")
        return
    
    # Update price
    old_price = item_prices[item_name]
    item_prices[item_name] = new_price
    print(f"Success: '{item_name}' price updated from ${old_price:.2f} to ${new_price:.2f}")

def view_items(item_names, item_prices):
    """Display all items in the inventory."""
    if not item_names:
        print("\nInventory is empty!")
        return
    
    print("\n" + "="*40)
    print("   CURRENT INVENTORY")
    print("="*40)
    print(f"{'Item Name':<25} {'Price':>10}")
    print("-"*40)
    for item in item_names:
        print(f"{item:<25} ${item_prices[item]:>9.2f}")
    print("="*40)
    print(f"Total Items: {len(item_names)}")

def main():
    """Main function to run the inventory management program."""
    # Initialize inventory storage
    item_names = []  # List to store item names
    item_prices = {}  # Dictionary to store item prices
    
    print("\nWelcome to Inventory Management System!")
    
    # Main program loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            add_item(item_names, item_prices)
        elif choice == "2":
            update_price(item_names, item_prices)
        elif choice == "3":
            view_items(item_names, item_prices)
        elif choice == "4":
            print("\nThank you for using Inventory Management System!")
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
