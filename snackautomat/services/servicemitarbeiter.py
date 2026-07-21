class Servicemitarbeiter: 
    def __init__(self, name: str): 
        self.name = name 
        
    def bestand_auffuellen(self, produkt: str, anzahl: int, automat):
        automat.bestand[produkt] = automat.bestand[produkt] + anzahl
    
mitarbeiter = Servicemitarbeiter("Haru Tawara")