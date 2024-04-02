cars = ["Ford", "Volvo", "BMW", "Audi"]

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"Auto s číslem {x+1}: {prvek[x]}")
        print(" ")

prvek_plus = input("Zadejte auto, které chcete přidat: ")

cars.append(prvek_plus)
vypis_pole(cars)

prvek_minus = int(input("Jakou pozici chcete odebrat? "))

cars.pop(prvek_minus)
vypis_pole(cars)