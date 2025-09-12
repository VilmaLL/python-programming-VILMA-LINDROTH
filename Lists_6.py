import matplotlib.pyplot as plt
import random
import math

NrOfPoints = int(input("Enter Nr of points to simulate: "))

punkt = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(NrOfPoints)]


BiggerX = []
BiggerY = []
SmallerX = []
SmallerY = []

RedPoints = 0
BluePoints = 0

for x, y in punkt:
    d = math.sqrt(x**2 + y**2)

    if d < 1.0:
        SmallerX.append(x)
        SmallerY.append(y)
        RedPoints += 1
    else:
        BiggerX.append(x)
        BiggerY.append(y)
        BluePoints += 1

Fraction = RedPoints/BluePoints
print(f"Fraction between red and blue points: {Fraction:.4f}")

'''
plt.figure(figsize=(6, 6))
plt.scatter(SmallerX, SmallerY, color='red', s=1)
plt.scatter(BiggerX, BiggerY, color='blue', s=1)
plt.title(f"Simulation of {NrOfPoints} points")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
'''