from menu import MenuItem

class Cafe:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_menu_item(self):
        name = input("Enter item name: ")

        # duplicate item check
        for item in self.menu:
            if item.name.lower() == name.lower():
                print("⚠️ Item already exists in menu")
                return

        price = float(input("Enter item price: "))
        self.menu.append(MenuItem(name, price))
        print("✅ Item added to menu")

    def show_menu(self):
        if not self.menu:
            print("Menu is empty")
            return

        print("\n--- Cafe Menu ---")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item.name} - ₹{item.price}")

    def take_order(self):
        self.show_menu()
        if not self.menu:
            return

        choice = int(input("Select item number: "))
        if 1 <= choice <= len(self.menu):
            self.order.append(self.menu[choice - 1])
            print("✅ Item added to order")
        else:
            print("❌ Invalid choice")

    def generate_bill(self):
        if not self.order:
            print("No items ordered")
            return

        total = 0
        print("\n--- Bill ---")
        for item in self.order:
            print(f"{item.name} - ₹{item.price}")
            total += item.price

        print("----------------")
        print(f"Total Amount: ₹{total}")
