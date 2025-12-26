from cafe import Cafe

cafe = Cafe()

while True:
    print("\n--- Cafe Management System ---")
    print("1. Add Menu Item")
    print("2. Show Menu")
    print("3. Take Order")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cafe.add_menu_item()
    elif choice == "2":
        cafe.show_menu()
    elif choice == "3":
        cafe.take_order()
    elif choice == "4":
        cafe.generate_bill()
    elif choice == "5":
        print("Thank you for visiting our cafe ☕")
        break
    else:
        print("Invalid choice")
