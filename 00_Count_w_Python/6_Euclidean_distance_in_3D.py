import math

P1 = (2, 1, 4)
P2 = (3, 1, 0)

p = (P1[0], P1[1], P1[2])
q = (P2[0], P2[1], P2[2])

distance = math.sqrt((P1[0]-P2[0])**2 + (P1[1] - P2[1])**2 + (P1[2] - P2[2])**2)

print (f"Euclidean distance: {distance:.2f}")
