#vjezba4_zd11 Karlo Hasnek 08/11/2022

import random

#Nasumični generator "ABC" stringa proizvoljne dužine
print("Ovaj program računa udio slova unutar nasumično generiranog stringa")
length = int(input("Unesite duljinu stringa: "))
letters = 'ABC'
sequence = ''.join(random.choice(letters) for i in range(length))
print("Nasumično generirani string:", sequence)

#Manual input
#sequence = str(input("Unesite niz koji se sastoji od slova A,B ili C: "))

sequence_length = len(sequence)
kol_A, kol_B, kol_C = sequence.count("A"), sequence.count("B"), sequence.count("C")
part_A, part_B, part_C = round(kol_A/sequence_length*100, 2), round(kol_B/sequence_length*100, 2), round(kol_C/sequence_length*100, 2)
print("\nPostotak pojavljivanja slova A je:", part_A, "%")
print("Postotak pojavljivanja slova B je:", part_B, "%")
print("Postotak pojavljivanja slova C je:", part_C, "%\n")

#Sortiranje u tip 'String'
sorted_letters = sorted(sequence)
sorted_sequence = ''.join(sorted_letters)
print("Generirani string sortiran u tip 'String':", sorted_sequence)

#Sortiranje u tip 'List'
sorted_sequence = sorted(sequence)
print("Generirani string sortiran u tip 'List':", sorted_sequence)
