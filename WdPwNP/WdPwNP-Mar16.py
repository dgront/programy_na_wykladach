import random, math

# ---------- Wyrażenie listowe
lista_30_zer = [0 for j in range(30)]
lista_parzystych = [j*2 for j in range(30)]

zagadka = [[0 for j in range(4)] for i in range(4)]
print(zagadka)

# ---------- Korzystanie z matplotlib
from matplotlib import pyplot as plt
x = [i/180.0* math.pi for i in range(0,360) ]
y = [math.sin(xi) for xi in x]
plt.plot(x, y, c="red")
plt.show()
#plt.savefig("plot.pdf")

# Funkcje: deklarowanie
def nazwa_funkcji():
    return 0
# przykład funkcji bezargumentowej
random.random()
print(nazwa_funkcji())

# def do_kwadratu(x):
#     return x*x

# Funkcje: zmienne lokalne i globalne
suma = 1234567890
def wypisz_liczby_od_do(od, do):
    suma = 0
    for i in range(od, do+1):
        suma += i
        print(i, end=" ")
    print("\nSuma =", suma)

wynik = wypisz_liczby_od_do(1, 4)
print("\nSuma po funkcji =", suma)
print(wynik) # Drukuje: None



