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
print("\n4.feladat")

print("\n5.feladat")

print("\n6.feladat")