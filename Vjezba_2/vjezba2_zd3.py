#vjezba2_zd3 Karlo Hasnek 25/10/2022

centimetri = int(input("Unesite duljinu u centimetrima: "))
inci_total = centimetri / 2.54
stope = int(inci_total // 12)
inci = inci_total - stope*12
print("Duljina od %d cm odgovara duljini od %d stopa i %d inča" %(centimetri,stope,inci))
