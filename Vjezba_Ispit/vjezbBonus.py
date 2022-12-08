a1=''
a2=''
a3=''
a4=''
for i in "xy":
    for j in "xy":
        for k in "xy":
            for l in "xy":
                par = i+j+k+l
                if par.count("y") == 0:
                    print(par)
                if par.count("y") == 1:
                    a1=a1+par+' '
                elif par.count("y") == 2:
                    a2=a2+par+' '
                elif par.count("y") == 3:
                    a3=a3+par+' '
                elif par.count("y") == 4:
                    a4=a4+par+' '
print("%s\n%s\n%s\n%s" % (a1, a2, a3, a4))
