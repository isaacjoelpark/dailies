def login(database, username, password):
    if username in database and database[username] == password:
        print('welcome')
        return username 
    else: 
        print("login failure")
        return " "

def register(database, username):
    if username in database:
        print("already exists, please enter new username")
        return ""
    else:
        print("username registered now!")
        return username

def donate(username):
    donation_amt = int(input("Enter the amount that you wish to donate: "))
    donation = (username + "donated" + donation_amt)
    print(donation)

def show_donations(donations):
    print("---All Donations ---")
    if donations == []:
        print("Currently, ther are no donations. ")
    else:
       print("nothing")
