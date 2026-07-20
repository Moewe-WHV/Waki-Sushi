"""Essen-Modelle für den Snackautomaten."""

class Essen:
    """Basis-Klasse für essbare Artikel im Snackautomaten."""

    def __init__(self, verpackung, menge_gramm):
        """Initialisiert ein Lebensmittel mit Verpackung und Gewicht.

        Args:
            verpackung (str): Bezeichnung der Verpackung oder des Produkts.
            menge_gramm (int|float): Gewicht des Produkts in Gramm.
        """
        self.verpackung = verpackung
        self.menge_gramm = menge_gramm

class Wasabinuesse(Essen):
    """Wasabinüsse als Snack."""
    pass
    
class Algenchips(Essen):
    """Algenchips als Snack."""
    pass

class Mars(Essen):
    """Mars-Riegel als Snack."""
    pass

wasabinuesse = Wasabinuesse(menge_gramm=50, verpackung="Wasabinuesse")
algenchips = Algenchips(menge_gramm=30, verpackung="Algenchips")
mars = Mars(menge_gramm=45, verpackung="Mars")