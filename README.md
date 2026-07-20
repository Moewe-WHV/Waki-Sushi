# WAKI-SUSHI 
Lermprojekt - FIAE Umschulung  - Snackautomat

---

### Angaben
| Erstellt | Bearbeitet | Start | Abgabe | SOLL Zeit | IST Zeit | Geschätzte Zeit |
|----------|------------|-------|--------|-----------|----------|-----------------|
| Gruppe 2 | Gruppe 3   | 20.07 |  23.07 | 8 Stunden |          |                 |

---

### Aufgabenstellung
Waki-Sushi betreibt 5 Snackautomaten, verteilt über Campus und Wohnheime. Jeder Automat braucht zwei Verbindungen:  
- Bank (lizenziert, für Kartenzahlung)
- Uni-Netzwerk (zentrale Datenbank + Kommunikationsknoten der Betreiber)  

Die Automaten selbst reden nicht miteinander – Datenschutzgründe beim Bezahlen.  
Bestückt wird alles vom Servicemitarbeiter Haru Tawara, der seine Infos vom Uni-Netzwerk bekommt.   
Sortiment: 
- Wasabinüsse, Algenchips, Mars 
- Wasser, Cola, Grüner Tee  

Ein Programm bauen, das den vollen Funktionsumfang eines einzelnen Automaten im Netzwerk abbildet – auf Basis der Klassen- und Sequenzdiagramme.

---

### Architektur
```
WAKI-SUSHI/
├─ docs/
│  ├── aufgabenstellung.md
│  ├── dokumentation.md
│  └── diagramme/
│       ├── (korrektur)Klassendiagramm.md
│       └── (korrektur)Sequenzdiagramm.md
└── snackautomat/
│   ├── main.py                     # Programmstart, Interaktionsschleife
│   ├── models/
│   │   ├── __init__.py
│   │   ├── produkt.py              # Produkt (Basis), Essen, Getränke + Subklassen
│   │   ├── kunde.py                # Kunde
│   │   └── snackautomat.py         # Snackautomat (Kernklasse)
│   └── services/
│        ├── __init__.py
│        ├── bank.py                 # Bank
│        ├── uni_netzwerk.py         # Uni-Netzwerk
│        └── servicemitarbeiter.py   # Servicemitarbeiter
├──.gitignore.md
└── README.md

```  

---

### Milestones
```plantuml
MS0 --> MS1 : Programmierung snackautomat/ + models/    (parallel, je 3h)
MS1 --> MS2 : zusammenfügen in main                     (1h)
MS2 --> MS3 : Test & Doku                               (1h)
```