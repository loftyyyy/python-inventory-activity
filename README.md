# Assignment for Programming Languages CS15L(4404)

## Activity Title
**Activity 1 - Python Inventory System**

## Author
``Rho Alphonce E. Jornadal``

## Sample output from the instructions
![Sample Output](images/sample%20output.png)

## Sample output from my take
![My Sample Ouput](images/my%20sample%20output.png)

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

3. **Menu System**: Uses loops and conditionals for navigation
   - Interactive menu with numbered options
   - Input validation for menu choices
   - Continuous operation until user chooses to exit

### Technical Constraints
- No delete functionality
- No out-of-stock features
- Uses Python lists and dictionaries as primary data structures
- Implements loops for menu navigation
- Uses conditionals for input validation and error handling


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
- **Error Handling**: Try-except blocks for validating input
- **User Input**: Interactive console-based interface
