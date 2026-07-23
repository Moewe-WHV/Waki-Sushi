"""Kundenmodell und Zahlungslogik für den Snackautomaten."""

from services.bank import Bank
from models.essen import mars


class Kunde:
    """Repräsentiert einen Kunden, der im Snackautomaten einkauft.

    Attributes:
        kontostand (int): Aktueller Konto- oder Kartenbetrag des Kunden.
        bargeld (int): Verfügbares Bargeld des Kunden.
        nutzt_karte (bool): Ob der Kunde eine Karte zur Zahlung verwenden möchte.
        produkt_auswahl (str): Gewähltes Produkt für den Kauf.
    """

    def __init__(self, kontostand: int, bargeld: int, nutzt_karte: bool):
        self.kontostand: int = kontostand
        self.bargeld: int = bargeld
        self.nutzt_karte: bool = nutzt_karte
        self.produkt_auswahl: str = ""

    def auswahl_produkt(self, auswahl: str):
        """Speichert die Produktwahl des Kunden."""
        self.produkt_auswahl = auswahl

    def karte_eingeben(self) -> str:
        """Gibt einen Status zurück, ob eine Karte eingelesen wurde."""
        if self.nutzt_karte:
            return "Karte eingelesen"
        else:
            return "Keine Karte vorhanden"

    def karte_ausgeben(self) -> str:
        """Simuliert das Ausgeben der Karte nach der Zahlung."""
        return "Karte wird ausgegeben"

    def bezahlen(self, mit_karte: bool, betrag: int, bank: Bank) -> str:
        """Führt eine Zahlung mit Karte oder Bargeld aus.

        Args:
            mit_karte (bool): True für Kartenzahlung, False für Bargeld.
            betrag (int): Zu zahlender Betrag.
            bank (Bank): Bankdienst für die Kartenautorisierung.

        Returns:
            str: Ergebnis der Zahlung.
        """
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
        """Beschreibt das Entfernen des gewählten Produkts aus dem Automaten."""
        return f"{self.produkt_auswahl} wird entnommen"

    def wechselgeld_entnehmen(self) -> int:
        """Gibt das Wechselgeld zurück, das dem Kunden ausgegeben wird."""
        return 0


kunde = Kunde(kontostand=50, bargeld=10, nutzt_karte=True)
bank = Bank(kontostand_kunde=50, karte_gueltigkeit=True)

kunde.auswahl_produkt("Mars")
print(kunde.bezahlen(True, mars.preis, bank))
