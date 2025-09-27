def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            choice = input("Enter the item to add:")
           
        elif choice == 2:
            choice =input("Enter the item to remove:")
                        else:
                print("item cannot be found")
        elif choice == 3:
            if shopping_list:
                print("your shopping list")
                for i in shopping_list:
                    print("-",item)
            else:
                print("your shopping list is empty")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()