from services.bank import Bank
from models.essen import mars


class Kunde:
    def __init__(self, kontostand: int, bargeld: int, nutzt_karte: bool):
        self.kontostand: int = kontostand
        self.bargeld: int = bargeld
        self.nutzt_karte: bool = nutzt_karte
        self.produkt_auswahl: str = ""

    def auswahl_produkt(self, auswahl: str):
        self.produkt_auswahl = auswahl

    def karte_eingeben(self) -> str:
        if self.nutzt_karte:
            return "Karte eingelesen"
        else:
            return "Keine Karte vorhanden"

    def karte_ausgeben(self) -> str:
        return "Karte wird ausgegeben"

    def bezahlen(self, mit_karte: bool, betrag: int, bank: Bank) -> str:
        if mit_karte:
            autorisiert = bank.zahlung_autorisieren(betrag)
            if autorisiert:
                bank.kontostand_aktualisieren(betrag)
                return "Zahlung mit Karte erfolgreich"
            else:
                return "Zahlung mit Karte fehlgeschlagen"
        else:
            if self.bargeld >= betrag:
                self.bargeld = self.bargeld - betrag
                return "Zahlung mit Bargeld erfolgreich"
            else:
                return "Zahlung mit Bargeld fehlgeschlagen"

    def ware_entnehmen(self) -> str:
        return f"{self.produkt_auswahl} wird entnommen"

    def wechselgeld_entnehmen(self) -> int:
        return 0


kunde = Kunde(kontostand=50, bargeld=10, nutzt_karte=True)
bank = Bank(kontostand_kunde=50, karte_gueltigkeit=True)

kunde.auswahl_produkt("Mars")
print(kunde.bezahlen(True, mars.preis, bank))
