Curriculum = {
    "Intro till AI" : 5,
    "Programmering inom Python" : 40,
    "Databehandlingar" : 25,
    "Linjär algebra" : 20,
    "Statistiska metoder" : 30,
    "Maskininlärning" : 45,
    "Databaser" : 25,
    "Dataengineering och agila metoder" : 45,
    "LIA 1" : 40,
    "Djup maskininlärning" : 40,
    "LIA 2" : 70,
    "Examensarbete" : 15
}
Sum = 0
for key, value in Curriculum.items():
    Sum += value

Nr_of_YHP = Sum
print(Nr_of_YHP)