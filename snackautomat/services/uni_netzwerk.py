"""Schnittstelle zum Uni-Netzwerk für Automatenbestände und Zahlungen."""

import json

from models.snackautomat import Snackautomat, DATEINAME


class Uni_Netzwerk:
    """Stellt die Verbindung zum Hochschulnetzwerk für Snackautomaten bereit."""

    def __init__(self, bestand: dict, kontostand: int, anzahl_snackautomaten: int):
        """Initialisiert das Uni-Netzwerk mit Basisdaten.

        Args:
            bestand (dict): Bestandsdaten der Automaten.
            kontostand (int): Gesamter Wechselgeldbestand des Netzwerks.
            anzahl_snackautomaten (int): Anzahl der verwalteten Automaten.
        """
        self.bestand: dict = bestand
        self.kontostand: int = kontostand
        self.anzahl_snackautomaten: int = anzahl_snackautomaten

    def bestandsdaten_empfangen(self, automat):
        """Empfängt Bestandsdaten eines Automaten und speichert sie.

        Args:
            automat: Der Snackautomat, dessen Bestand übertragen wird.
        """
        self.bestand = automat.bestand

    def bestand_aus_datei_laden(self):
        """Liest den Bestand direkt aus der gespeicherten JSON-Datei des Automaten."""
        with open(DATEINAME, "r") as datei:
            daten = json.load(datei)
        self.bestand = daten["bestand"]

    def wechselgeldbestand_empfangen(self, automat: str, bestand: int):
        """Empfängt den Wechselgeldbestand eines Automaten.

        Args:
            automat (str): Bezeichnung des Automaten.
            bestand (int): Wechselgeldbestand des Automaten.
        """
        pass


snackautomat1 = Snackautomat("Automat 1", 40, 200, 0.8)

print(snackautomat1.bestand)
