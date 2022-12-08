s = str(input("Unesi string: "))
s = [*s]
for i in range(len(s)):
    if s[i] == s[i].lower():
        s[i] = s[i].upper()
    elif s[i] == s[i].upper():
        s[i] = s[i].lower()
s = ''.join(s)
razmak = s.count(" ")
tocka = s.count(".")
zarez = s.count(",")
print(s)
print(razmak, tocka, zarez)