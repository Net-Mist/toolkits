import unittest

from cooklang.hugo import transform

cake = """
>> title: Cake aux olives

>> time: 50m


>> servings: 6


Préchauffer le four à 180°C (Th 6)


Dans un saladier, mélanger le @yaourt{1}, la @farine{150%g (environ 3 pots de yaourt)}, la @levure{1/2%sachet} et les @œufs{3}.
Ajouter l'@huile d'olive{1/2%pot (environ 50 ml)}. Bien mélanger.


Ajouter le @gruyère râpé{100%g}, le @basilic et les @olives{Environ 20 dénoyautées de chaque couleur (noires, vertes)} coupées en petits morceaux.

Verser dans un #moule à cake{} préalablement beurré et fariné. Cuire ~{40%minutes} au four à 180° C (thermostat 6).

Retirer le cake du four quand il est doré. Le servir tiède ou froid.

>> steps: optional
Incorporer éventuellement le @jambon{100%g} (coupé en dés), les @tomates séchées{40%g} et le @fromage de chèvre{100%g}.


"""


class TestHugo(unittest.TestCase):
    def test_cake(self) -> None:
        out = transform(cake)
        print(out)
