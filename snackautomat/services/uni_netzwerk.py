class Uni_Netzwerk:
    def __init__(self, bestand: dict, kontostand: int, anzahl_snackautomaten: int):
        self.bestand: dict = bestand
        self.kontostand: int = kontostand
        self.anzahl_snackautomaten: int = anzahl_snackautomaten

    def bestandsdaten_empfangen(self, automat: str, produkte: dict):
        pass

    def wechselgeldbestand_empfangen(self, automat: str, bestand: int):        
        pass
    
automat_1 = Uni_Netzwerk(bestand={'Cola': 20}, kontostand=100, anzahl_snackautomaten=1)
print(automat_1.anzahl_snackautomaten)
print(automat_1.bestand)