Squares = [i**2 for i in range(-10, 11)]

import matplotlib.pyplot as plt
plt.plot(range(-10, 11), Squares)
plt.title("Squares from -10 to 10")
plt.show()
