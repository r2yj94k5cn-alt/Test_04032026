<<<<<<< HEAD
from __future__ import annotations
from dataclasses import dataclass
from math import hypot, pi


@dataclass
class Punkt:
    x: float
    y: float

    def verschieben(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def distanz_zu(self, anderer: "Punkt") -> float:
        return hypot(self.x - anderer.x, self.y - anderer.y)


class Form:
    def flaeche(self) -> float:
        raise NotImplementedError

    def umfang(self) -> float:
        raise NotImplementedError

    def verschieben(self, dx: float, dy: float) -> None:
        raise NotImplementedError


@dataclass
class Kreis(Form):
    mittelpunkt: Punkt
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("Der Radius muss > 0 sein.")

    def flaeche(self) -> float:
        return pi * self.radius**2

    def umfang(self) -> float:
        return 2 * pi * self.radius

    def verschieben(self, dx: float, dy: float) -> None:
        self.mittelpunkt.verschieben(dx, dy)


@dataclass
class Rechteck(Form):
    links_unten: Punkt
    breite: float
    hoehe: float

    def __post_init__(self) -> None:
        if self.breite <= 0 or self.hoehe <= 0:
            raise ValueError("Breite und Höhe müssen > 0 sein.")

    def flaeche(self) -> float:
        return self.breite * self.hoehe

    def umfang(self) -> float:
        return 2 * (self.breite + self.hoehe)

    def verschieben(self, dx: float, dy: float) -> None:
        self.links_unten.verschieben(dx, dy)

    def enthaelt(self, punkt: Punkt) -> bool:
        return (
            self.links_unten.x <= punkt.x <= self.links_unten.x + self.breite
            and self.links_unten.y <= punkt.y <= self.links_unten.y + self.hoehe
        )


if __name__ == "__main__":
    p1 = Punkt(0, 0)
    p2 = Punkt(3, 4)

    print(f"Distanz p1 -> p2: {p1.distanz_zu(p2):.2f}")

    k = Kreis(Punkt(1, 1), 2)
    r = Rechteck(Punkt(0, 0), 5, 2)

    print(f"Kreis: Fläche={k.flaeche():.2f}, Umfang={k.umfang():.2f}")
    print(f"Rechteck: Fläche={r.flaeche():.2f}, Umfang={r.umfang():.2f}")
    print(f"Punkt {p2} liegt im Rechteck? {r.enthaelt(p2)}")
=======
def addiere(a, b):
    return a + b


print("Hallo Welt!")
ergebnis = addiere(3, 4)
print("3 + 4 =", ergebnis)


def subtrahiere(a, b):
    return a - b


ergebnis_subtraktion = subtrahiere(10, 5)
print("10 - 5 =", ergebnis_subtraktion)
>>>>>>> human_feature
