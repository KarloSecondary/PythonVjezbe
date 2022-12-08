for i in "xy":
    for j in "xy":
        for k in "xy":
            for l in "xy":
                par = i+j+k+l
                if par.count("y") == 0:
                    print(par)
                if par.count("y") == 1:
                    print(par, end=" ")
                if par.count("y") == 2:
                    print(end=par, sep=" ")
                if par.count("y") == 3:
                    print(end=par, sep=" ")
                if par.count("y") == 4:
                    print(end=par, sep=" ")