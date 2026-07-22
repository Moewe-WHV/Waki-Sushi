from models.snackautomat import Snackautomat
from models.kunde import Kunde
from models.essen import Essen, Mars, Wasabinuesse, Algenchips # Alle kindklassen werden so aus der Elternklasse und die Elterklasse selbst importiert
from models.getraenke import Getraenke, Cola, Wasser, Tee # Hier dasselbe wie bei der Zeile oben drüber
from services.bank import Bank
from services.servicemitarbeiter import Servicemitarbeiter
from services.uni_netzwerk import Uni_Netzwerk


def main():
    # Die Klasse Snackautomat
    automat1 = Snackautomat("Automat 1", 40, 200, 0.8)
    # Produkte aus den Klassen Essen und Getraenke
    mars = Mars(menge_gramm=45, verpackung="Plastikfolie", preis=1.20)
    wasabinuesse = Wasabinuesse(menge_gramm=50, verpackung="Papiertüte", preis=1.50)
    algenchips = Algenchips(menge_gramm=30, verpackung="Pappdose", preis=1.80)
    cola = Cola(menge_liter=330, verpackung="PET Flasche", sorte="Cola", preis=1.50)
    wasser_mit_Kohlensäure = Wasser(menge_liter=250, verpackung="PET Flasche", kohlensaeure=True, preis=1.00)
    wasser_ohne_Kohlensäure = Wasser(menge_liter=250, verpackung="PET Flasche", kohlensaeure=False, preis=1.00)
    grüner_tee_heiß = Tee(menge_liter=25, verpackung="Glasflasche", kalt=False, sorte="Grüner Tee", preis=1.50)
    grüner_tee_kalt = Tee(menge_liter=25, verpackung="Glasflasche", kalt=True, sorte="Grüner Tee", preis=1.50)
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
    print()
    # Ab hier beginnt die Bezahlung
    if auswahl_produkt == 1:
            automat1.zahlung_abwickeln(cola)
            print()
            karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
            if karte_oder_bar == "b":
                print()
                automat1.bargeld_annehmen_und_ausgeben(cola)
            elif karte_oder_bar == "k":
                print()
                print("Bitte stecken Sie ihre Karte ein!")
                print(".......................................")
                automat1.karte_einlesen()
                print(".......................................")
                automat1.karte_pruefen()
                print(".......................................")
                print("Die Überweisung war erfolgreich!")
                print(".......................................")
                automat1.karte_ausgeben()
#---------------------------------------------------------------------------------------------------------
    if auswahl_produkt == 2:
            automat1.zahlung_abwickeln(wasser_mit_Kohlensäure)
            print()
            karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
            if karte_oder_bar == "b":
                print()
                automat1.bargeld_annehmen_und_ausgeben(wasser_mit_Kohlensäure)
            elif karte_oder_bar == "k":
                print()
                print("Bitte stecken Sie ihre Karte ein!")
                automat1.karte_einlesen()
                automat1.karte_pruefen()
                print("Die Überweisung war erfolgreich!")
                automat1.karte_ausgeben()
#----------------------------------------------------------------------------------------------------------
    if auswahl_produkt == 3:
            automat1.zahlung_abwickeln(grüner_tee_heiß)
            print()
            karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
            if karte_oder_bar == "b":
                print()
                automat1.bargeld_annehmen_und_ausgeben(grüner_tee_heiß)
            elif karte_oder_bar == "k":
                print()
                print("Bitte stecken Sie ihre Karte ein!")
                automat1.karte_einlesen()
                automat1.karte_pruefen()
                print("Die Überweisung war erfolgreich!")
                automat1.karte_ausgeben()
#----------------------------------------------------------------------------------------------------------
    if auswahl_produkt == 4:
            automat1.zahlung_abwickeln(algenchips)
            print()
            karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
            if karte_oder_bar == "b":
                print()
                automat1.bargeld_annehmen_und_ausgeben(algenchips)
            elif karte_oder_bar == "k":
                print()
                print("Bitte stecken Sie ihre Karte ein!")
                automat1.karte_einlesen()
                automat1.karte_pruefen()
                print("Die Überweisung war erfolgreich!")
                automat1.karte_ausgeben()
#---------------------------------------------------------------------------------------------------------
    if auswahl_produkt == 5:
            automat1.zahlung_abwickeln(wasabinuesse)
            print()
            karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
            if karte_oder_bar == "b":
                print()
                automat1.bargeld_annehmen_und_ausgeben(wasabinuesse)
            elif karte_oder_bar == "k":
                print()
                print("Bitte stecken Sie ihre Karte ein!")
                automat1.karte_einlesen()
                automat1.karte_pruefen()
                print("Die Überweisung war erfolgreich!")
                automat1.karte_ausgeben()
#----------------------------------------------------------------------------------------------------------
    if auswahl_produkt == 6:
        automat1.zahlung_abwickeln(mars)
        print()
        karte_oder_bar = input("Möchten Sie Bar oder mit Karte zahlen?(b/k) ")
        if karte_oder_bar == "b":
            print()
            automat1.bargeld_annehmen_und_ausgeben(mars)
        elif karte_oder_bar == "k":
            print()
            print("Bitte stecken Sie ihre Karte ein!")
            automat1.karte_einlesen()
            automat1.karte_pruefen()
            print("Die Überweisung war erfolgreich!")
            automat1.karte_ausgeben()
            
        

    print()
    automat1.produkt_ausgeben(auswahl_produkt)
    automat1.bestand_aktualisieren(auswahl_produkt)
    print()
    #automat1.bestand_anzeigen()
    antwort = input("Ein weiteres Produkt?(y/n): ")
    if antwort == "y":
        main()    

if __name__ == "__main__":
    main()