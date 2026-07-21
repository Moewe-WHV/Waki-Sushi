class Snackautomat: 
    def __init__(self, name, wechselgeldbestand, wechselgeld_kapazitaet, wechselgeld_leerungsgrenze):
        self.name = name
        self.bestand = {"Wasabinuesse" : 15, "Algenchips" : 15, "Mars" : 20, "Wasser" : 20, "Cola" : 20, "Tee" : 15}
        self.wechselgeldbestand = 40
        self.wechselgeld_kapazitaet = 200
        self.wechselgeld_leerungsgrenze = 0.8 # 0.8 steht für was ??? wir nehmen an, dass 20% der Kapazität im Automaten bleiben soll

    def bestand_anzeigen(self):
        for key, value in self.bestand.items():
            print(f"{key} : {value}")

    def wechselgeldbestand_anzeigen(self):
        wechselgeldbestand = self.wechselgeldbestand
        print(f"{wechselgeldbestand} EUR")

    def karte_einlesen(self):
        print("Karte wird eingelesen...")

    def karte_pruefen(self):
        # Überprüfung von Kontostand > Rechnung oder ist Karte eine Bankkarte ???
        print("Karte wird geprüft...")

    def karte_ausgeben(self):
        print("Karte wird ausgegeben...")

    def zahlung_abwickeln(self):
        #Geld wird von Konto irgendwo hin transferiert bei Kartenzahlung
        pass

    def bargeld_annehmen(self):
        annahme_bar = int(input("Wieviel Bargeld wird eingezahlt? ")) # float wäre besser statt int

    def bargerld_ausgeben(self):
        ausgabe_bar = annahme_bar - rechnung # rechnung kommt von...

    def produkt_ausgeben(self):                                                             # Kann man produkt_ausgeben und bestand_aktualisieren zusammenfügen?
        if auswahl_produkt = "Cola" and self.bestand["Cola"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        elif auswahl_produkt == "2" and self.bestand["Wasser"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        elif auswahl_produkt == "3" and self.bestand["Tee"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        elif auswahl_produkt = "Mars" and self.bestand["Mars"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        elif auswahl_produkt == "5" and self.bestand["Wasabinuesse"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        elif auswahl_produkt = "Algenchips" and self.bestand["Algenchips"] == 0:
            print(f"{auswahl_produkt} ist derzeit ausverkauft!")
        else:
            print(f"{auswahl_produkt} wird ausgegeben!")

    def bestand_aktualisieren(self, auswahl_produkt):
        if auswahl_produkt == "Cola":
            self.bestand["Cola"] = self.bestand["Cola"] - 1
        elif auswahl_produkt == "Wasser":
            self.bestand["Wasser"] = self.bestand["Wasser"] - 1
        elif auswahl_produkt == "Tee":
            self.bestand["Tee"] = self.bestand["Tee"] - 1
        elif auswahl_produkt == "Mars":
            self.bestand["Mars"] = self.bestand["Mars"] - 1
        elif auswahl_produkt == "Wasabinuesse":
            self.bestand["Wasabinuesse"] = self.bestand["Wasabinuesse"] - 1
        elif auswahl_produkt == "Algenchips":
            self.bestand["Algenchips"] = self.bestand["Algenchips"] - 1

    def wechselgeldbestand_aktualisieren(self):
        pass



snackautomat1 = Snackautomat("Nummer 1")
snackautomat1.bestand_anzeigen()
self.bestand["Cola"]


#Fragen: 
# 1.Werden Bareinnahmen in Wechselgeld umgewandelt oder wird das seperat gespeichert im Automaten?  
# 2.Wohin wird das Geld der Karte überwiesen? kein Firmenkonto verzeichnet
# 3.Ist bei karte_pruefen im Snackautomaten der Kontostand gemeint oder ob die Karte eine Bankkarte ist?
# 4.Warum gibt es bei Geld keinen float statt einem int?