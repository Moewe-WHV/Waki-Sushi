"""Getränke-Modelle für den Snackautomaten."""

class Getraenke:
    """Basis-Klasse für Getränke im Snackautomaten."""

    def __init__(self, verpackung, menge_liter):
        """Getränk mit Verpackung und Menge.

        Args:
            verpackung (str): Bezeichnung der Verpackung oder des Getränks.
            menge_liter (int|float): Menge des Getränks in Litern oder Millilitern.
        """
        self.verpackung = verpackung
        self.menge_liter = menge_liter

class Wasser(Getraenke):
    """Wasser mit Kohlensäureinformation."""

    def __init__(self, verpackung, menge_liter, kohlensaeure):
        """Initialisiert ein Wasserprodukt.

        Args:
            verpackung (str): Produktname, z. B. "Wasser" oder "Stilles Wasser".
            menge_liter (int|float): Menge des Wassers.
            kohlensaeure (bool): True bei kohlensäurehaltigem Wasser.
        """
        super().__init__(verpackung, menge_liter)
        self.kohlensaeure = kohlensaeure

class Cola(Getraenke):
    """Cola-Variante im Snackautomaten."""

    def __init__(self, verpackung, menge_liter, sorte):
        """Initialisiert eine Cola-Variante.

        Args:
            verpackung (str): Produktname der Cola-Variante.
            menge_liter (int|float): Menge der Cola.
            sorte (str): Sorte der Cola, z. B. "Cola", "Light" oder "Zero".
        """
        super().__init__(verpackung, menge_liter)
        self.sorte = sorte

class Tee(Getraenke):
    """Tee mit Sorte und Temperaturinformation."""

    def __init__(self, verpackung, menge_liter, sorte, kalt):
        """Initialisiert einen Teeartikel.

        Args:
            verpackung (str): Produktname des Tees.
            menge_liter (int|float): Menge des Tees.
            sorte (str): Teesorte, z. B. "schwarz" oder "gruen".
            kalt (bool): True, wenn der Tee kalt ist.
        """
        super().__init__(verpackung, menge_liter)
        self.sorte = sorte
        self.kalt = kalt


wasser_mit_Kohlensäure = Wasser(menge_liter=250, verpackung="Wasser", kohlensaeure=True)
wasser_ohne_Kohlensäure = Wasser(menge_liter=250, verpackung="Stilles Wasser", kohlensaeure=False)

cola = Cola(menge_liter=330, verpackung="Cola", sorte="Cola")
cola_light = Cola(menge_liter=330, verpackung="Cola Light", sorte="Light")
cola_zero = Cola(menge_liter=330, verpackung="Cola Zero", sorte="Zero")

schwarz_tee_heiß = Tee(menge_liter=25, verpackung="Heißer schwarzer Tee", kalt=False, sorte="schwarz")
schwarz_tee_kalt = Tee(menge_liter=25, verpackung="Kalter Schwarzer Tee", kalt=True, sorte="schwarz")

gruen_tee_heiß = Tee(menge_liter=250, verpackung="Heißer grüner Tee", kalt=False, sorte="gruen")
gruen_tee_kalt = Tee(menge_liter=250, verpackung="Kalter grüner Tee", kalt=True, sorte="gruen")
