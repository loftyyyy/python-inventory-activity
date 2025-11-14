# Python Inventory Management System

## Activity Title
**Inventory Management System - A Python Console Application**

## Problem Description
This program implements a simple inventory management system that allows users to manage items and their prices. The system is designed with the following specifications:

### Data Storage
- **Item names** are stored in a **list** data structure
- **Item prices** are stored in a **dictionary** data structure with item names as keys

### Features
1. **Add Items**: Users can add new items by providing:
   - Item name
   - Item price (must be a valid positive number)
   - Duplicate prevention: The system checks if an item already exists and prevents duplicates

2. **Update Prices**: Users can update the price of existing items
   - Error handling: If the item doesn't exist in inventory, an error message is displayed
   - Shows both old and new price after successful update

3. **View All Items**: Display all items currently in inventory with their prices
   - Formatted table view showing item names and prices
   - Shows total count of items

4. **Menu System**: Uses loops and conditionals for navigation
   - Interactive menu with numbered options
   - Input validation for menu choices
   - Continuous operation until user chooses to exit

### Technical Constraints
- No delete functionality
- No out-of-stock features
- Uses Python lists and dictionaries as primary data structures
- Implements loops for menu navigation
- Uses conditionals for input validation and error handling

## Sample Output

```
Welcome to Inventory Management System!

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 1
Enter item name: Laptop
Enter item price: $999.99
Success: 'Laptop' added with price $999.99

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 1
Enter item name: Mouse
Enter item price: $25.50
Success: 'Mouse' added with price $25.50

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 1
Enter item name: Keyboard
Enter item price: $75.00
Success: 'Keyboard' added with price $75.00

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 3

========================================
   CURRENT INVENTORY
========================================
Item Name                      Price
----------------------------------------
Laptop                    $   999.99
Mouse                     $    25.50
Keyboard                  $    75.00
========================================
Total Items: 3

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 1
Enter item name: Laptop
Error: 'Laptop' already exists in inventory!

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 2
Enter item name to update: Mouse
Enter new price: $29.99
Success: 'Mouse' price updated from $25.50 to $29.99

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 2
Enter item name to update: Monitor
Error: 'Monitor' does not exist in inventory!

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 3

========================================
   CURRENT INVENTORY
========================================
Item Name                      Price
----------------------------------------
Laptop                    $   999.99
Mouse                     $    29.99
Keyboard                  $    75.00
========================================
Total Items: 3

========================================
   INVENTORY MANAGEMENT SYSTEM
========================================
1. Add Item
2. Update Item Price
3. View All Items
4. Exit
========================================

Enter your choice (1-4): 4

Thank you for using Inventory Management System!
Goodbye!
```

## How to Run the Program

1. Make sure you have Python 3 installed on your system
2. Clone this repository or download the `inventory.py` file
3. Open a terminal/command prompt
4. Navigate to the directory containing `inventory.py`
5. Run the command: `python3 inventory.py` (or `python inventory.py` on Windows)
6. Follow the on-screen menu to interact with the inventory system

## Key Programming Concepts Demonstrated

- **Lists**: Used to maintain the order of items added to inventory
- **Dictionaries**: Used for efficient price lookup and updates using item names as keys
- **Loops**: `while` loop for continuous menu operation until user exits
- **Conditionals**: `if-elif-else` statements for menu navigation and input validation
- **Functions**: Modular code organization with separate functions for each operation
- **Error Handling**: Try-except blocks for validating numeric input
- **User Input**: Interactive console-based interface
- **String Formatting**: Formatted output for better user experience

## Program Structure

The program consists of the following functions:

1. `display_menu()` - Displays the main menu options
2. `add_item()` - Handles adding new items with duplicate prevention
3. `update_price()` - Updates prices of existing items with error handling
4. `view_items()` - Displays all items in a formatted table
5. `main()` - Main program loop that coordinates all operations

## Author
**[Your Full Name Here]**

## Screenshots

### Program Running - Main Menu
![Inventory System Main Menu](screenshot-menu.png)

### Adding Items and Viewing Inventory
![Adding Items](screenshot-add-items.png)

### Error Handling Examples
![Error Handling](screenshot-errors.png)

---

*Note: To see the screenshots, please run the program and capture your own screenshots, or refer to the sample output above which demonstrates all program features.*