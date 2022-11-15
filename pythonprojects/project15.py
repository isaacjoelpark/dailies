from p#14 import PAUSE_AMOUNT
import random, sys, time 
WIDTH = 70 
PAUSE_AMOUNT = 0.05

time.sleep(2)

leftWidth = 20
gapWidth = 10 

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + ('# ' * gapWidth ) +('#' * rightWidth))
    try: 
        time.sleep(PAUSE_AMOUNT)
    except: 
        sys.exit()

    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth -1 
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH -1:
        leftWidth = leftWidth + 1
    else:
        pass

    diceRoll = random.randint(1,6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth -1 
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1
    else:
        pass 