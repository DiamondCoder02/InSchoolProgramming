print("1.feladat")
be=open("melyseg.txt")
melysege=[]
for sor in be:
	melysege.append(int(sor.strip()))
print("A fájl adatainak száma: ",len(melysege))
print("2.feladat")
keret=int(input("Adjon meg egy távolság értéket!"))
print("Ezen a helyen a felszín",melysege[keret-1],"méter mélyen van.")
print("3.feladat")
erintetlen=0
for m in melysege:
    if m==0:
        erintetlen+=1
print("Az érintetlen terület aránya:{0:4.2f}%".format(100*erintetlen/len(melysege)))
kimenet=open("godrok.txt","w")
egysor=[]
sorok=[]
elozo=0
for x in melysege:
    if x >0:
        egysor.append(str(x))
    if x==0 and elozo >0:
        sorok.append(egysor)
        egysor=[]
    elozo=x
for egysor in sorok:
    print(" ".join(egysor),file=kimenet)
kimenet.close()
print("5.feladat")
print("A gödrök száma:",len(sorok))
print("6.feladat")
if melysege[keret-1]>0:
    print("a)")
    poz=keret-1
    while melysege[poz]>0:
        poz-=1
    kezdo=poz+2
    poz=keret
    while melysege[poz]>0:
        poz+=1
    veg=poz
    print("A gödör kezdete:",kezdo,"méter, a gödör vége",veg,"méter.")
    print("b)")
    pont=0
    poz=kezdo
    while melysege[poz]>=melysege[poz-1] and poz<=veg:
        poz+=1
    while melysege[poz]<=melysege[poz-1] and poz<=veg:
        poz+=1
    if poz>veg:
        print("Folyamatosan mélyül")
    else:
        print("Nem mélyül folyamatosan")
    print("c)")
    print("A legnagyobb mélysége",max(melysege[kezdo-1:veg]),"méter.")
    print("d)")
    terfogat=10*sum(melysege[kezdo-1:veg])
    print("A térfogata:",terfogat,"m^3")
    print("e)")
    viz=terfogat-10*(veg-kezdo+1)
    print("A vízmennyiség",viz,"m^3")
else:
    print("Az adott helyen nincs godor.")
    
    
    
    