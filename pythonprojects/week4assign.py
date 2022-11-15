class User: 
    def __init__(self, name, pin, password):
        self.name = name 
        self.pin = pin 
        self.password = password 
    def change_name(self, name):
        self.name = name 
        print("Your name has changed to, ", self.name)
    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has changed to, ", self.pin)
    def change_password(self, password):
        self.password = password 
        print("Your password has changed to, ", self.password)

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0 
    def show_balance(self):
        print(self.name, "has an account of: ", self.balance)
    def withdraw(self, lost):
        self.balance = self.balance - lost
        print(self.name,"has an account of ", self.balance)
    def deposit(self, gain): 
        self.balance = self.balance + gain
        print(self.name, "has an account of ", self.balance)
    def transfer_money(self, transfer, an_user):
        print("you are going to transfer money", transfer, "to user", an_user.name )
        pin = int(input("please enter your pin to confirm: "))
        if self.pin == pin:
            print("Transfer Authorized")
            print("Transferring $", transfer, "to", an_user.name)
            self.balance -= transfer 
            an_user.balance += transfer
            return True
        else:
            print("Invalid PIN. Transaction cancelled")
            return False 
    def request_money(self, deposit, an_user):
        print("you are requesting money", deposit, "to user", an_user.name )
        pin = int(input("Enter " + an_user.name + "s pin"))
        if self.pin == pin:
            print(" ")
            passw = input("please enter password")
            if passw == self.password:
                print("Request authorized")
                self.balance -= deposit
                an_user.balance += deposit
                print(an_user.name, "sent", deposit)
                return True
            else:
                return False
        else:
            return False 

        
park = BankUser("Bob", 1234, "password")
# park1 = BankUser("Bob", 1234, "password")
# print(park.name, park.pin, park.password)
# park.change_password("newpassword")
# park.change_name("Bobby")
# park.change_pin(4321)
# print(park.name, park.pin, park.password)
park_2 = BankUser("DIck", 1234, "password")
# print(park_2.name, park_2.pin, park_2.password, park_2.balance)
# park_2.show_balance()
# park_2.deposit(5000)
# park_2.withdraw(1000)
# park_2.show_balance()
# park_2.transfer_money(700, park)
# park.show_balance()
# park_2.show_balance()
park_2.request_money(400, park)
park.show_balance()
park_2.show_balance()