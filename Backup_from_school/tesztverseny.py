print("\n1.feladat: Az adatok beolvasása.")
with open("valaszok.txt") as ff:
    megoldasok=next(ff).strip()
    eredmenyek=[]
    for sor in ff:
        eredmenyek.append(sor.split())
print('\n2.feladat: A vetélkedőn {} versenyző indul.'.format(len(eredmenyek)))
be_kod=input("\n3.feladat: A versenyző azonosytója = ").strip()
be_valasz=None
for szkod,szvalasz in eredmenyek:
    if be_kod  == szkod:
        be_valasz =szvalasz
        break
print(be_valasz + " (A versenyző válasza)")
print("\n4.feladat:")
print("{} \t(A helyes megoldás)".format(megoldasok))
helyes=""
for i,jel in enumerate(megoldasok):
    helyes+="+" if jel==be_valasz[i] else " "
print(helyes + " \t(A versenyző helyes válaszai)")
fsorszam=int(input("\n5.feladat: A feladata sorszáma = "))-1
jovalasz=0
jojel=megoldasok[fsorszam]
for szkod,szvalasz in eredmenyek:
    if szvalasz[fsorszam]==jojel:
        jovalasz+=1
print("A feladatra {} fő, a versenyzők {}%-a adott helyes választ".format(jovalasz, round(jovalasz*100/len(eredmenyek),2)))
print("\n6.feladat: A versenyzők pontszámának meghatározása")
def fpontok(megoldasok, szvalasz):
    pont=[3,3,3,3,3,4,4,4,4,4,5,5,5,6]
    ossz=0
    for i,jel in enumerate(megoldasok):
        if jel==szvalasz[i]:
            ossz+=pont[i]
    return ossz
with open("pontok.txt","w") as ff:
    for i, (szkod, szvalasz) in enumerate(eredmenyek):
        pontszam=fpontok(megoldasok, szvalasz)
        ff.write("{} {}\n".format(szkod,pontszam))
print("\n7.feladat: A verseny legjobbjai.")
def hasonlit(adat):
    szkod,szvalasz,pontszam=adat
    return pontszam
eredmenyek.sort(key=hasonlit, reverse=True)
dij=1
elozopsz=eredmenyek[0][2]
for szkod,szvalasz,pontszam in eredmenyek:
    if pontszam<elozopsz:
        dij+=1
        elozopsz=pontszam
    if dij>3:
        break
    print("{}. díj ({} pont) {}".format(dij,pontszam,szkod))