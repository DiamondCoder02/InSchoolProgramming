utazasok=[]
utazas={}
with open("utasadat.txt","r",encoding="utf-8") as ff:
    for sor in ff:
        adatok=sor.strip().split()
        utazas["megallo"]=int(adatok[0])
        dat_ip=adatok[1].split("-")
        utazas["datum"]=dat_ip[0]
        utazas["idopont"]=dat_ip[1]
        utazas["azonosito"]=adatok[2]
        utazas["tipus"]=adatok[3]
        utazas["ervenyes"]=adatok[4]
        utazasok.append(utazas)
        utazas={}
print(utazasok)
print("2.feladat")
print("A buszra",len(utazasok)," utas akart felszálni")
print("3.feladat")
szamlalo=0
for utazas in utazasok:
    if (utazas["tipus"]!="JGY" and utazas["datum"]>utazas["ervenyes"]) or (utazas["tipus"]=="JGY" and utazas["ervenyes"]=="0"):
        szamlalo+=1
print('A buszra',szamlalo,"utas nem szálhatott fel")
print("4.feladat")
megallok=[]
for index in range(0,30):
    megallok.append(0)
for utazas in utazasok:
    megallok[utazas["megallo"]]+=1
maxutas=max=(megallok)
meg=True
for index, utasok in enumerate(megallok):
    if meg and utasok==maxutas:
        print("A legtöbb utas(", maxutas, " fő) a", index,". megállóban próbált felszálni.")
print("5. feladat")
ingyen=0
kedvezmeny=0
for utazas in utazasok:
    if utazas["datum"]<=utazas["ervenyes"]:
        if utazas["tipus"]=="NYP" or utazas["tipus"]=="RVS" or utazas["tipus"]=="GYK":
            ingyen+=1
        if utazas["tipus"]=="TAB" or utazas["tipus"]=="NYB":
            kedvezmeny+=1
print("Ingyenes utazók száma:", ingyen, "fő")
print("A kedvezményesen utazók száma:", kedvezmeny, "fő")