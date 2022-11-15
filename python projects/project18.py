import random, sys

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == "QUIT":
            print("thanks for playing")
            sys.exit()
            
    diceStr = diceStr.lower().replace(' ', '')

    if dIndex == -1:
       raise Exception("missing the d character.")
    
    numberOfDice = diceStr[:dindex] 
    if not numberOfDice.isdecimal():
        raise Excetion("missing the number of dice. ")
    numberOfDice = int(numberOfDice)

    modIndex = diceStr.find('+')
    if modIndex == -1:
        modIndex = diceStr.find("-")
    
    if modIndex == -1:
        numberOfSides = diceStr[dIndex + 1:]
    else:
        numberOfSides = diceStr[dIndex + 1: modIndex]
    
    if not numberOfSides.isdecimal():
        raise Exception('Missing the number of sides.')
    numberOfSides = int(numberOfSides)

    if modIndex == -1:
        modAmount = 0
    else:
        modAmount = int(diceStr[modIndex + 1 :])
        if diceStr[modIndex] == '-':
            modAmount = -modAmount

    rolls = []
    for i in range(numberOfDice):
        rollResult = random.randint(1, numberOfSides)
        rolls.append(rollResult)
    
    print('total: ', sum(rolls) + modAmount, '(each die:', end = '')

    for i, roll in enumerate(rolls):
        rolls[i] = str(roll)
    print(', '.join(rolls), end = ' ')

    if modAmount != 0:
        modSign = diceStr[modIndex]
        print(', {}{}'.format(modSign, abs(modAmount)), end = '')
        print(')')
    except Exception as exc:
        print('Invalid input. Enter something like ')
        print('Input was invalid becaused: ' + str(exc))
        continue 
    
