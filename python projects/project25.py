import random, sys, time
while True:
    print()
    print('it is high noon.')
    time.sleep(random.randint(20,50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        print("you drw draw appeeared! you lose.")
    elif timeElapsed > 0.3: 
        timeElapsed = round(timeElapsed, 4)
        print(" you took, time ", timeElapsed, "seconds to draw too slow")
    else:
        timeElapsed = round(timeElapsed, 4)
        print("you took", timeElapsed, "seconds to draw.")
        print("you are the fastest draw in th west! you win!")
    print("enter quit to stop, or press enter to play again.")
    response = input('> ').upper()
    if response == 'QUIT':
        print("Thanks for playing!")
        sys.exit()