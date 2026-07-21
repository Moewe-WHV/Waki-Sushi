from models.snackautomat import Snackautomat
from models.kunde import Kunde
from models.essen import Essen
from models.getraenke import Getraenke
from services.bank import Bank
from services.servicemitarbeiter import Servicemitarbeiter
from services.uni_netzwerk import Uni_Netzwerk


def betrieb_starten():
    while True:
        print()
        print("HERZLICH WILLKOMMEN BEI DEINEM SNACKAUTOMATEN NUMMER 1")
        print("Folgendes haben wir im Angebot:") # Menge und Preis hinzufügen
        print()
        print("--GETRÄNKE--")
        print("1. Cola")
        print("2. Wasser")  # mit oder ohne CO2?
        print("3. Tee") # Kalt oder Heiß?
        print("--------------------------------------------------------------------------")
        print("--SPEISEN--")
        print("4. Algenchips")
        print("5. Wasabinüsse")
        print("6. Mars")
        print("--------------------------------------------------------------------------")
        print("7. Abbruch")
        auswahl_produkt = input("Bitte wähle die Nummer des Produkts aus: ")
        
        if auswahl_produkt == "7":
            break   
        print()
        automat1 = Snackautomat("Automat 1", 40, 200, 0.8)
        automat1.produkt_ausgeben(auswahl_produkt)
        automat1.bestand_aktualisieren(auswahl_produkt)
        automat1.bestand_anzeigen()
        antwort = input("Ein weiteres Produkt?(y/n): ")
        if antwort == "y":
            betrieb_starten()

betrieb_starten()

if __name__ == "__main__":
    main()