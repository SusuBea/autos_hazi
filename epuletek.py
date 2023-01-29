from Auto import Auto
autok_lista = []

def faljbeolvasas():
    fajlom = open("auto.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    fajltartalom = fajlom.readlines()
    fajlom.close()
    i = 0
    while i < len(fajltartalom):
        sor = fajltartalom[i].strip().split("$")
        autok_lista.append(Auto(sor))
        i += 1


def flotta():
    print("III/Flotta: ")
    print(f"\tAutók száma: {len(autok_lista)}.")

def legfiatalabb():
    i = 0
    leg = 0
    while i < len(autok_lista):
        if autok_lista[leg].gyartasi_datum > autok_lista[i].gyartasi_datum:
            leg = i
        i += 1
    return f"\t A legfiatalabb autó: {autok_lista[leg].nev}({autok_lista[leg].gyartasi_datum})"








