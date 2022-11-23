from asyncio import format_helpers


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class Bank_User(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
    balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, to_user, amount):
        print("\nYou are transferring $", amount, "to", to_user.name)
        print("Authentication required")
        pin = int(input("Enter your PIN: "))
        if self.pin == pin:
            print("Transfer Authorized")
            print("Transferring $", amount, "to", to_user.name)
            self.balance -= amount
            to_user.balance += amount
            return True
        else:
            print("Invalid PIN. Transaction cancelled")
            return False

    def request_money(self, from_user, amount):
        print("\nYou are requesting $", amount, "from", from_user.name)
        print("Authentication required...")
        pin = int(input("Enter " + from_user.name + "'s PIN: "))
        if from_user.pin == pin:
            password = input("Enter your password: ")
            if self.password == password:
                print("Request Authorized")
                print(from_user.name, "sent $", amount)
                from_user.balance -= amount
                self.balance += amount
                return True
            else:
                print("Invalid password. Transaction cancelled")
                return False
        else:
            print("Invalid PIN. Transaction cancelled")
            return False


""" Driver Code for Task 1 """

# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3 """
# user1 = Bank_User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password, user1.balance)

""" Driver Code for Task 4 """
# user1 = Bank_User("Bob", 1234, "password")
# user1.show_balance()
# user1.deposit(100)
# user1.show_balance()
# user1.withdraw(50)
# user1.show_balance()

# print(user1.name, user1.pin, user1.password, user1.balance)

""" Driver Code for Task 5 """
user1 = Bank_User("Bob", 1234, "password")
user2 = Bank_User("Alice", 5678, "alicepassword")

user2.deposit(5000)
user2.show_balance()
user1.show_balance()

user2.transfer_money(user1, 500)
user2.show_balance()
user1.show_balance()

user2.request_money(user1, 250)
user2.show_balance()
user1.show_balance()
