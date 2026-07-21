"""Kunde-Modell für den Snackautomaten."""

class Kunde:
    """Kunde, der am Snackautomaten Produkte auswählt, bezahlt und entnimmt."""

    def __init__(self, kontostand: int, bargeld: int, nutzt_karte: bool, snackautomat=None):
        self.kontostand: int = kontostand
        self.bargeld: int = bargeld
        self.nutzt_karte: bool = nutzt_karte
        self.snackautomat = snackautomat

    def Auswahl_produkt(self, produktauswahl: str) -> None:
        self.produktauswahl = produktauswahl

    def Bezahlen(self, mit_karte: bool) -> str:
        # Ablauf/Betrag wird über self.snackautomat <-> Bank abgewickelt
        return "..."

    def Wechselgeld_entnehmen(self) -> str:
        return "..."

    def Karte_eingeben(self, karte_einfuehren: bool) -> str:
        self.nutzt_karte = karte_einfuehren
        return "..."

    def PIN_eingeben(self, pin_eingabe: int) -> None:
        self.pin_eingabe = pin_eingabe

    def Karte_entnehmen(self) -> str:
        return "..."

    def Ware_entnehmen(self) -> str:
        return "..."