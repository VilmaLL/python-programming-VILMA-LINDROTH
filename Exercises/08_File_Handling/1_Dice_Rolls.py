import random

path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\dice_rolls.txt" 

DiceRolls20 = [random.randint(1, 6) for i in range(20)]

with open(path, "w") as File:

    File.write("Simulate 20 dice rolls:\n")
    File.write(" ".join(str(roll) for roll in DiceRolls20))
    File.write("\n\n")

    DiceRollsSorted = sorted(DiceRolls20)

    File.write("Sorted dice rolls: \n")
    File.write(" ".join(str(roll) for roll in DiceRollsSorted))
    File.write("\n\n")

    NrOf4 = DiceRollsSorted.count(4)

    File.write(f"Number of fours: {NrOf4}")

