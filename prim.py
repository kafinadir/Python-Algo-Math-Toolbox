print("|____________________ NP ____________________|")
print("|________tester un nombre est premier________|")
print()

re = '1'

while re == '1':
    nombre = int(input("entree un nombre ici : "))
    print()

    i = 2
    while i < nombre and nombre % i != 0:
        i = i + 1

    if i == nombre:
        print(nombre, "est un nombre premier !")
    else:
        print(nombre, "n'est pas un nombre premier !")
    print()
    print()
    print()
    print("|__________________ By kafi __________________|")
    print()
    re = input("Tapez '1' pour repetez le programme ou '0' pour quittez : ")