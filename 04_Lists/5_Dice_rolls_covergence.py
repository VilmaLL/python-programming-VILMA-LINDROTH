import matplotlib.pyplot as plt
import random

# a)
'''
DiceRolls = [random.randint(1, 6) for _ in range(100)]
NrOfSixes = DiceRolls.count(6)
print(f"Number of sixes: {NrOfSixes}")
'''

# b)
x = [10, 100, 1000, 10000, 100000, 1000000]
NrOfSixes = []
Probabilities = []

random.seed(1)

for rolls in x:
    outcomes = [random.randint(1, 6) for _ in range(rolls)]
    sixes = outcomes.count(6)
    prob = sixes / rolls

    NrOfSixes.append(sixes)
    Probabilities.append(prob)

for i, rolls in enumerate(x):
    print(f"Rolls: {rolls}, Sixes: {NrOfSixes[i]}, Probability: {Probabilities[i]:.4f}")    


# c)    
plt.plot(x, Probabilities)
plt.title("Probability of rolling a six")
plt.xlabel("Number of Rolls")
plt.xscale("log")
plt.ylabel("Probability")
plt.show()

