Värde = int(input("Ange värde: "))

def Cash(Värde):

    Antal1000 = int(Värde / 1000)
    Värde = Värde - (Antal1000 * 1000)
    Antal500 = int(Värde / 500)
    Värde = Värde - (Antal500 * 500)
    Antal200 = int(Värde / 200)
    Värde = Värde - (Antal200 * 200)
    Antal100 = int(Värde / 100)
    Värde = Värde - (Antal100 * 100)   
    Antal50 = int(Värde / 50)
    Värde = Värde - (Antal50 * 50)
    Antal20 = int(Värde / 20)
    Värde = Värde - (Antal20 * 20)
    Antal10 = int(Värde / 10)
    Värde = Värde - (Antal10 * 10)
    Antal5 = int(Värde / 5)
    Värde = Värde - (Antal5 * 5)
    Antal2 = int(Värde / 2)
    Värde = Värde - (Antal2 * 2)
    Antal1 = int(Värde / 1)
    Värde = Värde - (Antal1 * 1)

    print(f"{Antal1000}st 1000-lapp\n {Antal500}st 500-lapp\n {Antal200}st 200-lapp\n {Antal100}st 100-lapp\n {Antal50}st 50-lapp\n {Antal20}st 20-lapp\n {Antal10}st 10-krona\n {Antal5}st 5-krona\n {Antal2}st 2-krona\n {Antal1}st 1-krona")
    return

Cash(Värde)
