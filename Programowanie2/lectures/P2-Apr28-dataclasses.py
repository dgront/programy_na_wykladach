from __future__ import annotations
import dataclasses
import inspect
from dataclasses import dataclass, field

from functools import total_ordering



@total_ordering
class CypIdByClass:
    def __init__(self, family: int, subfamily: str, ortholog: int, variant: int):
        self.__family: int = family
        self.__subfamily: str = subfamily
        self.__ortholog: int = ortholog
        self.__variant: int = ortholog

    @property
    def family(self): return self.__family

    @property
    def subfamily(self): return self.__subfamily

    def __str__(self):
        return f"CYP{self.family}{self.subfamily}{self.ortholog}v{self.__variant}"

    def __eq__(self, other: CypIdByClass):
        if not isinstance(other, CypIdByClass):
            return NotImplemented
        return (self.family, self.subfamily, self.ortholog) == (other.family, other.subfamily, other.ortholog)

    def __lt__(self, other: CypIdByClass):
        if not isinstance(other, CypIdByClass):
            return NotImplemented
        return (self.family, self.subfamily, self.ortholog) < (other.family, other.subfamily, other.ortholog)

    def __hash__(self):
        return hash((self.__class__, self.family, self.subfamily, self.ortholog))


@dataclass(frozen=True, order=True)
class CypId:
    family: int = 1
    subfamily: str = "A"
    ortholog: int = 1
    variant: int | None = None

    def __str__(self):
        if self.variant:
            return f"CYP{self.family}{self.subfamily}{self.ortholog}v{self.variant}"
        else:
            return f"CYP{self.family}{self.subfamily}{self.ortholog}"


def main_class():
    cyp_id = CypIdByClass(1, "A", 2)


def main_dataclass():

    cyp_id2 = CypId(1, "A", 2)
    # cyp_id2.variant = 3
    print(cyp_id2)

    # print(",\n".join(map(str,inspect.getmembers(inspect.getmembers(cyp_id2, inspect.isfunction())))))
    #
    cyp_id = CypId(1, "A", 2)
    # cyp_id.family = 3  # can't modify because it's immutable
    print(cyp_id)
    d = {cyp_id: 2}
    print(dataclasses.astuple(cyp_id))
    print(dataclasses.asdict(cyp_id))
    copy = dataclasses.replace(cyp_id, family=3)
    print(copy)


if __name__ == '__main__':
        main_dataclass()


