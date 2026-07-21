"""Kunde-Modell für den Snackautomaten.

Dieses Modul enthält die Kundenklasse für die Interaktion mit dem Automaten.
"""

class Kunde:
    """Modelliert einen Kunden am Snackautomaten.

    Ein Kunde kann eine Produktauswahl treffen, zwischen Karte und Bar wählen,
    eine PIN eingeben und die Ware sowie Wechselgeld entnehmen.
    """

    def __init__(self, kontostand, bargeld, nutzt_karte, snackautomat=None, bank=None):
        """Initialisiert einen Kunden mit Zahlungsinformationen.

        Args:
            kontostand (int|float): Kontostand auf der Karte.
            bargeld (int|float): Verfügbares Bargeld bei der Nutzung des Automaten.
            nutzt_karte (bool): True, wenn der Kunde mit Karte zahlen möchte.
            snackautomat (Snackautomat|None): Referenz auf den genutzten Automaten.
            bank (Bank|None): Referenz auf die Bank zur Karten-/PIN-Prüfung.
        """
        self.kontostand = kontostand
        self.bargeld = bargeld
        self.nutzt_karte = nutzt_karte
        self.snackautomat = snackautomat
        self.bank = bank
        self.pin_korrekt = None
        self.rechnungsbetrag = None  # wird gesetzt, sobald Snackautomat den Preis liefert

    def Auswahl_produkt(self, produktauswahl):
        """Speichert die gewählte Produktoption.

        Args:
            produktauswahl (str): Name des ausgewählten Produkts.
        """
        self.produktauswahl = produktauswahl
        # TODO: sobald Snackautomat fertig ist, hier den Preis nachtragen:
        # self.rechnungsbetrag = self.snackautomat.preis_ermitteln(produktauswahl)

    def Bezahlen(self, mit_karte):
        """Führt den Bezahlvorgang aus.

        Args:
            mit_karte (bool): True bei Kartenzahlung, False bei Barzahlung.

        Returns:
            str: Ergebnis der Bezahlung.
        """
        if self.rechnungsbetrag is None:
            return "..."

        if mit_karte:
            if self.bank is None:
                return "Zahlung abgelehnt"

            if not self.bank.karte_gueltigkeit:
                return "Zahlung abgelehnt"

            if not self.pin_korrekt:
                return "Zahlung abgelehnt"

            genug_guthaben = self.bank.Kontostand_pruefen(self.rechnungsbetrag)
            if not genug_guthaben:
                return "Zahlung abgelehnt"

            self.bank.Kontostand_aktualisieren(self.rechnungsbetrag)
            self.kontostand = self.bank.kontostand_kunde
            return "Zahlung erfolgreich"

        else:
            if self.bargeld < self.rechnungsbetrag:
                return "Zahlung abgelehnt"

            self.bargeld = self.bargeld - self.rechnungsbetrag
            return "Zahlung erfolgreich"

    def Wechselgeld_entnehmen(self):
        """Gibt Hinweise zur Entnahme von Wechselgeld zurück.

        Returns:
            str: Platzhalter für das Wechselgeld-Entnahmeverhalten.
        """
        return "..."

    def Karte_eingeben(self, karte_einfuehren):
        """Aktiviert die Kartennutzung und prüft die Kartengültigkeit bei der Bank.

        Args:
            karte_einfuehren (bool): True, wenn die Karte eingelegt wurde.

        Returns:
            str: Rückmeldung zum Karten-Einführungsprozess.
        """
        self.nutzt_karte = karte_einfuehren

        if not karte_einfuehren:
            return "..."

        if self.bank is None:
            return "..."

        if self.bank.karte_gueltigkeit:
            return "Karte gültig"
        else:
            return "Karte ungültig"

    def PIN_eingeben(self, pin_eingabe):
        """Speichert die eingegebene PIN und prüft sie bei der Bank.

        Args:
            pin_eingabe (str|int): PIN-Eingabe des Kunden.
        """
        self.pin_eingabe = pin_eingabe

        if self.bank is not None:
            self.pin_korrekt = self.bank.PIN_pruefen(pin_eingabe)

    def Karte_entnehmen(self):
        """Gibt den Abschluss der Kartenentnahme zurück.

        Returns:
            str: Platzhalter für das Kartenrückgabeverhalten.
        """
        return "..."

    def Ware_entnehmen(self):
        """Bestätigt die Entnahme der ausgegebenen Ware.

        Returns:
            str: Platzhalter für den Entnahmeprozess.
        """
        return "..."
