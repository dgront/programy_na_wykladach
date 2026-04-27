# # Słownik = tablica asocjacyjna = mapa = hash map / tablica haszująca
# import random
#
# # --- przypomnienie o listach
# lista = []          # pusta lista
# for i in range(10): lista.append(i/180.0)
lista = [1, 4, 2, 56, -2, 0, 0, 1, 0]
# print(lista)
#
# sum = 0
# for val in lista:
#     # print(val)
#     sum += val
#
# # --- to samo, ale ze słownikiem
slownik = {}        # pusty slownik
slownik = {"klucz" : 3, "inny klucz": "jest"}
slownik["Frodo"] = "present!"
slownik["Frodo"] = "gone!"
# if "Aragorn" in slownik:
#     print(slownik["Aragorn"])
# else:
#     print("Aragorn poszedł")
# print(slownik)
#
# color_settings = {"fill": "0xaaaaaa", "stroke": "black"}
# # czytanie ze słownika
# if "font-size" in color_settings:
#     print(color_settings["font-size"])
# else:
#     print("12pt")
#
# print(color_settings.get("font-size", "12pt"))
#
# # iteracja po kluczach
# for key in slownik:
#     print(key, slownik[key])
#
# for key in slownik.keys():
#     print(key, slownik[key])
#
# for key_val in slownik.items():
#     print("iteracja dwukrotką:",key_val[0], ":", key_val[1])
#
# for key, val in slownik.items():
#     print("iteracja dwukrotką rozpakowaną:",key, ":", val)
#
# # iteracja po wartościach
# for val in slownik.values():
#     print(val)
#
# # O tupli zwanej krotką - ta immutable lista
# krotka = (1, 2, 3, 4)
#
# print(krotka[3])
# x = krotka[3] + krotka[2] + krotka[1] + krotka[0]
# print(x)
# for ki in krotka: print(ki)
# print(krotka)
# # krotka[0] += 3
# # krotka.append(5.0)
# # --- rozpakujmy krotkę
# a1, a2, a3, a4 = krotka
# print(a3)
import random

# --- Śródziemie
# 1) pusty slownik
zliczenia = {}
fname = "/Users/dgront/src.git/lecture-notes/source/doc/Programowanie2/wykład/trzy_style/lotr1-utf8.txt"
with open(fname) as plik:
# 2) idziemy po linijkach
    for line in plik:
        # 3) dzielimy linijkę na wyrazy
        for znak in ",.;:`-!?&'_()":
            line = line.replace(znak," ")
        wyrazy = line.strip().split()
        for wyraz in wyrazy:    # 4) zliczamy wyrazy, rozpatrując 2 przypadki: pierwsze i kolejne wystąpienie wyrazu
            wyraz = wyraz.lower()
            if wyraz in zliczenia:
                zliczenia[wyraz] += 1
            else:
                zliczenia[wyraz] = 1
# 5) posortować malejąco klucze po zliczeniach
# unikalne_wyrazy = list(zliczenia.keys())
# def krotnosc(k):
#     return zliczenia[k]
# unikalne_wyrazy_sorted = sorted(unikalne_wyrazy, key=krotnosc, reverse=True)
# for w in unikalne_wyrazy_sorted[:100]:
#     print(w, zliczenia[w])

# Lans na `enumerate`
for i, element in enumerate(lista):
    print(i, ":", element)

lista_2 = [v*2.4 - random.random() for v in lista]
# Lans na `zip`
for i, (element1, element2) in enumerate(zip(lista, lista_2)):
    print(i, element1, element2)

# for i, element in enumerate(lista):
#     print(i, ":", element)

# ---- args i kwargs


def moja_fajna_funkcja2(x, y):
    return x*y

def moja_fajna_funkcja3(x, y, z):
    return x*y*z

def moja_fajna_superfunkcja(*zupa, **grzybowa):
    print(grzybowa)
    if len(zupa) == 1 : return zupa[0] * zupa[0]
    iloczyn = 1
    for v in zupa: iloczyn*=v
    return iloczyn / grzybowa["norm"]


moja_fajna_superfunkcja(1, 2, 3, 4, 5, 6, 7, 8, norm=6.0)