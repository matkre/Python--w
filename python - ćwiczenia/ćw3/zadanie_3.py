def wiadomosc():
    mess = str(input("Podaj wiadomosc: "))
    return mess


def klucz():
    k = 0
    while True:
        k = int(input("Wartość: "))
        if 1 <= k <= 26:
            return k


def szyfrowanie(k, mess):

    sz_c = ""

    for symbol in range(len(mess)):
        char = mess[symbol]

        if char.isupper():
            sz_c += chr((ord(char) + k - 65) % 26 + 65)
        else:
            sz_c += chr((ord(char) + k - 97) %26 + 97)

    return sz_c


k = getKey()
mess = wiadomosc()
print(szyfrowanie(k, mess))
