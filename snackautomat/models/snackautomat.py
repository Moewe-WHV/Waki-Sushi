class Snackautomat: 
        def __init__(self, name, wechselgeldbestand, wechselgeld_kapazitaet, wechselgeld_leerungsgrenze):
        self.name = name
        self.bestand = {"Wasabinuesse" : 20, "Algenchips" : 20, "Mars" : 20, "Wasser" : 20, "Cola" : 20, "Tee" : 20}
        self.wechselgeldbestand = wechselgeldbestand
        self.wechselgeld_kapazitaet = 200
        self.wechselgeld_leerungsgrenze = 0.8

    def bestand_anzeigen(self):
        for key, value in self.bestand.items():
            print(f"{key} : {value}")

    def wechselgeldbestand_anzeigen(self):
        pass
    def karte_einlesen(self):
        pass
    def karte_pruefen(self):
        pass
    def karte_ausgeben(self):
        pass
    def zahlung_abwickeln(self):
        pass
    def bargeld_annehmen(self):
        pass
    def bargerld_ausgeben(self):
        pass
    def produkt_ausgeben(self):
        pass
    def bestand_aktualisieren(self):
        pass
    def wechselgeldbestand_aktualisieren(self):
        pass






snackautomat1 = Snackautomat("Nummer 1")
snackautomat1.bestand_anzeigen()