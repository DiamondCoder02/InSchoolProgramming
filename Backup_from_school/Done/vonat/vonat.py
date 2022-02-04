menetrend={}
with open("vonat.txt", "r") as ff:
    for sor in ff:
        adatok=sor.strip().split()
        for i,item in enumerate(adatok):
            if i!=4:
                adatok[i]=int(item)
        if adatok[0] not in menetrend:
            menetrend[adatok[0]]={}
        if adatok[1] not in menetrend[adatok[0]]:
            menetrend[adatok[0]][adatok[1]]={}
        if adatok[4]=="I":
            menetrend[adatok[0]][adatok[1]]["Indulás"]=adatok[2]*60+adatok[3]
        else:
            menetrend[adatok[0]][adatok[1]]["Érkezés"]=adatok[2]*60+adatok[3]
print(menetrend)
print("\n2.feladat")
print("Az állomások száma:", len(menetrend[1]))
print("A vonatok száma:", len(menetrend))
print("\n3.feladat")
legtobb={"állásidő":menetrend[1][1]["Indulás"]-menetrend[1][1]["Érkezés"],"vonat":1,"állomás":1}
for vonat in menetrend:
    for állomás in range(1,len(menetrend[vonat])-1):
        if menetrend[vonat][állomás]["Indulás"]-menetrend[vonat][állomás]["Érkezés"]>legtobb["állásidő"]:
            legtobb["állásidő"] = menetrend[vonat][állomás]["Indulás"]-menetrend[vonat][állomás]["Érkezés"]
            legtobb["vonat"]=vonat
            legtobb["állomás"]=állomás
print("A(z)", legtobb["vonat"],"vonat a(z)",legtobb["állomás"],"állomáson", legtobb["állásidő"],"percet ált")
print("\n4.feladat")
bevonat=int(input("Adjon meg egy vonat azonosítóját!"))
oraperc=input("Adjon meg egy időpontot (óra perc) !")
print("\n5.feladat")
eloirt=2*60+22
elteres=eloirt-(menetrend[bevonat][len(menetrend[bevonat])-1]["Érkezés"]-menetrend[bevonat][0]["Indulás"])
if elteres<0:
    print("A(z) {}.vonat útja".format(bevonat), abs(elteres), "perccel rövidebb volt az előírtnál")
elif elteres==0:
    print("A(z)", bevonat, ". vonat utja pontosan az előírt ideig tartott.")
else:
    print("A(z)",bevonat,". vonat útja ", abs(elteres), " perccel hosszabb volt az előírtnál")
#6.feladat
def valto(x):
    return str(x//60)+":"+str(x%60)
fajlnev="halad"+str(bevonat)+".txt"
with open(fajlnev,"w",encoding="utf-8") as halad:
    for állomás in range(1, len(menetrend[bevonat])):
        print(állomás,". állomás:", valto(menetrend[bevonat][állomás]["Érkezés"]), file=halad)
print("7. feladat")
idopont=int(oraperc.split()[0])*60+int(oraperc.split()[1])
for vonat in menetrend:
    if menetrend[vonat][0]["Indulás"]<menetrend[vonat][1]["Érkezés"]:
        print("A(z)", vonat, ". vonat a 0. és az 1. állomás között járt.")
    for állomás in range(1, len(menetrend[vonat])-1):
        if menetrend[vonat][állomás]["Érkezés"]<=idopont<=menetrend[vonat][állomás]["Indulás"]:
            print("A(z)", vonat, "vonat a",állomás,". állomáson állt")
        if menetrend[vonat][állomás]["Indulás"]<idopont<menetrend[vonat][állomás+1]["Érkezés"]:
            print("A(z)", vonat, "vonat a",állomás,"és a ",állomás+1,". állomás között járt")