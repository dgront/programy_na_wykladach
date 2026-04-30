# ------------ standardowy układ programu w Pythonie
# --- własne moduły i importowanie
import re
import sys
from typing import Dict

sys.path.append("/home/dgront/work/p450/")
print(sys.path)
from my_utils import dodaj

if __name__ == "__main__":
    print(dodaj(1,2,3))

# napisy na wiele linii
napis1 = "Ala ma papugę, psa i pin-\ngwina a Ola ma kota i psa."
napis_multi = """Ala ma papugę "Ara", psa i pin-
gwina a Ola ma kota i psa."""
print(napis1)
print(napis_multi)
# ------------ args, kwargs
# ------------ anotacje typów

# wyrażenia listowe, wyrażenia słownikowe, enumerate, zip, lambda
even = [2*i for i in range(1, 10) if i%3 == 0]
slownik: Dict[str, int] \
    = {w:len(w) for w in "Ala ma kota".split()}
# print(slownik)
# ------------ regex
print("----- regex -----")
napis1 = "Ala ma kota"
napis2 = "Ola ma kota"
napis3 = "Ula ma kota"
for napis in [napis3, napis2, napis1]:
    print(re.findall("[A-Z]la", napis))
