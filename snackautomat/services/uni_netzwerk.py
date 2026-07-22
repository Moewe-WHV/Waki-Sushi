from models.snackautomat import Snackautomat

class Uni_Netzwerk:
    def __init__(self, bestand: dict, kontostand: int, anzahl_snackautomaten: int):
        self.bestand: dict = bestand
        self.kontostand: int = kontostand
        self.anzahl_snackautomaten: int = anzahl_snackautomaten

    def bestandsdaten_empfangen(self, automat):
        self.bestand = automat.bestand

    def wechselgeldbestand_empfangen(self, automat: str, bestand: int):
        pass

snackautomat1 = Snackautomat("Automat 1", 40, 200, 0.8)

print(snackautomat1.bestand)

#...