#vjezba1_zd5 Karlo Hasnek 18/10/2022

#zadano vrijeme prikazano u sekundama
vrijeme = 876245

#konst = ostatak dijeljenja zadanih sekundi sa konstantom od sekundi u danu
konst = vrijeme % 86400

dani = vrijeme // 86400
sati = int(konst / 3600)
minute = int(konst % 3600 / 60)
#sekunde = int(vrijeme-(dani*86400 + sati*3600 + minute*60))
sekunde = int(konst % 3600 % 60)
print("%d sekundi = %d dana, %d sata, %d minuta i %d sekundi" %(vrijeme,dani,sati,minute,sekunde))
