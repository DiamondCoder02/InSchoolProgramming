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
print("\n5.feladat")

print("\n6.feladat")