from time import sleep

f = open('./test.txt', 'r')

for i in f:
    print(i)
    sleep(3)
