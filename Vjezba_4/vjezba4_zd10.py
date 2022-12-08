#vjezba4_zd10 Karlo Hasnek 08/11/2022

name_list = []
n = int(input("Unesite broj imena koji zelite unijeti: "))
for i in range(n):
    name = str(input("unesite %d. ime: " % (i+1))).capitalize()
    name_list.append(name)
    name_list.sort()
for name in name_list:
    print("%d. %s" % ((name_list.index(name)+1), name))
