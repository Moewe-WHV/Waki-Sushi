"""Bankdienst für die Zahlungsprüfung im Snackautomaten."""


class Bank:
    """Simuliert eine Bankverbindung für die Kartenzahlung.

    Attributes:
        kontostand_kunde (int|float): Aktueller Kontostand des Kunden.
        karte_gueltigkeit (bool): Ob die Karte gültig ist.
    """

    def __init__(self, kontostand_kunde, karte_gueltigkeit):
        """Initialisiert die Bank mit Kontostand und Kartenvalidität.

        Args:
            kontostand_kunde (int|float): Verfügbarer Kontostand des Kunden.
            karte_gueltigkeit (bool): True, wenn die Karte gültig ist.
        """
        self.kontostand_kunde = kontostand_kunde
        self.karte_gueltigkeit = karte_gueltigkeit

    def kontostand_pruefen(self, betrag):
        """Prüft, ob der Kunde genügend Guthaben für die Zahlung hat.

        Args:
            betrag (int|float): Zu prüfender Betrag.

        Returns:
            bool: True, wenn der Kontostand ausreichend ist.
        """
        if self.kontostand_kunde >= betrag:
            return True
        else:
            return False

    def kontostand_aktualisieren(self, betrag):
        """Zieht einen Betrag vom Kundenkonto ab.

        Args:
            betrag (int|float): Betrag, der abgebucht werden soll.
        """
        self.kontostand_kunde = self.kontostand_kunde - betrag

    def zahlung_autorisieren(self, betrag):
        """Prüft, ob eine Kartenzahlung durchgeführt werden darf.

        Die Karte muss gültig sein und der Kontostand muss ausreichen.

        Args:
            betrag (int|float): Betrag, der abgebucht werden soll.

        Returns:
            bool: True, wenn die Zahlung autorisiert wird.
        """
        if not self.karte_gueltigkeit:
            return False
        if self.kontostand_pruefen(betrag):
            return True
        else:
            return False
