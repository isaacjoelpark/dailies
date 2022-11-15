import sys, time
time.sleep(2)
bottles = 99
PAUSE = 2

try:
    while bottles > 1:
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE) # Pause for PAUSE number of seconds.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1 # Decrease the number of bottles by one.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print() # Print a newline.

    # Display the last stanza:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.
    