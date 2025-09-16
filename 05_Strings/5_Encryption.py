# c) encryption or decryption choice

Choice = input ("Encryption or decryption? (e/d): ")

if Choice == "e":
    # a) encryption
    def custom_encrypt(letter):
        custom_map = {
            "z" : "å",
            "å" : "ä",
            "ä" : "ö",
            "ö" : "a",
            "Z" : "Å",
            "Å" : "Ä",
            "Ä" : "Ö",
            "Ö" : "A"
        }

        if letter in "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY":
            return chr(ord(letter) + 1)
        elif letter in custom_map:
            return custom_map[letter]
        else:
            return letter

    Word = input("word: ")
    NewWord = "".join(custom_encrypt(c) for c in Word)
    print(NewWord)

elif Choice == "d":
    # b) decrypt
    def custom_decrypt(letter):
        custom_map = {
            "å" : "z",
            "ä" : "å",
            "ö" : "ä",
            "a" : "ö",
            "Å" : "Z",
            "Ä" : "Å",
            "Ö" : "Ä",
            "A" : "Ö"
        }

        if letter in "bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ":
            return chr(ord(letter) - 1)
        elif letter in custom_map:
            return custom_map[letter]
        else:
            return letter

    Word = input("word: ")
    NewWord = "".join(custom_decrypt(c) for c in Word)
    print(NewWord)