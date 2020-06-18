import secrets


#possible character list
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 abcdefghijklmnopqrstuvwxyz'


#message and key go in, encrypted/decrypted message comes out
def caesarWheel(message, key, encrypt):
#deconstructs key and message into numbers for math purposes, then encrypts or decrypts as appropriate
    nmessage = str()
    for char, mchar in zip(key, message):
        num = CHARACTERS.find(char)
        mnum = CHARACTERS.find(mchar)

        if encrypt == True:
            nindex = mnum + num
            if nindex >= len(CHARACTERS):
                nindex -= len(CHARACTERS)

            nmessage += CHARACTERS[nindex]
        else:
            nindex = mnum - num
            if nindex < 0:
                nindex += len(CHARACTERS)


            nmessage += CHARACTERS[nindex]
    return nmessage

#message goes in, appropriate key comes out
def keygen(message):
    keylen = len(message)

    #for loop constructs the key
    nkey = str()
    print('generating key..')
    for i in range(keylen):
        num = secrets.randbelow(len(CHARACTERS))
        nkey = nkey + CHARACTERS[num]

    return nkey

#message or key goes in, boolean (and possibly corrections) get returned
def charchecker(text):
    charcheck = True
    for char in text:
        if char not in CHARACTERS:
            charcheck = False
            print("""Input does not use the correct types of characters.
            Please confine yourself to alphanumerics and not symbols like '$' or '*'. """)
            break
    return charcheck

#message gets passed in, ensures the user defined key is valid
def keyfilter(message):
    message = message
    key = input('Please enter your key: ')
    while True:
        lencheck = False
        charcheck = True
        if len(key) == len(message):
            lencheck = True
            print('key is proper length')
        if len(key) != len(message):
            print('key is not the proper length')
        charcheck = charchecker(key)
        if lencheck == True and charcheck == True:
            print('Key is valid')
            break
        key = input('Please enter a valid key: ')
    return key


def main():
    mode = input('''Hello user. Please enter 'e' if you are here to encode a message.
        Enter 'd' if you wish to decode a message: ''')

    #main loop for program runtime
    while True:
        #loop that ensures user answer is valid
        while True:
            if mode == 'e' or mode == 'E' or mode == 'D' or mode == 'd': break
            mode = input("Please enter a valid input, 'e' to encode a message, 'd' to decode : ")
        if mode == 'e' or mode == 'E':
            message = input('Please enter your message: ')
            #loop that ensures message is valid
            while True:
                isValid = charchecker(message)
                if isValid == True: break
                message = input('Please enter a valid message: ')
            keybool = input('Do you wish to use your own key? (y/n) ')
            #loop that ensures user's answer is valid
            while True:
                if keybool == 'Y' or keybool == 'y' or keybool == 'N' or keybool == 'n': break
                keybool = input("Please enter 'y' for yes or 'n' for no: ")
            if keybool == 'Y' or keybool == 'y':
                key = keyfilter(message)
            else: key = keygen(message)
            encrypt = True
            nmessage = caesarWheel(message, key, encrypt)
            print('Your encrypted message reads:', nmessage)
            print('Your key is:', key)
        if mode == 'd' or mode == 'D':
            message = input('Please enter your encrypted message: ')
            #loop that ensures message is valid
            while True:
                isValid = charchecker(message)
                if isValid == True: break
                message = input('Please enter a valid message: ')
            key = keyfilter(message)
            encrypt = False
            nmessage = caesarWheel(message, key, encrypt)
            print('Your decrypted message reads:', nmessage)


        isFinished = input('Are you finished today? (y/n): ')
        while True:
            if isFinished == 'Y' or isFinished == 'y' or isFinished == 'N' or isFinished == 'n': break
            isFinished = input("Please enter 'y' for yes or 'n' for no: ")
        if isFinished == 'Y' or isFinished == 'y': break
        mode = input("Select program mode, 'e' to encode, 'd' to decode: ")



if __name__ == '__main__':
    main()
