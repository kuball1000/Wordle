def zielone_L(string, lista):
    string = string.lower()
    for index, litera in enumerate(string):
        # print(index, litera)
        if litera != "0":
            lista = [slowo for slowo in lista if slowo[index] == litera]
    return lista

def zolte_L(string, lista):
    string = string.lower()
    for index, litera in enumerate(string):
        if litera != "0":
            lista = [slowo for slowo in lista if slowo[index] != litera and litera in slowo ]
    return lista

def szare_L(string, lista):
    string = string.lower()
    szare_litery = [*string]
    lista2 = []
    for slowo in lista:
        if all(litera not in slowo for litera in szare_litery):
            lista2.append(slowo)
    return lista2

file = open("slowa.txt", "r", encoding='utf8')
lista_slow = file.readlines()
file.close()
lista_slow = [slowo.replace("\n", "") for slowo in lista_slow if len(slowo) == 6]


def literalnie(lista, zielone: str = "00000", zolte: str = "00000", szare: str = ""):

    lista = zielone_L(zielone, lista)
    lista = zolte_L(zolte, lista)
    lista = szare_L(szare, lista)
    return lista


print(literalnie(lista_slow, "I000A", "00000", "DWKE"))


