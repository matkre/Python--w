def getMessage():
    message = str(input("Podaj wiadomość do zaszyfrowania: "))
    return message


def getKey():
    key = 0
    while True:
        key = int(input("Podaj wartość szyfrowania: "))
        if 1 <= key <= 26:
            return key


def getCaesarMessage(key, message):

    caesar = ""

    for symbol in range(len(message)):
        char = message[symbol]

        if char.isupper():
            caesar += chr((ord(char) + key - 65) % 26 + 65)
        else:
            caesar += chr((ord(char) + key - 97) %26 + 97)

    return caesar


key = getKey()
message = getMessage()
print(getCaesarMessage(key, message))
