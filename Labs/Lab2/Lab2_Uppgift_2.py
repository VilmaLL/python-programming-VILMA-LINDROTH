import numpy as np
from collections import Counter

# felhantering för input vid negativa tal ´samt icke-numerisk input
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
        print("Invalid input: ", err)

testpunkt = (testpunkt_x, testpunkt_y)

# Definiera lista och importera datapoints från fil. cleana upp datapunker och tilldela labels
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

# nearest neighbor (NNK) funktion med euklidisk distans som beräkning. k=10 
def EuclideanDistance (p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


def NearestNeighbor(testpunkt, datapoints, k=10):
    distances = []

    for data in datapoints:
        DataPoint = (data[0], data[1])
        label = data[2]
        distance = EuclideanDistance(testpunkt, DataPoint)
        distances.append((distance, label))

    distances.sort(key = lambda x: x[0])

    k_neighbors = distances[:k]

    k_labels = [label for _, label in k_neighbors]

    most_common = Counter(k_labels).most_common(1) 

    return most_common[0][0]

# Klassificera testpunkt som pichu eller pikachu
PredictedLabel = NearestNeighbor(testpunkt, datapoints, k = 10)
if PredictedLabel == 0:
    print("Sample classified as Pichu")
else:
    print("Sample classified as Pikachu")

