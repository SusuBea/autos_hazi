import random
huzott_szamok = []


def lotto_szamok():
    i = 0
    szamok_str = ""
    while i < 5:
        vel = int(random.random() * 90) + 1
        huzott_szamok.append(vel)
        if i == 4:
            szamok_str += str(vel)
        else:
            szamok_str += str(vel) + "-"
        i += 1
    print("II/ A,B,C: ")
    print(f"\t {szamok_str}")


def egyjegyuek_szama():
    i = 0
    egyjegyu_db = 0
    while i < len(huzott_szamok):
        if huzott_szamok[i] < 10:
            egyjegyu_db += 1
        i += 1
    return egyjegyu_db

def konzol_kiir():
    print("II/D,E: ")
    print(f"\t Az egyjegyuek száma: {egyjegyuek_szama()}.")

def fajl_kiir():
    fajlom = open("szamok.txt", "w", encoding="utf-8")
    fajlom.write(f"A szamok.txt tartalma: \n    II/F:\n\tA fejek szám: {egyjegyuek_szama()}")
    fajlom.close()











