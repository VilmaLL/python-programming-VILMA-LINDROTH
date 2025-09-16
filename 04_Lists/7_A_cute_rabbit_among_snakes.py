import matplotlib.pyplot as plt
import random

# Antal simuleringar att testa
NrOfSimulations = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6]

# Listor för att lagra resultat
ProportionWinsSwitch = []
ProportionWinsStay = []

# Funktion för att köra simuleringar
def run_simulation(n, switch):
    win = 0
    for _ in range(n):
        Doors = [1, 2, 3]
        DoorWithRabit = random.choice(Doors)
        PickedDoor = random.choice(Doors)
        OpenDoor = random.choice([door for door in Doors if door != PickedDoor and door != DoorWithRabit])
        RemainingDoor = [door for door in Doors if door != PickedDoor and door != OpenDoor]
        if switch:
            PickedDoor = RemainingDoor[0]
        if PickedDoor == DoorWithRabit:
            win += 1
    return win / n

# Kör simuleringar för båda strategierna
for N in NrOfSimulations:
    ProportionWinsSwitch.append(run_simulation(N, switch = True))
    ProportionWinsStay.append(run_simulation(N, switch = False))

# Plotta resultaten
plt.figure(figsize = (10, 6))
plt.plot(NrOfSimulations, ProportionWinsSwitch, marker = 'o', color = 'green', label = 'Switch')
plt.plot(NrOfSimulations, ProportionWinsStay, marker = 'o', color = 'red', label = 'Stay')
plt.xscale('log')
plt.xlabel("Number of Simulations")
plt.ylabel("Proportion of Wins")
plt.title("Monty Hall Simulation")
plt.legend()
plt.grid(True)
plt.show()
