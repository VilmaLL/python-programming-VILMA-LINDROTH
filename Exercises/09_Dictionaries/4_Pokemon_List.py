
path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\09_Dictionaries\pokemon_list.txt"

with open(path, "r") as file:
    Pokedex = {}
    for line in file:
        Pokemons = line.strip().split(" ")
        if len(Pokemons) == 3:
            pokemon = Pokemons[1].strip()
            type = Pokemons[2].strip()
            index = Pokemons[0].strip()
            Pokedex[pokemon] = type, index

print(Pokedex["Snorlax"])
print(Pokedex)