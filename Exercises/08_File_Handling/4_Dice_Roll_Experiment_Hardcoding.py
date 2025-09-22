#hardcoding calculations and file writing
"""
Sim10 = []
Sim100 = []
Sim1000 = []
Sim10000 = []
Sim100000 = []

for Roll in range (10):
    Roll = random.randint(1, 6)
    Sim10.append(Roll)
    
for Roll in range (100):
    Roll = random.randint(1, 6)
    Sim100.append(Roll)

for Roll in range (1000):
    Roll = random.randint(1, 6)
    Sim1000.append(Roll)

for Roll in range (10000):
    Roll = random.randint(1, 6)
    Sim10000.append(Roll)

for Roll in range (100000):
    Roll = random.randint(1, 6)
    Sim100000.append(Roll)

NrOf1_10 = Sim10.count(1)
NrOf2_10 = Sim10.count(2)
NrOf3_10 = Sim10.count(3)
NrOf4_10 = Sim10.count(4)
NrOf5_10 = Sim10.count(5)
NrOf6_10 = Sim10.count(6)

ProbabilityFor1_10 = NrOf1_10/10
ProbabilityFor2_10 = NrOf2_10/10
ProbabilityFor3_10 = NrOf3_10/10
ProbabilityFor4_10 = NrOf4_10/10
ProbabilityFor5_10 = NrOf5_10/10
ProbabilityFor6_10 = NrOf6_10/10


NrOf1_100 = Sim100.count(1)
NrOf2_100 = Sim100.count(2)
NrOf3_100 = Sim100.count(3)
NrOf4_100 = Sim100.count(4)
NrOf5_100 = Sim100.count(5)
NrOf6_100 = Sim100.count(6)

ProbabilityFor1_100 = NrOf1_100/100
ProbabilityFor2_100 = NrOf2_100/100
ProbabilityFor3_100 = NrOf3_100/100
ProbabilityFor4_100 = NrOf4_100/100
ProbabilityFor5_100 = NrOf5_100/100
ProbabilityFor6_100 = NrOf6_100/100


NrOf1_1000 = Sim1000.count(1)
NrOf2_1000 = Sim1000.count(2)
NrOf3_1000 = Sim1000.count(3)
NrOf4_1000 = Sim1000.count(4)
NrOf5_1000 = Sim1000.count(5)
NrOf6_1000 = Sim1000.count(6)

ProbabilityFor1_1000 = NrOf1_1000/1000
ProbabilityFor2_1000 = NrOf2_1000/1000
ProbabilityFor3_1000 = NrOf3_1000/1000
ProbabilityFor4_1000 = NrOf4_1000/1000
ProbabilityFor5_1000 = NrOf5_1000/1000
ProbabilityFor6_1000 = NrOf6_1000/1000


NrOf1_10000 = Sim10000.count(1)
NrOf2_10000 = Sim10000.count(2)
NrOf3_10000 = Sim10000.count(3)
NrOf4_10000 = Sim10000.count(4)
NrOf5_10000 = Sim10000.count(5)
NrOf6_10000 = Sim10000.count(6)

ProbabilityFor1_10000 = NrOf1_10000/10000
ProbabilityFor2_10000 = NrOf2_10000/10000
ProbabilityFor3_10000 = NrOf3_10000/10000
ProbabilityFor4_10000 = NrOf4_10000/10000
ProbabilityFor5_10000 = NrOf5_10000/10000
ProbabilityFor6_10000 = NrOf6_10000/10000


NrOf1_100000 = Sim100000.count(1)
NrOf2_100000 = Sim100000.count(2)
NrOf3_100000 = Sim100000.count(3)
NrOf4_100000 = Sim100000.count(4)
NrOf5_100000 = Sim100000.count(5)
NrOf6_100000 = Sim100000.count(6)

ProbabilityFor1_100000 = NrOf1_100000/100000
ProbabilityFor2_100000 = NrOf2_100000/100000
ProbabilityFor3_100000 = NrOf3_100000/100000
ProbabilityFor4_100000 = NrOf4_100000/100000
ProbabilityFor5_100000 = NrOf5_100000/100000
ProbabilityFor6_100000 = NrOf6_100000/100000


path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\simulation.txt"

with open (path, "a") as File:
    File.write("Number of rolls: 10\n")
    File.write(f"Ones: {NrOf1_10}, probability: {ProbabilityFor1_10}\n")
    File.write(f"Twos: {NrOf2_10}, probability: {ProbabilityFor2_10}\n")
    File.write(f"Threes: {NrOf3_10}, probability: {ProbabilityFor3_10}\n")
    File.write(f"Fours: {NrOf4_10}, probability: {ProbabilityFor4_10}\n")
    File.write(f"Fives: {NrOf5_10}, probability: {ProbabilityFor5_10}\n")
    File.write(f"Sixes: {NrOf5_10}, probability: {ProbabilityFor6_10}\n")
    File.write("\n")

    File.write("Number of rolls: 100\n")
    File.write(f"Ones: {NrOf1_100}, probability: {ProbabilityFor1_100}\n")
    File.write(f"Twos: {NrOf2_100}, probability: {ProbabilityFor2_100}\n")
    File.write(f"Threes: {NrOf3_100}, probability: {ProbabilityFor3_100}\n")
    File.write(f"Fours: {NrOf4_100}, probability: {ProbabilityFor4_100}\n")
    File.write(f"Fives: {NrOf5_100}, probability: {ProbabilityFor5_100}\n")
    File.write(f"Sixes: {NrOf5_100}, probability: {ProbabilityFor6_100}\n")
    File.write("\n")

    File.write("Number of rolls: 1000\n")
    File.write(f"Ones: {NrOf1_1000}, probability: {ProbabilityFor1_1000}\n")
    File.write(f"Twos: {NrOf2_1000}, probability: {ProbabilityFor2_1000}\n")
    File.write(f"Threes: {NrOf3_1000}, probability: {ProbabilityFor3_1000}\n")
    File.write(f"Fours: {NrOf4_1000}, probability: {ProbabilityFor4_1000}\n")
    File.write(f"Fives: {NrOf5_1000}, probability: {ProbabilityFor5_1000}\n")
    File.write(f"Sixes: {NrOf5_1000}, probability: {ProbabilityFor6_1000}\n")
    File.write("\n")

    File.write("Number of rolls: 10000\n")
    File.write(f"Ones: {NrOf1_10000}, probability: {ProbabilityFor1_10000}\n")
    File.write(f"Twos: {NrOf2_10000}, probability: {ProbabilityFor2_10000}\n")
    File.write(f"Threes: {NrOf3_10000}, probability: {ProbabilityFor3_10000}\n")
    File.write(f"Fours: {NrOf4_10000}, probability: {ProbabilityFor4_10000}\n")
    File.write(f"Fives: {NrOf5_10000}, probability: {ProbabilityFor5_10000}\n")
    File.write(f"Sixes: {NrOf5_10000}, probability: {ProbabilityFor6_10000}\n")
    File.write("\n")

    File.write("Number of rolls: 100000\n")
    File.write(f"Ones: {NrOf1_100000}, probability: {ProbabilityFor1_100000}\n")
    File.write(f"Twos: {NrOf2_100000}, probability: {ProbabilityFor2_100000}\n")
    File.write(f"Threes: {NrOf3_100000}, probability: {ProbabilityFor3_100000}\n")
    File.write(f"Fours: {NrOf4_100000}, probability: {ProbabilityFor4_100000}\n")
    File.write(f"Fives: {NrOf5_100000}, probability: {ProbabilityFor5_100000}\n")
    File.write(f"Sixes: {NrOf5_100000}, probability: {ProbabilityFor6_100000}\n")
    File.write("\n")
"""