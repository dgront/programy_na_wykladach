# iterowanie po liście
# instrukcja while
# instrukcja match - case
# print i formatowanie
# obrazki _#_ (choinki)
# sortowanie bąbelkowe

# ---- wypisywanie zawartości tablicy
# lista = [1, 3, 2, 6, 4, 5]
# N = len(lista)
# for i in range(0, N):
#     print(lista[i])

# for w in lista:
#     print(w)

# ---- print
color = 0xfffa12
# print("%x" % (color))
zmienna_d = 5
zmienna_f = 999.123
zmienna_s = "napis"
# print("%05d %8.3f %s" % (zmienna_d, zmienna_f, zmienna_s))
f_string = f"d={zmienna_d:05} a f wynosi: {zmienna_f}"
print(f_string)
# ---- choinki
# import random
# N = 9
# for i in range(N): # wiersze
#     for j in range(N-1-i):
#         print(" ", end="")
#     for j in range(2*i+1): # kolumny
#         if random.random() < 0.2:
#             print("o", end="")
#         else:
#             print("#", end="")
#     print()


# ---- pętla while
# i = 0
# epsilon = 1e-10
# # sumujemy 1/(i*i)
# suma = 0
# wyraz = 1.0
# while wyraz > epsilon:
#     i += 1
#     wyraz = 1.0 / (i*i)
#     suma += wyraz
#     print(i, wyraz)

# ---- match - case
# d = 5
#
# match d:
#     case 1:
#         print("jeden")
#     case 2:
#         print("jeden")
#     case 3:
#         print("jeden")
#     case 4:
#         print("jeden")
#     case _:
#         print("żaden z powyższych")

# ---- sortowanie bąbelkowe
lista = [6, 1, 2, 3, 4, 5]
N = len(lista)
if_needs_sorting = True
j = 0
while if_needs_sorting:
    if_needs_sorting = False
    for i in range(1, N-j):
        # print(i, lista[i-1] > lista[i])
        if lista[i-1] > lista[i]:
            tmp = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = tmp
            if_needs_sorting = True
    j+=1
    print(j)
print(lista)
