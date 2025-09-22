NameList = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]

def Cleaning(Name):
    Name = Name.strip().title()
    return Name

for Name in NameList:
    print(Cleaning(Name))

