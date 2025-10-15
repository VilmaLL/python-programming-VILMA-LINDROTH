
path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\09_Dictionaries\morse.txt"
with open (path, "r") as file:
    MorseTranslate = {}
    for line in file:
        Letters = line.strip().split(":")
        if len(Letters) == 2:
            SvenskBokstav = Letters[0].strip()
            MorseKod = Letters[1].strip()
            MorseTranslate[SvenskBokstav] = MorseKod

def TranslatedToMorse(Text, MorseTranslate):
    Text = Text.upper()
    translation = []
    for char in Text:
        if char in MorseTranslate:
            translation.append(MorseTranslate[char])
        elif char == " ":
            translation.append("/")
        else:
            translation.append("?")
    return " ".join(translation)

Text = input("Ange svensk text: ")
morse_results = TranslatedToMorse(Text, MorseTranslate)
print(morse_results)

    
