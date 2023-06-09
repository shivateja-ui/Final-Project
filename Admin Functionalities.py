#Admin Functionalities
import random

class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
class AdminMenu:
    def __init__(self):
        self.food_items = []
        self.next_food_id = 1
    def add_food_item(self):
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount for the food item (in decimal form): "))
        stock = int(input("Enter the stock amount of the food item: "))
        food_id = self.generate_food_id()
        food = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food)
        print(f"Food item '{name}' added with ID: {food_id}")
    def generate_food_id(self):
        return random.randint(1000, 9999)
    def edit_food_item(self):
        food_id = int(input("Enter the ID of the food item to edit: "))
        for food in self.food_items:
            if food.food_id == food_id:
                name = input("Enter the new name of the food item: ")
                quantity = input("Enter the new quantity of the food item: ")
                price = float(input("Enter the new price of the food item: "))
                discount = float(input("Enter the new discount for the food item (in decimal form): "))
                stock = int(input("Enter the new stock amount of the food item: "))
                food.name = name
                food.quantity = quantity
                food.price = price
                food.discount = discount
                food.stock = stock
                print(f"Food item with ID {food_id} edited successfully.")
                return
        print(f"Food item with ID {food_id} not found.")
    def view_all_food_items(self):
        if len(self.food_items) == 0:
            print("No food items found.")
        else:
            print("Food items:")
            for food in self.food_items:
                print(f"ID: {food.food_id}, Name: {food.name}, Quantity: {food.quantity}, "
                      f"Price: {food.price}, Discount: {food.discount}, Stock: {food.stock}")
    def remove_food_item(self):
        food_id = int(input("Enter the ID of the food item to remove: "))
        for food in self.food_items:
            if food.food_id == food_id:
                self.food_items.remove(food)
                print(f"Food item with ID {food_id} removed successfully.")
                return
        print(f"Food item with ID {food_id} not found.")
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    accounts[username] = {
        'password': password,
        'email': email,
        'phone_number': phone_number,
        'address': address
    }
    print("Account created successfully.")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if accounts.get(username) and accounts[username]['password'] == password:
        return True
    print("Invalid username or password.")
    return False
menu = AdminMenu()
accounts = {}
while True:
    print("\n==== Welcome to the Admin Panel ====")
    print("1. Create Account")
    print("2. Login")
    print("0. Exit")
    choice = input("Enter your choice (0-2): ")
    if choice == "1":
        create_account()
    elif choice == "2":
        if login():
            while True:
                print("\n==== Admin Menu ====")
                print("1. Add new food item")
                print("2. Edit food item")
                print("3. View all food items")
                print("4. Remove food item")
                print("0. Logout")
                choice = input("Enter your choice (0-4): ")
                if choice == "1":
                    menu.add_food_item()
                elif choice == "2":
                    menu.edit_food_item()
                elif choice == "3":
                    menu.view_all_food_items()
                elif choice == "4":
                    menu.remove_food_item()
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