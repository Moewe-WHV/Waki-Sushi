"""Kunde-Modell für den Snackautomaten."""

class Kunde:
    """Kunde, der am Snackautomaten Produkte auswählt, bezahlt und entnimmt."""

    def __init__(self, kontostand, bargeld, nutzt_karte, snackautomat=None):
        self.kontostand = kontostand
        self.bargeld = bargeld
        self.nutzt_karte = nutzt_karte
        self.snackautomat = snackautomat

    def Auswahl_produkt(self, produktauswahl):
        self.produktauswahl = produktauswahl

    def Bezahlen(self, mit_karte):
        # Ablauf/Betrag wird über self.snackautomat <-> Bank abgewickelt
        return "..."

    def Wechselgeld_entnehmen(self):
        return "..."

    def Karte_eingeben(self, karte_einfuehren):
        self.nutzt_karte = karte_einfuehren
        return "..."

    def PIN_eingeben(self, pin_eingabe):
        self.pin_eingabe = pin_eingabe

    def Karte_entnehmen(self):
        return "..."

    def Ware_entnehmen(self):
        return "..."
