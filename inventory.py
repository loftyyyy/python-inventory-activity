def main():
    items = []
    item_prices = {}

    print("====================== INVENTORY MENU ======================")
    print("[1] Add Items")
    print("[2] Update Price")
    print("[3] Exit")

    while True:
        try: 

            input_option = input("Choice: ")

            if input_option == "1":

                item_name = input("Enter item name to add: ")
                
                if(item_name in items):
                    print(f"Item '{item_name}' already exists in inventory.\n")
                    continue
                
                item_price = float(input("Enter item price: "))
                if(item_price < 0 | type(item_price) != float):
                    print("Price cannot be negative or not a number. Please try again.\n")
                    continue

                items.append(item_name)
                item_prices[item_name] = item_price
                    
                print(f"Item '{item_name}' with price {item_price} added to inventory. Please try again")
                print("Item added successfully")

            elif input_option == "2":
                item_name = input("Enter item name to update: ")

                if(item_name not in items):
                    print(f"Item '{item_name}' not found in inventory.\n")
                else:
                    item_price = float(input("Enter new item price: "))

                    if(item_price < 0 | type(item_price) != float):
                        print("Price cannot be negative or not a number. Please try again.\n")
                        continue

                    previous_price = item_prices[item_name]
                    item_prices[item_name] = item_price
                    
                    print(f"Price for item '{item_name}', updated from {previous_price} to {item_price}.\n")
                    print("Price updated successfully")

            elif input_option == "3":
                print("Exiting the inventory menu. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")

        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    main()