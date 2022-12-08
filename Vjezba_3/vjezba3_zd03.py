#Vježba3_Zadatak3 Karlo Hasnek 31.10.

a = int(input("Unesite 1. cijeli broj: "))
b = int(input("Unesite 2. cijeli broj: "))
operator = input("Unesite jednu od računskih operacija (+, -, * ili /): ")

if operator == '+':
    print("Zbroj zadanih brojeva iznosi:",a+b)
elif operator == '-':
    print("Razlika zadanih brojeva iznosi:",a-b)
elif operator == '*':
    print("Umnožak zadanih brojeva iznosi:",a*b)
elif operator == '/':
    print("Kvocijent zadanih brojeva iznosi:",a/b)
else:
    print("Računska operacija je krivo unešena! Pokušajte ponovno")
