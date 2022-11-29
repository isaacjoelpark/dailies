def  show_balance(balance):
    print(float(balance))

def deposit(balance):
    amount = float(input("enter amount to deposit"))
    return balance + amount 

def withdraw(balance):
    amount = float(input("enter the amount to withdraw"))
    return balance - amount

def logout(name):
    print("goodbye", name, "!")