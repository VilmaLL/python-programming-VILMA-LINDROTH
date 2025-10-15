import numpy as np
import matplotlib.pyplot as plt

# a)

Possible_Values_of_Dice = [1, 2, 3, 4, 5, 6]
sum = 0
for i in Possible_Values_of_Dice:
    sum += i
Theoretical_Mean = sum/len(Possible_Values_of_Dice)
print(Theoretical_Mean)

# b)
nr_of_rolls = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

Means = []

for sim in nr_of_rolls:
    Dice_Rolls = np.random.randint(1, 7, sim)

    Dice_Rolls_value = 0
    for roll in Dice_Rolls:
        Dice_Rolls_value += roll

    mean = Dice_Rolls_value/len(Dice_Rolls)
    Means.append(mean)

plt.figure(figsize = (10, 6))
plt.plot(nr_of_rolls, Means)
plt.xscale("log")
plt.xlabel("Number of rolls")
plt.ylabel("Sample mean")
plt.title("Mean of a six-sided die")
plt.grid()
plt.show()