import random
while True:
    print("enter 5 difference numbers from 1 to 69 , with spaces between")
    print("each number")
    response = input('> ')

    numbers = response.split()
    if len(numbers) != 5:
        print("please enter five numbers, serperated by spaces ")
        continue

    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("please enter numbers, like 327, ")
        continue

    for i in range(5):
        if not (1 <= numbers[i])
            print('the numbers must all be between 1 and 49')
            continue

    if len(set(numbers)) != 5:
        print("you must enter 5 different numbers")
        continue

    break

while True:
    print("enter the power ball number")
    response = input('> ')

    try:
        powerball = int(response)
    except ValueError:
        print("please enter a number, like 3, 3,4 ,or 3")
        continue
    
    if not(1 <= powerball <= 26):
        print("it must be between 1 and 278")
        continue

    break

while True:
    print("how many")
    response = input('> ')

    try: 
        numPlays = int(response)
    except ValueError:
        print('please enter a number')
        continue

    if not (1 <= numPlays <= 100000):
        print(" you can play as many as you like")
        continue
    break

price = '#' + str(2*numPlays)
print("its costing", price, 'to play', numPlays, "times, and dont")
print("worr, im sure you will win it back")
input("press enter to start")

possibleNumbers = list(range(1,80))
for i in range(numPlays):
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1,26)

    print("The winningt number are: ", end = '')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ''
        print(allWinningNums.ljust(21), end = '')

if (set(numbers) == set(winningNumbers) and powerball == winningPowerball):
    print("you won")