"""Kunde-Modell für den Snackautomaten.

Dieses Modul enthält die Kundenklasse für die Interaktion mit dem Automaten.
"""

class Kunde:
    """Modelliert einen Kunden am Snackautomaten.

    Ein Kunde kann eine Produktauswahl treffen, zwischen Karte und Bar wählen,
    eine PIN eingeben und die Ware sowie Wechselgeld entnehmen.
    """
    def __init__(self, kontostand: int, bargeld: int, nutzt_karte: bool):
        self.kontostand: int = kontostand
        self.bargeld: int = bargeld 
        self.nutzt_karte: bool = nutzt_karte
        
    def auswahl_produkt(self) -> str: 
        pass 
    
    def karte_eingeben(self) -> str: 
        return "..."
    
    def karte_ausgeben(self) -> str: 
        return "..."
    
    def bezahlen(self, mit_karte: bool) -> str:
        if mit_karte:
            return "..."
        else: 
            return "..."
    
    
