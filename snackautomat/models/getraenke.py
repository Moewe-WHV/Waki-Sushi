"""Getränke-Modelle für den Snackautomaten."""

class Getraenke:
    """Basis-Klasse für Getränke im Snackautomaten."""

    def __init__(self, verpackung, menge_liter, preis):
        """Getränk mit Verpackung und Menge.

        Args:
            verpackung (str): Bezeichnung das Material der Verpackung.
            menge_liter (int|float): Menge des Getränks in Litern oder Millilitern.
            preis (int|float): Preis des Produkts in Euro
        """
        self.verpackung = verpackung
        self.menge_liter = menge_liter
        self.preis = preis

class Wasser(Getraenke):
    """Wasser mit Kohlensäureinformation."""

    def __init__(self, verpackung, menge_liter, kohlensaeure, preis):
        """Initialisiert ein Wasserprodukt.

        Args:
            verpackung (str): Produktname, z. B. "Wasser" oder "Stilles Wasser".
            menge_liter (int|float): Menge des Wassers.
            kohlensaeure (bool): True bei kohlensäurehaltigem Wasser.
            preis (int|float): Preis des Produkts in Euro
        """
        super().__init__(verpackung, menge_liter, preis)
        self.kohlensaeure = kohlensaeure

class Cola(Getraenke):
    """Cola-Variante im Snackautomaten."""

    def __init__(self, verpackung, menge_liter, sorte, preis):
        """Initialisiert eine Cola-Variante.

        Args:
            verpackung (str): Produktname der Cola-Variante.
            menge_liter (int|float): Menge der Cola.
            sorte (str): Sorte der Cola, z. B. "Cola", "Light" oder "Zero".
            preis (int|float): Preis des Produkts in Euro
        """
        super().__init__(verpackung, menge_liter, preis)
        self.sorte = sorte

class Tee(Getraenke):
    """Tee mit Sorte und Temperaturinformation."""

    def __init__(self, verpackung, menge_liter, sorte, kalt, preis):
        """Initialisiert einen Teeartikel.

        Args:
            verpackung (str): Produktname des Tees.
            menge_liter (int|float): Menge des Tees.
            sorte (str): Teesorte, z. B. "schwarz" oder "gruen".
            kalt (bool): True, wenn der Tee kalt ist.
            preis (int|float): Preis des Produkts in Euro
        """
        super().__init__(verpackung, menge_liter, preis)
        self.sorte = sorte
        self.kalt = kalt


wasser_mit_Kohlensäure = Wasser(menge_liter=250, verpackung="PET Flasche", kohlensaeure=True, preis=1.00)
wasser_ohne_Kohlensäure = Wasser(menge_liter=250, verpackung="PET Flasche", kohlensaeure=False, preis=1.00)

cola = Cola(menge_liter=330, verpackung="PET Flasche", sorte="Cola", preis=1.50)

grüner_tee_heiß = Tee(menge_liter=25, verpackung="Glasflasche", kalt=False, sorte="Grüner Tee", preis=1.50)
grüner_tee_kalt = Tee(menge_liter=25, verpackung="Glasflasche", kalt=True, sorte="Grüner Tee", preis=1.50)
