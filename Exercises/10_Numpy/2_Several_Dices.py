import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

dice = np.arange(1, 7)
total_nr_of_outcomes = 6**2

sum_matrix = dice[:, None] + dice[None, :]

print(sum_matrix)

unique_sums = np.unique(sum_matrix)
print(unique_sums)

counted = Counter(sum_matrix.flatten())
for i in sorted(counted):
    print(f"{i} : {counted[i]}")


frequency = []
for n in counted:
    frequency.append(counted[n] / total_nr_of_outcomes)

print(frequency)

plt.figure(figsize= (10, 6))
plt.bar(unique_sums, frequency)
plt.title("Probability distributions of sum of 2 dices")
plt.xlabel("Sums")
plt.ylabel("probability")
plt.show()
