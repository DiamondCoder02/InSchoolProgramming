print("1.feladat")
fájlnév=input("Adja meg a bemeneti fájl nevét!")
sor=int(input("Adja meg egy sor számát!"))
oszlop=int(input("Adja meg egy oszlop számát!"))
bemenet=open(fájlnév,"r")
tablazat=[]
for i in range(9):
	adatsor=bemenet.readline().strip().split()
	adatok=[int(elem) for elem in adatsor]
	tablazat.append(adatok)
lepes=[]
for adatsor in bemenet:
	adatok=[int(elem) for elem in adatsor.strip().split()]
	lepes.append(adatok)
print("3.feladat")
if tablazat[sor-1][oszlop-1]==0:
	print("Az adott helyet még nem töltötték ki.")
else:
	print("Az adott helyen szereplő szám:",tablazat[sor-1][oszlop-1])
print("A hely a(z)",3*((sor-1)//3)+((oszlop-1)//3)+1,"résztáblához tartozik")