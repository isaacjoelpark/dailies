def main():
    print("diamonds, by isaac park")

    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlinediamond(size):
    for i in range(size):
        print(' ' * (size -1 -1 ), end = '')
        print('/', end = '')
        print(' ' * (i * 2), end = '')
        print('\\')
    
    for i in range(size):
        print(' ' * i, end = '')
        print('\\', end = '')
        print(' ' * ((size - i -1 ) * 2), end = '')
        print('/')

def displayFilledDiamond(size):
    for i in range(size):
        print(' ' * i, end = '')
        print('\\' * (size - 1), end = '')
        print('/' * (size -1))

if __name__ == '__main__':
    main()
