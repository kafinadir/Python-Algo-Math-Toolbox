nombre = 2
a = 0
while nombre <= 10000:
    i = 2
    while i < nombre and nombre % i != 0:
        i = i + 1

    if i == nombre:
        print(nombre)
        a = a+1
    nombre += 1
print()
print("le nombre de nb prim inferieur a 10000 est", a)
print()
print("|__________________ By kafi __________________|")
print()
