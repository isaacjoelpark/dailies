from donations_pkg.homepage import show_homepage, show_donations, donate
from donations_pkg.user import login, register 
database = {"admin" : "password123"}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate")
else: 
    print("Logged in as:", authorized_user)
while True:
    option = int(input("Please enter your option! "))
    if option == 1: 
        username = input("Please enter your username: ")
        password = input("please enter your password: ")
        authorized_user = login(database, username, password)
    elif option == 2:
        username = input("Please enter your username: ")
        password = input("please enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
        else:
            print("false, ")

    elif option == 3:
        if authorized_user == " ":
            print("you are not logged in. ")
        else: 
            donation_string = donate(authorized_user)
            if  donation_string != "":
                donations.append(donation_string)
                print(" ")
        
        
        print(" you have donated" + donations)
        print("thank you for your donation")
    elif option == 4:
        print("todo, write login functionality")
    elif option == 5:
        print("todo, write login functionality")
    else: 
        print("todo, write login functionality")