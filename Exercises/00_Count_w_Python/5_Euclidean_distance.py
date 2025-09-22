import math

P1 = (3, 5)
P2 = (-2, 4)

distance = math.sqrt((P2[0]-P1[0])**2 + (P2[1]-P1[1])**2)

print(f"Euclidean distance: {distance:.1f}")
