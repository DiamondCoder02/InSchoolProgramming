print("\n1.feladat")
be=open("melyseg.txt")
melysege=[]
for sor in be:
    melysege.append(int(sor.strip()))
print("A fájl adatainak száma: ", len(melysege))
print("\n2.feladat")
keret=int(input("Adjon meg egy távolság értéke!: "))
print("Ezen a helyen a felszín ",melysege[keret-1], " méter mélyen van.")
print("\n3.feladat")
erintetlen=0
for m in melysege:
    if m==0:
        erintetlen+=1
print("Az érintetlen terület arány: {0:4.2f}%".format(100*erintetlen/len(melysege)))
print("\n4.feladat")
print("\n5.feladat")
print("\n6.feladat")
print("\n7.feladat")