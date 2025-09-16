import random

RandomInt = random.randint(1, 100)
NrOfGuesses = 0
Continue = True
min = 1
max = 100


#while (Continue == True):
#    guess = int(input("Guess the number 1-100: "))
#    NrOfGuesses += 1

#    if (guess == RandomInt):
#        print("Congratulations player!")
#        print("You found the number in", NrOfGuesses, "guesses!")
#        Continue = False
#  
#    elif (guess < RandomInt):
#        print("Your guess is too low, try again!")

#    elif (guess > RandomInt):   
#        print("Your guess is too high, try again!")


while (Continue == True):
    Guess = (min + max) // 2
    print(Guess)
    NrOfGuesses += 1
    if (Guess == RandomInt):
        print("Congratulations Computer!")
        print("You found the number in", NrOfGuesses, "guesses!")
        Continue = False
    elif (Guess < RandomInt):
        min = Guess + 1
    elif (Guess > RandomInt):
        max = Guess - 1

