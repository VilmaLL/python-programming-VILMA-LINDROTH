import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)

def f(x): 
    return x**2 - 3
def g(x):
    return 4*x - 7

f_y = f(x)
g_y = g(x)

plt.plot(x, f_y, label= "f(x) = x^2 - 3", color= "blue")
plt.plot(x, g_y, label= "g(x) = 4x - 7", color= "green")

plt.title("two funktions")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


