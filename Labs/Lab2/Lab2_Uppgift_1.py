import matplotlib.pyplot as plt
import numpy as np

# felhantering för input vid negativa tal och icke-numeriska inputs
while True:
    try:
        print("Input width and height: ")
        testpunkt_x, testpunkt_y = float(input()), float(input())
        if testpunkt_x < 0:
            raise ValueError("Width must be a positive number")
        if testpunkt_y < 0:
            raise ValueError("Height must be a positive number")
        break
    except ValueError as err:
        print("Invalid input:", err)

testpunkt = (testpunkt_x, testpunkt_y)

# Definiera lista och importera datapoints från fil, cleana upp datapunkter och tilldela labels
datapoints = []
pathData = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\datapoints.txt"
with open(pathData, "r") as file:
    for line in file:
        DataParts = line.strip().split(",")
        if len(DataParts) == 3:
            WidthData = float(DataParts[0])
            HeightData = float(DataParts[1])
            Label = int(DataParts[2])
            datapoints.append((WidthData, HeightData, Label))

# separera datapunkter för pichu (0) och pikachu (1)
WidthsPichu = []
HeightsPichu = []
WidthsPikachu = []
HeightsPikachu = []

for width, height, label in datapoints:
    if label == 0:
        WidthsPichu.append(width)
        HeightsPichu.append(height)
    elif label == 1:
        WidthsPikachu.append(width)
        HeightsPikachu.append(height)

# nearest neighbor funktion med euklidisk distance beräkning
def EuclideanDistance (p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


def NearestNeighbor(testpunkt, datapoints):
    MinDistance = float("inf")
    PredictedLabel = None

    for data in datapoints:
        DataPoint = (data[0], data[1])
        label = data[2]
        distance = EuclideanDistance(testpunkt, DataPoint)
        if distance < MinDistance:
            MinDistance = distance
            PredictedLabel = label

    return PredictedLabel

# Klassificera testpunkt som pichu eller pikachu
PredictedLabel = NearestNeighbor(testpunkt, datapoints)
if PredictedLabel == 0:
    print("Sample classified as Pichu")
else:
    print("Sample classified as Pikachu")




