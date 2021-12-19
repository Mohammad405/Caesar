import caesar

def walcome():
    print('+*************************+')
    print('|****< Caesar cipher >****|')
    print('+*************************+')

def help():
    print("""* Commands:
                * I : Enter.
                * E : enctypt.
                * D : decrypt.
                * S : stop.
                * H : Help.
                """)

def userInput():
    mgs = input('Enter the masage: ')
    key = int(input('Enter the key: '))
    return mgs , key

def enter():
    m, k = userInput()
    c = caesar.Caeser(m, k)
    return c


def main():
    
    walcome()
    
    cipher = None

    while True:
        userCommand = input('Enter a command: ')
        if userCommand == 'S':
            print('Goodbye!')
            break

        elif userCommand == 'I':
            cipher = enter()

        elif userCommand == 'E':
            emgs = cipher.encrypt()
            print(f'The encrypted masage is {emgs}')
        
        elif userCommand == 'D':
            dmgs = cipher.decrypt()
            print(f'The decrypted masage is {dmgs}')
        
        elif userCommand == 'H':
            help()

        else:
            print('Plase, Enter a usefull command!!')

if __name__ =='__main__':main()