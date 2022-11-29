from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

balance = 0 
print("          == Automated Teller Machine == ")
name = input("Enter name to register: ")
pin = int(input("please enter your pin: "))
print(name, "has benn reistered witha starting balance of $", balance)

while True:
    name_to_validate = input('enter your name:')
    pin_to_valid = int(input("enter your pin "))
    if name_to_validate == name and pin_to_valid == pin: 
        print("valid credtials")
        break
    else:
        print("invalid")
        continue

while True:  
    atm_menu(name)
    option = int(input("please choose an option: "))
    if option == 1:
        account.show_balance(balance)
    elif option == 2:
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == 3: 
        balance = account.withdraw(balance)
        print(balance)
    elif option == 4: 
        account.logout(name)
        break