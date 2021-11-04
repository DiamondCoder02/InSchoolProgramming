#-*- coding:utf-8 -*-
print("\n1.feladat")
with open("penztar.txt") as ff:
 kosarak=[]
 kosar=[]
 for aru in ff:
    aru=aru.strip()
    if aru=="F":
        kosarak.append(kosar)
        kosar=[]
    else:
        kosar.append(aru)

print("\n2.feladat")
print("A fizetések száma:", len(kosarak))

print("\n3.feladat")
print("Az első vásárlő", len(kosarak[0]), "darab árucikket vásárolt.")

print("\n4.feladat")
sorszam=int(input("Adja meg egy vásárlás sorszámát!"))
arucikk=input("Adja meg az árucikk nevét!").strip()
darab=int(input("Adja meg a vásárolt darabszámot!"))

print("\n5.feladat")
kosarvalogatas=[(index,kosar) for (index, kosar) in enumerate(kosarak) if arucikk in kosar]
print("Az első vásárlás sorszáma:", kosarvalogatas[0][0]+1)
print("Az utolsó vásárlás sorszáma:", kosarvalogatas[-1][0]+1)
print(len(kosarvalogatas), "vásárlás során vettek belőle.")

print("\n6.feladat")
def ertek(db):
    if db==1:
        return 500
    elif db==2:
        return 950
    return 950+(db-2)*400
print(darab, "darab vételekor fizetendő:", ertek(darab))

print("\n7.feladat")
termekek=dict()
for kacat in kosarak[sorszam-1]:
    termekek[kacat]=termekek.get(kacat,0)+1
for kacat in termekek:
    print(termekek[kacat], kacat)

#8.feladat
print("\n8.feladat")
with open("osszeg.txt","w") as ff:
    for index, kosar in enumerate(kosarak):
        termekek2=dict()
        for kacat in kosar:
            termekek2[kacat]=termekek2.get(kacat,0)+1
        osszeg=0
        for kacat in termekek2:
            osszeg+=ertek(termekek2[kacat])
        ff.write(str(index+1)+":"+str(osszeg)+"\n")