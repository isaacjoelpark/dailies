import sys
while True:
    while True:
        response = input('> ').upper()
        if response == 'quit':
            print("Thanks for playing!")
            sys.exit()
        if response.iddecimal() and int(response) != 0:
            nth = int(response)
            break
        print('please enter a number greater than 0 ,  or quit')
    print()

    if nth == 1:
        print('0')
        print()
        print("the fibonacci number is 0.")
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print("the 2 fibonacid number is 1.")
        continue

    if nth >= 10000:
        print("""warning: this iwll tkae ahiwle to display on the screen. if you want to quit this program beofer it is done, press ctrl-c, press enter to begin""")

        secondtoLasNUmber = 0 
        lastNumber = 1 
        fibNumbersCalculated = 2 

        print('0, 1, ', end = '')
        while True:
            
            if fibNumbersCalculated == nth:
                print()
                print()
                print('the number is', fibNumbersCalculated, "fibonaccid number is ", nextNumber, sep = '')
                break
            print(', ', end = '')

