l = []
m = int(input("unesi m broj: "))
n = int(input("unesi n broj: "))
if m>0 and n>0:
    for i in range(1,m+1):
        l.append(i/n)
else:
    print("Jedan od zadanih brojeva je ili negativan ili nula.")
print(l)
print(sum(l))
