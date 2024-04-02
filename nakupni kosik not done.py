zbozi = ["CPU(0)", "GPU(1)", "RAM(2)", "Motherboard(3)", "Zdroj(4)"]
kosik = []

print(zbozi)
print("Vyberte zboží které si chcete přidat do košíku: ")

vyber = int(input())

kosik.append(vyber(zbozi))
zbozi.pop(vyber)
print(kosik)
print(zbozi)
