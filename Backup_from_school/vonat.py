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
print("3.feladat")
legtobb={"állásidő":menetrend[1][1]["Indulás"]-menetrend[1][1]["Érkezés"],"vonat":1,"állomás":1}
for vonat in menetrend:
    for állomás in range(1,len(menetrend[vonat])-1):
        if menetrend[vonat][állomás]["Indulás"]-menetrend[vonat][állomás]["Érkezés"]>legtobb["állásidő"]:
            legtobb["állásidő"] = menetrend[vonat][állomás]["Indulás"]-menetrend[vonat][állomás]["Érkezés"]
            legtobb["vonat"]=vonat
            legtobb["állomás"]=állomás
print("A(z)", legtobb["vonat"],"vonat a(z)",legtobb["állomás"],"állomáson", legtobb["állásidő"],"percet ált")