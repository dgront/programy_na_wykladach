from math import pow
from typing import List


def reverse_list(input: List):
    return input.reverse()


def dodaj(factor: float, *zupa, **grzybowa) -> float:

    """Zwraca sumę wszystkich argumentów podniesionych
do potęgi exp i pomnożoną przez factor.

Wykładnik 'exp' przekazywany jest jako kwargs.
    """
    suma = 0
    exp = grzybowa.get("exp", 1.0)
    for x in zupa:
        suma += pow(x, exp)
    print(grzybowa)

    return suma*factor

if __name__ == "__main__":
    print("testuję ...")
    if dodaj(0.5, 1,2,3, 4, 5, 6, eksp=10.0) != 10.5:
        print("nie działa!")