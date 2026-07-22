from models.snackautomat import Snackautomat
from models.kunde import Kunde
from models.essen import Essen
from models.getraenke import Getraenke
from services.bank import Bank
from services.servicemitarbeiter import Servicemitarbeiter
from services.uni_netzwerk import Uni_Netzwerk


def main():
    automat1 = Snackautomat("Automat 1", 40, 200, 0.8)
    essen1 = Essen
    
    print()
    print("HERZLICH WILLKOMMEN BEI DEINEM SNACKAUTOMATEN NUMMER 1")
    print("Folgendes haben wir im Angebot:") # Menge und Preis hinzufügen
    print()
    print("--GETRÄNKE--")
    print("1. Cola              -- 1.50 EUR")
    print("2. Wasser            -- 1.00 EUR")  # mit oder ohne CO2?
    print("3. Tee               -- 1.50 EUR") # Kalt oder Heiß?
    print("--------------------------------------------------------------------------")
    print("--SPEISEN--")
    print("4. Algenchips        -- 1.50 EUR")
    print("5. Wasabinüsse       -- 1.80 EUR")
    print("6. Mars              -- 1.20 EUR")
    print("--------------------------------------------------------------------------")
    auswahl_produkt = int(input("Bitte wähle die Nummer des Produkts aus: "))
    if auswahl_produkt == 2:
        mit_co2 = input("Mit oder ohne Kohlensäure?(j/n) ")
    if auswahl_produkt == 3:
        print(input("Soll der Tee heiß oder kalt sein?(h/k) "))
        
    automat1.zahlung_abwickeln(mars)
    print()
    
    automat1.produkt_ausgeben(auswahl_produkt)
    automat1.bestand_aktualisieren(auswahl_produkt)
    automat1.bestand_anzeigen()
    antwort = input("Ein weiteres Produkt?(y/n): ")


if __name__ == "__main__":
    main()