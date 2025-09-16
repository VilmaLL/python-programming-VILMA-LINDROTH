import math

# a)
def EucDistance(P, Q):
    distance = math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
    return distance

# b)
pX = float(input("Enter x-coordinate for point P: "))
pY = float(input("Enter y-coordinate for point P: "))
qX = float(input("Enter x-coordinate for point Q: "))
qY = float(input("Enter y-coordinate for point Q: "))

P = (pX, pY)
Q = (qX, qY)

print(f"Euclidean distance between P and Q: {EucDistance(P, Q)}")
# c)

OriginX = 0
OriginY = 0
TrialPoints = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]
EucDistancesTrial = []


for Q in TrialPoints:
    P = (OriginX, OriginY)
    EucDistancesTrial.append(round(EucDistance(P, Q), 1))

print(EucDistancesTrial)

