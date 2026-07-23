"""Servicepersonal für die Wartung und Befüllung des Snackautomaten."""


class Servicemitarbeiter:
    """Repräsentiert einen Service-Mitarbeiter, der Automaten betreut."""

    def __init__(self, name: str):
        """Initialisiert einen Service-Mitarbeiter mit einem Namen."""
        self.name = name

    def bestand_auffuellen(self, produkt: str, anzahl: int, automat):
        """Füllt einen Snackautomaten mit zusätzlicher Menge eines Produkts auf.

        Args:
            produkt (str): Name des aufzufüllenden Produkts.
            anzahl (int): Anzahl der nachzufüllenden Einheiten.
            automat: Der Snackautomat, dessen Bestand aktualisiert wird.
        """
        automat.bestand[produkt] = automat.bestand[produkt] + anzahl


mitarbeiter = Servicemitarbeiter("Haru Tawara")