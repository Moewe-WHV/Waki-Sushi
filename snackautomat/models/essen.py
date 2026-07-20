"""Essen-Modelle für den Snackautomaten."""

class Essen:
    """Basis-Klasse für essbare Artikel im Snackautomaten."""

    def __init__(self, verpackung, menge_gramm, preis):
        """Initialisiert ein Lebensmittel mit Verpackung und Gewicht.

        Args:
            verpackung (str): Bezeichnung der Verpackung oder des Produkts.
            menge_gramm (int|float): Gewicht des Produkts in Gramm.
            preis (int|float): Preis des Produkts in Euro
        """
        self.verpackung = verpackung
        self.menge_gramm = menge_gramm
        self.preis = preis

class Wasabinuesse(Essen):
    """Wasabinüsse als Snack."""
    pass
    
class Algenchips(Essen):
    """Algenchips als Snack."""
    pass

class Mars(Essen):
    """Mars-Riegel als Snack."""
    pass

wasabinuesse = Wasabinuesse(menge_gramm=50, verpackung="Wasabinuesse", preis=1.50 )
algenchips = Algenchips(menge_gramm=30, verpackung="Algenchips", preis=1.80)
mars = Mars(menge_gramm=45, verpackung="Mars", preis=1.20)