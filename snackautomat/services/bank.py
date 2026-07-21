"""Bankdienst für die Zahlungsprüfung im Snackautomaten."""

class Bank:
    """Simuliert eine Bankverbindung für die Kartenzahlung.

    Attributes:
        kontostand_kunde (int|float): Aktueller Kontostand des Kunden.
        karte_gueltigkeit (bool): Ob die Karte gültig ist.
        pin (int): Bei der Bank hinterlegte, korrekte PIN.
    """

    def __init__(self, kontostand_kunde, karte_gueltigkeit, pin):
        """Initialisiert die Bank mit Kontostand, Kartenvalidität und PIN.

        Args:
            kontostand_kunde (int|float): Verfügbarer Kontostand des Kunden.
            karte_gueltigkeit (bool): True, wenn die Karte gültig ist.
            pin (int): Die bei der Bank hinterlegte, korrekte PIN.
        """
        self.kontostand_kunde = kontostand_kunde
        self.karte_gueltigkeit = karte_gueltigkeit
        self.pin = pin

    def Kontostand_aktualisieren(self, betrag):
        """Zieht einen Betrag vom Kundenkonto ab.

        Args:
            betrag (int|float): Betrag, der abgebucht werden soll.
        """
        self.kontostand_kunde = self.kontostand_kunde - betrag

    def Kontostand_pruefen(self, betrag):
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

    def PIN_pruefen(self, pin_eingabe):
        """Prüft die eingegebene PIN gegen die hinterlegte Bank-PIN.x   

        Args:
            pin_eingabe (int): Eingabe der Kunden-PIN.

        Returns:
            bool: True, wenn die PIN korrekt ist.
        """
        if pin_eingabe == self.pin:
            return True
        else:
            return False
