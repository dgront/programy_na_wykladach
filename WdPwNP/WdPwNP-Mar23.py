# ---------- operacje na plikach
#  - otwieranie, "w" i "r"
#  - zapis przez print() i write()
f = open("plik.txt", "w")
f.write("ala ma kota\n")
f.write("zuza ma psa\n")
print("Alice ma chomika", file=f)
f.write("-------\n")
f.close()

#  - read(), iterowanie, readline(), readlines()
f = open("plik.txt")
#zawartosc = f.read()
# lista_linii = f.readlines()
# for linia in lista_linii:
#     print(linia)
# f.close()

#  - with open() as ..
# with open("plik.txt") as f:
#     for linia in f:
#         print(linia)
# tutaj Python sam zamyka plik

#  - operacje na ścieżkach, katalogach i plikach:
#    - glob.glob(), os.path.join, Path, shutils
katalog = "fasta_folders"
import os
from pathlib import Path
for subfolder in ["1A", "1B", "F3"]:
    name = os.path.join(katalog, subfolder, "plik.fasta")
    print(name)
    print(os.path.dirname(name))
p = Path("../", "1A", "1B", "F3")
print(p, p.exists())

from glob import glob
# l = glob("../src.git/bioshell4/bioshell-taxonomy/src/*.rs")
# print(l)
# pliki .csv
import csv
fname = os.path.join("/Users/dgront/tmp", "plik.csv")
print(fname)
f = open(fname)
for record in csv.reader(f):
        print(record)

# operacje na napisach
realna = float("3")
calk = int(" 3 ")
#  - strip(), split(), find(), replace(), startswith()
n = " 3.4 ".strip()
print(f">{n}<")
wynik = "C         3       5.26".split()
print(wynik)
wynik = "C,3,5.26".split(",")
print(wynik)

for line in open(fname):
    if line.find("C") >= 0:
        print(line)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista[2] += 3
napis = "Alice ma chomika"
# napis[4] = "A"
i_od = 2
i_do = -2
# print(napis[i_od: i_do])

k = 3
for i in range(len(napis) - k):
    print(napis[i:i + k])

#lista = [i for i in range(40) if i%3 != 0 and i%7 != 0 and i%2==0]
#print(lista)

path = "/Users/dgront/tmp/try_python/*.fasta"
wynik = [p for p in glob(path) if "domain" in [line.strip() for line in open(p).readlines()]]
print(wynik)
# miscellanea
#  - lista[-1], napis[-3], napis[2:9], napis[2, -2], napis[i:j]
#  - [k for k in range(100) if k%7==0]
# l = [f for f in glob.glob("*.fasta") if "domain" in [l.strip() for l in open(f).readlines()]]



# enumerate
# Dict