def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login     | 2.    Reigster      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations       |")
    print("|               5. Exit                      |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("How much would you like to donate? : ")
    print()
    donation_string = username + " donated $" + donation_amt
    print("Thank you for the donation :)")
    return (donation_string)

def show_donations(donations):
    print("---All Donations ---")
    if donations == []:
        print("Currently, ther are no donations. ")
    else:
        print("nothing")