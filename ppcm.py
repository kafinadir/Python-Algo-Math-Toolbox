print("|__________________ PPCM __________________|")
print("|_____ le Plus Petit Commun Multiple ______|")
print()

re = '1'

while re == '1':
    a = int(input("entree le premier nb ici : "))
    print()
    b = int(input("entree le deuxiem nb ici : "))
    print()
    def decomp(n):
        L = dict()
        k = 2
        while n != 1:
            exp = 0
            while n % k == 0:
                n = n // k
                exp += 1
            if exp != 0:
                L[k] = exp
            k = k + 1
        return L

    print("la decomposition en facteur de nombres premiers de a et b est :")
    print()
    print("a = |",decomp(a),"|")
    print()
    print("b = |",decomp(b),"|")
    print()

    def ppcm(a,b):
        Da = decomp(a)
        Db = decomp(b)
        p = 1
        for facteur , exposant in Da.items():
            if facteur in Db:
                exp = max(exposant , Db[facteur])
            else:
                exp = exposant
            p *= facteur**exp
        for facteur , exposant in Db.items():
            if facteur not in Da:
                p *= facteur**exposant
        return p

    print("PPCM({} , {}) =".format(a,b), ppcm(a,b))
    print()
    print()
    print()
    print("|__________________ By kafi __________________|")
    print()
    re = input("Tapez '1' pour repetez le programme ou '0' pour quittez : ")