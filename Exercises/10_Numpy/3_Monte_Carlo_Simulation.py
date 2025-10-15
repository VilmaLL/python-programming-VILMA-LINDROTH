import numpy as np
import matplotlib.pyplot as plt

def SimulatePoints(simulated_nr_of_points):
    SimPoints = np.random.uniform(-1, 1, (simulated_nr_of_points, 2))
    return SimPoints

def EucDistanceToOrigin(SimPoints):
    distance = np.linalg.norm(SimPoints, axis = 1)
    return distance

def ClassifyPoints(distance, SimPoints):
    OutsideCircle = SimPoints[distance > 1]
    InsideCircle = SimPoints[distance <= 1]
    return OutsideCircle, InsideCircle

def PlotPoints(OutsideCircle, InsideCircle):
    plt.figure(figsize=(8, 8))
    plt.scatter(OutsideCircle[:,0], OutsideCircle[:,1], color = "blue")
    plt.scatter(InsideCircle[:,0], InsideCircle[:,1], color = "green")
    plt.title("Simulation of 500,000 points")
    plt.show()

def FractionBetweenInAndOut(InsideCircle, OutsideCircle):
    fraction = len(InsideCircle)/len(OutsideCircle)
    return fraction

# a)
SimPoints = SimulatePoints(500000)
distance = EucDistanceToOrigin(SimPoints)
OutsideCircle, InsideCircle = ClassifyPoints(distance, SimPoints)
PlotPoints(OutsideCircle, InsideCircle)

# b)

fraction = FractionBetweenInAndOut(InsideCircle, OutsideCircle)
print(fraction)
