room=[]
file=open("ajto.txt")
for data in file:
    room.append(data.strip('\n'))
    
print("2. feladat")
print("Az első belépő: " +room[0].split(' ')[2])
a=len(room)
for i in range(a-1,0,-1):
    if room[i].split(' ')[3]=="ki":
        print("Az utolsó kilépő: " +room[i].split(' ')[2])
        break

print("3. feladat")
file2=open("athaladas.txt","w")
move=[]
for i in range(0, 101, 1):
    move.append(0)
for i in room:
    num=int(i.split(' ')[2])
    move[num]=move[num]+1
for i in range(0,101,1):
    if move[i]!=0:
        file2.write(str(i)+" "+str(move[i])+"\n")

print("4. feladat")
print("A végén a társalgóban voltak:")
for i in range(0, 101, 1):
    if move[i]%2==1:
        print(str(i)+" ", end="")

print("\n5. feladat")
max=0
hour="9"
min="0"
inroom=0
for i in room:
    if i.split(" ")[3]=="be":
        inroom=inroom+1
    if i.split(" ")[3]=="ki":
        inroom=inroom-1
    if inroom>max:
        max=inroom
        hour=i.split(" ")[0]
        min=i.split(" ")[1]
print(hour, ":", min, "kor voltak a legtöbben a társalgóban.")