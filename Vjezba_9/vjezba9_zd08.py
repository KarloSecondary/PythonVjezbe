#vjezba9_zd8 Karlo Hasnek 23/12/2022
# '~' = '\n'

indeksi = {}


def intro():
    print(60*'-')
    print('Program za kompresiju/dekompresiju podataka'.center(60, '-'))
    print(60 * '-')
    print('1. Morate unijeti naziv .txt datoteke koju biste htjeli obraditi')
    print('Prvi korak je moguće preskočiti pritiskom tipke Enter. Default = ulaz8.txt')
    print('2. Imenujte izlazni file (ako je ime već zauzeto obrađena datoteka se sprema pod imenom "untitled.txt")')
    print('3. Odaberite radnju (kompresija/dekompresija) podataka')
    print(60 * '-')


def kompresija(f, f2):
    linije = f.readlines()
    s = ''.join(i for i in linije)

    for i in linije:
        for j in i:
            indeksi[j] = [index for index, char in enumerate(s) if char == j]

    for key, value in indeksi.items():
        if key == '\n':
            key = '~'
        f2.write(f'{key}\n{value}\n')

    f.close()
    f2.close()


def dekompresija(f, f2):
    dict_vrij = {}
    linije = f.readlines()
    for i in range(len(linije)):
        if i % 2 == 0:
            pocetak_liste = linije[i+1].index('[')
            kraj_liste = linije[i+1].rindex(']', 0, len(linije[i+1]))
            lista = (linije[i+1][pocetak_liste:kraj_liste+1])
            dict_vrij[linije[i][0]] = broj(lista)

        else:
            continue
    return ispis(dict_vrij, f2)


def ispis(dict_vrij, f2):
    brojac = 0
    for i in dict_vrij.values():
        for j in i:
            brojac += 1
    indeks = 0
    done = False
    while not done:
        for value in dict_vrij.values():
            for v in value:
                if v == indeks:
                    key = get_key(v, dict_vrij)
                    if key == '~':
                        key = '\n'
                    f2.write(f'{key}')
                    indeks += 1
                if indeks == brojac:
                    done = True


def get_key(val, dict_vrij):
    for key, value in dict_vrij.items():
        for v in value:
            if val == v:
                return key


def broj(lista):
    lista_brojeva = []
    string_broja = ''
    for j in lista:
        if j.isnumeric() or 0:
            string_broja += j
        elif string_broja != '':
            lista_brojeva.append(int(string_broja))
            string_broja = ''

    return lista_brojeva


def main():
    intro()

    ulazni_name = input('Unesite naziv ulazne datoteke (bez ekstenzije): ')
    name_choice = input('Odaberite naziv izlazne datoteke (bez ekstenzije): ')
    if ulazni_name != '':
        try:
            f = open(f'./{ulazni_name}.txt', 'r', encoding="utf8")
        except FileNotFoundError:
            f = open('./ulaz8.txt', 'r', encoding="utf8")
    else:
        f = open('./ulaz8.txt', 'r', encoding="utf8")
    if True:
        try:
            f2 = open(f'./{name_choice}.txt', 'x', encoding="utf8")
        except FileExistsError:
            f2 = open(f'./untitled.txt', 'x', encoding="utf8")

    type_choice = input('Upišite 1 za kompresiju ili 2 za dekompresiju: ')
    if type_choice == '1':
        return kompresija(f, f2)
    elif type_choice == '2':
        return dekompresija(f, f2)
    else:
        print('Error pri 3. koraku: unesena je vrijednost različita od 1 ili 2.')
        print('Pokrenite program ponovno.')
        exit()


main()
