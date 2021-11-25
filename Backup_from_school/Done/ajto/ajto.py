print("\n1.feladat")
with open("ajto.txt") as ff:
    codes=[code.strip() for code in ff]

print("\n2.feladat")
from_user=input("Adja meg mi nyitja a zárat!")

print("\n3.feladat")
print("A nyitó kódszámok sorai: ", end="")
for index, from_u in enumerate(codes):
    if from_u == from_user:
        print(index+1, end="")
        
print("\n4.feladat")
for index, from_u in enumerate(codes):
    if len(from_u) !=len(set(from_u)):
        print("Az első ismétlődést tartalmazó próbálkozás sorszáma: ", index+1)
        break
    else:
        print("Nem volt ismétlödő számjegy")
        
print("\n5.feladat")
import random
random.seed()
length=len(from_u)-1
r_code=random.sample("0123456789", length)
print('egy', length, 'hosszú kódszám: ', "".join(r_code))

print("\n6.feladat")
def nyit(good,test):
    egyezik=len(good)==len(test)
    if egyezik:
        elteres=ord(good[0])-ord(test[0])
        for i in range(1,len(good)):
            if (elteres-(ord(good[i]))-ord(test[i]))%10!=0:
                egyezik=False
                break
    return egyezik

print("\n7.feladat")
with open("siker.txt","w") as ff:
    for kod in codes:
        if (len(kod)!=len(from_user)):
            ff.write(from_user+"Hibás hossz\n")
        else:
            if nyit(kod,from_user):
                ff.write(kod+"sikeres\n")
            else:
                ff.write(kod+"Hibás kódszám\n")