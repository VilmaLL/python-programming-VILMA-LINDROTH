import numpy as np
from collections import Counter

Nr_Of_Throws = 1000000
Simulated_Numbers = np.random.randint(1, 7, Nr_Of_Throws)

counts = Counter(Simulated_Numbers)

Count_Of_Numbers = {str(i) : counts.get(i, 0) for i in range(1, 7)}

for key, value in Count_Of_Numbers.items():
    print(f"{key} : {value}")