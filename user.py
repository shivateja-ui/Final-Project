class FoodItem:
    def __init__(self, food_id, name, quantity, price):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
class UserMenu:
    def __init__(self):
        self.food_items = []
        self.orders = []
        self.next_order_id = 1
    def add_food_item(self, name, quantity, price):
        food_id = len(self.food_items) + 1
        food = FoodItem(food_id, name, quantity, price)
        self.food_items.append(food)
    def show_food_list(self):
        print("Available food items:")
        for food in self.food_items:
            print(f"{food.food_id}. {food.name} ({food.quantity}) [INR {food.price}]")
    def place_new_order(self):
        selected_items = []
        order_total = 0
        while True:
            self.show_food_list()
            selected_item_nums = input("Enter the numbers of the items to order (comma-separated): ").split(",")
            selected_item_nums = [int(num.strip()) for num in selected_item_nums]
            for num in selected_item_nums:
                if num > 0 and num <= len(self.food_items):
                    selected_items.append(self.food_items[num - 1])
            order_total = sum([food.price for food in selected_items])
            print("\nSelected items:")
            for food in selected_items:
                print(f"{food.name} ({food.quantity}) [INR {food.price}]")
            choice = input("Do you want to add more items? (Y/N): ")
            if choice.lower() != "y":
                break
        if len(selected_items) > 0:
            order_id = self.next_order_id
            self.next_order_id += 1
            self.orders.append({
                'order_id': order_id,
                'items': selected_items,
                'total': order_total
            })
            print(f"\nOrder placed successfully! Order ID: {order_id}")
        else:
            print("No items selected.")
    def show_order_history(self):
        if len(self.orders) == 0:
            print("No order history found.")
        else:
            print("Order history:")
            for order in self.orders:
                print(f"Order ID: {order['order_id']}")
                print("Items:")
                for food in order['items']:
                    print(f"{food.name} ({food.quantity}) [INR {food.price}]")
                print(f"Total: INR {order['total']}")
                print()
    def update_profile(self, email, phone_number, address):
        self.email = email
        self.phone_number = phone_number
        self.address = address
        print("Profile updated successfully.")
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    accounts[username] = {
        'password': password,
        'email': email,
        'phone_number': phone_number,
        'address': address,
        'menu': UserMenu()
    }
    print("Account created successfully.")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    account = accounts.get(username)
    if account and account['password'] == password:
        return account
    print("Invalid username or password.")
    return None
accounts = {}
while True:
    print("\n==== Welcome ====")
    print("1. Create Account")
    print("2. Login")
    print("0. Exit")
    choice = input("Enter your choice (0-2): ")
    if choice == "1":
        create_account()
    elif choice == "2":
        account = login()
        if account:
            while True:
                print("\n==== User Menu ====")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("0. Logout")

                choice = input("Enter your choice (0-3): ")

                if choice == "1":
                    account['menu'].place_new_order()
                elif choice == "2":
                    account['menu'].show_order_history()
                elif choice == "3":
                    email = input("Enter your new email address: ")
                    phone_number = input("Enter your new phone number: ")
                    address = input("Enter your new address: ")
                    account['menu'].update_profile(email, phone_number, address)
                elif choice == "0":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "0":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")