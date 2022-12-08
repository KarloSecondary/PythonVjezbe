#Vježba3_Zadatak1 Karlo Hasnek 31.10.

x = int(input("Unesite x koordinatu: "))
y = int(input("Unesite y koordinatu: "))

if x>0 and y>0:
    print("Točka (%d , %d) se nalazi u 1. kvadrantu" %(x,y))
elif x<0 and y>0:
    print("Točka (%d , %d) se nalazi u 2. kvadrantu" %(x,y))
elif x<0 and y<0:
    print("Točka (%d , %d) se nalazi u 3. kvadrantu" %(x,y))
else:
    print("Točka (%d , %d) se nalazi u 4. kvadrantu" %(x,y))
