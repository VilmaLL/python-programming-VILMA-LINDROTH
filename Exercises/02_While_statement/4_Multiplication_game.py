import random

PlayAgain = True
UserIsRight = 0
UserIsWrong = 0

DifficultyLevel = input("Choose a difficulty Level (Easy, Medium, Hard): ")
if DifficultyLevel.lower() == "easy":
    Nr = 10
elif DifficultyLevel.lower() == "medium":
    Nr = 20 
elif DifficultyLevel.lower() == "hard":
    Nr = 50

while PlayAgain == True:
    
    X = random.randint(1, Nr)
    Y = random.randint(1, Nr)
        
    CorrectAnswer = X * Y

    UserAnswer = int(input(f"What is {X} times {Y}? "))

    if UserAnswer == CorrectAnswer:
        print("Good work!")
        UserIsRight +=1
    else:
        print(f"The correct answer is {CorrectAnswer}")
        UserIsWrong +=1

    print(f"You have {UserIsRight} correct answers and {UserIsWrong} wrong answers.")
    PlayAgainInput = input("Do you want to play again? (y/n) ")
    if PlayAgainInput.lower() != 'y':
        PlayAgain = False
        print("Thanks for playing!")
    
