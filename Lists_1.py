import random

DiceRolls = []

for i in range(10):
    RandomDice = random.randint(1, 6)
    DiceRolls.append(RandomDice)

print(DiceRolls)

DiceRolls.sort()
print(DiceRolls)

DiceRolls.sort(reverse=True)
print(DiceRolls)
MaxValue = DiceRolls[0]
MinValue = DiceRolls[9]
print(f"Max value: {MaxValue}, Min value: {MinValue}")
