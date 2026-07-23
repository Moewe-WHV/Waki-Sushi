import json

from models.essen import Mars

DATEINAME = "data/zustand.json" # Datei, in der Bestand und Bargeldbetrag gespeichert werden

class Snackautomat:
    def __init__(self, name, wechselgeldbestand, wechselgeld_kapazitaet, wechselgeld_leerungsgrenze):
        self.name = name
        self.bestand = {"Wasabinuesse" : 15, "Algenchips" : 15, "Mars" : 20, "Wasser" : 20, "Cola" : 20, "Tee" : 15}
        self.wechselgeldbestand = 40 # Es wurde nicht angegeben, bis wohin ein Wechselgeldbestand ausgeleert wird. Wir haben uns selbst für 20% der max Kapazität entschieden
        self.wechselgeld_kapazitaet = 200
        self.wechselgeld_leerungsgrenze = 0.8 # 0.8 steht für was ??? wir nehmen an, dass 20% der Kapazität im Automaten bleiben soll
                                                # 0.8 sind 80% der Kapazität
        self.zustand_laden() # Falls schon einmal gespeichert wurde, überschreibt das die Werte von oben

    def zustand_speichern(self):
        """Speichert den Bestand und den Bargeldbetrag in einer JSON-Datei."""
        daten = {
            "bestand": self.bestand,
            "wechselgeldbestand": self.wechselgeldbestand
        }
        with open(DATEINAME, "w") as datei:
            json.dump(daten, datei, indent=4)

    def zustand_laden(self):
        """Lädt den Bestand und den Bargeldbetrag aus der JSON-Datei, falls vorhanden."""
        try:
            with open(DATEINAME, "r") as datei:
                daten = json.load(datei)
            self.bestand = daten["bestand"]
            self.wechselgeldbestand = daten["wechselgeldbestand"]
        except FileNotFoundError:
            pass
    
    def bestand_anzeigen(self):
        for key, value in self.bestand.items():
            print(f"{key} : {value}")
 
    def wechselgeldbestand_anzeigen(self):
        wechselgeldbestand = self.wechselgeldbestand
        print(f"{wechselgeldbestand} EUR")

    def zahlung_abwickeln(self, produkt):
    #Geld wird von Konto irgendwo hin transferiert bei Kartenzahlung
        rechnung = produkt.preis
        print(f"Der Preis ist {rechnung:.2f} Euro.")
        print()
 
    def karte_einlesen(self):
        print("Karte wird eingelesen...")
 
    def karte_pruefen(self):
        # Überprüfung von Kontostand > Rechnung oder ist Karte eine Bankkarte ??? // entscheiden uns für Prüfung ob Bankkarte
        print("Karte wird geprüft...")
 
    def karte_ausgeben(self):
        print("Karte wird ausgegeben...")
 
    def bargeld_annehmen_und_ausgeben(self, produkt):
        annahme_bar = float(input("Wieviel Bargeld wird eingezahlt? ")) # float wäre besser statt int // entscheiden uns für float
        ausgabe_bar = annahme_bar - produkt.preis
        print(f"Es gibt {ausgabe_bar} Euro zurück.")
        self.wechselgeldbestand = self.wechselgeldbestand + produkt.preis
        self.zustand_speichern()

    
                
    def wechselgeldbestand_aktualisieren(self):
            pass
 
    def produkt_ausgeben(self, auswahl_produkt):                                                             # Kann man produkt_ausgeben und bestand_aktualisieren zusammenfügen?
        if auswahl_produkt == 1 and self.bestand["Cola"] == 0:
            print("Cola ist derzeit ausverkauft!")
        elif auswahl_produkt == 2 and self.bestand["Wasser"] == 0:
            print("Wasser ist derzeit ausverkauft!")
        elif auswahl_produkt == 3 and self.bestand["Tee"] == 0:
            print("Tee ist derzeit ausverkauft!")
        elif auswahl_produkt == 4 and self.bestand["Algenchips"] == 0:
                    print("Algenchips sind derzeit ausverkauft!")
        elif auswahl_produkt == 5 and self.bestand["Wasabinuesse"] == 0:
            print("Wasabinüsse sind derzeit ausverkauft!")
        elif auswahl_produkt == 6 and self.bestand["Mars"] == 0:
                    print("Mars ist derzeit ausverkauft!")
        elif auswahl_produkt == 0 and auswahl_produkt >= 7:
            print("Diese Zahl enthält kein Produkt!")
        else:
            print("Das gewählte Produkt wird ausgegeben!")
 
    def bestand_aktualisieren(self, auswahl_produkt):
        if auswahl_produkt == 1:
            self.bestand["Cola"] = self.bestand["Cola"] - 1
        elif auswahl_produkt == 2:
            self.bestand["Wasser"] = self.bestand["Wasser"] - 1
        elif auswahl_produkt == 3:
            self.bestand["Tee"] = self.bestand["Tee"] - 1
        elif auswahl_produkt == 6:
            self.bestand["Mars"] = self.bestand["Mars"] - 1
        elif auswahl_produkt == 5:
            self.bestand["Wasabinuesse"] = self.bestand["Wasabinuesse"] - 1
        elif auswahl_produkt == 4:
            self.bestand["Algenchips"] = self.bestand["Algenchips"] - 1
        self.zustand_speichern()




#snackautomat1 = Snackautomat("Nummer 1")
#snackautomat1.bestand_anzeigen()
#self.bestand["Cola"]
 
 
#Fragen:
# 1.Werden Bareinnahmen in Wechselgeld umgewandelt oder wird das seperat gespeichert im Automaten?  
# 2.Wohin wird das Geld der Karte überwiesen? kein Firmenkonto verzeichnet
# 3.Ist bei karte_pruefen im Snackautomaten der Kontostand gemeint oder ob die Karte eine Bankkarte ist?
# 4.Warum gibt es bei Geld keinen float statt einem int?
# 5.Warum gibt es kein Menü für den Servicemitarbeiter?
# 6. Warum kann der Kunde die Karte ausgeben?

