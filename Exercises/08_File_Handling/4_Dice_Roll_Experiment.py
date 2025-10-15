import random

simulations = [10, 100, 1000, 10000, 100000]

results = {}

for num_rolls in simulations:
    rolls = [random.randint(1, 6) for _ in range (num_rolls)]
    counts = {i: rolls.count(i) for i in range (1, 7)}
    probabilities = {i: counts[i] / num_rolls for i in range(1, 7)}
    results[num_rolls] = (counts, probabilities)

path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\simulation.txt"

with open(path, "a") as file:
    for num_rolls in simulations:
        counts, probabilities = results[num_rolls]
        file.write(f"Number of rolls: {num_rolls}\n")
        for i in range(1, 7):
            file.write(f"{i}s: {counts[i]}, probability: {probabilities[i]:.4f}\n")
        file.write("\n")

