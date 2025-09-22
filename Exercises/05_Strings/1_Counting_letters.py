Word = input("Chose a word: ")
NrOfLetters = len(Word)
print(f"The word {Word} has {NrOfLetters} letters")

NrOfUpperCase = 0
NrOfLowerCase = 0

for char in Word:
    if char.isupper():
        NrOfUpperCase += 1
    elif char.islower():
        NrOfLowerCase += 1

print(f"The word {Word} has {NrOfUpperCase} uppercase letters and {NrOfLowerCase} lowercase letters")