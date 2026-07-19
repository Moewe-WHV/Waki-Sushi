# WAKI-SUSHI Dokumentation

Erstellt: Gruppe 2 (Henning, Phillip & Niklas)  
Bearbeitet: Gruppe 3 (Jesse & Tim)  
Aufgabe: Programmieren eines Snackautomaten  
SOLL Zeit:  
IST Zeit:  

---

## Gefundene Fehler
### Klassendiagramm 

| Fehler                                                                                                                                                               | Korrektur                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Essen/Getränke sind per Vererbungspfeil an Snackautomat. Das heißt semantisch "ein Snackautomat _ist_ ein Essen". | Das muss **Komposition/Aggregation** sein  – der Automat _hat_ Essen und Getränke im Bestand. |
| -`sting`  <br>- `enthnemen`  <br>- `anehmen`| - `string`<br>- `entnehmen`<br>-  `annehmen` | - Klasse = `Bargeld_ausgeben`<br>- Sequenzdiagramm = `Wechselgeld ausgabe`| Sollte einheitlich sein: <br>Klasse = Bargeld_ausgeben <br>Sequenz = Bargeld ausgeben         |
| Im Sequenzdiagramm ruft das Uni-Netzwerk direkt den Servicemitarbeiter an ("Servicecall"), aber im Klassendiagramm gibt's zwischen den beiden gar keine Assoziation. | Beziehungen und Kompositionen korrekt darstellen und konsistent arbeiten. |
---
#### Sequenzdiagramm

| Fehler                                                                                                                                                            | Korrektur                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| "Kontostand aktualisieren" ist gestrichelt gezeichnet.<br>                                                                                                        | Aktiver, durchgezogener Aufruf Snackautomat→Bank |
| "Wechselgeld ausgabe" **vor** dem Self-Call "Wechselgeldbestand aktualisieren"                                                                                    | Erst intern aktualisieren, dann rausgeben        |
| "Bestand auffüllen" passiert direkt am Automaten, ohne dass der Servicemitarbeiter sichtbar auftaucht lt. Klassendiagramm Methode "Bestand auffüllen vorhanden" |                                                  |                                                                                                                                                                

***
## Projekt-Tagebuch

### 23.07.
```

```
- []
---
### 22.07.
```

```
- []
---
### 21.07.

``` 

```
- []
---
### 20.07.
```

```
- []
---
### 17.07.
```
Erhalt der Unterlagen.
```
- [x] Aufgabenstellung verstehen
- [x] Diagramme prüfen 
- [x] Repo anlegen
- [ ] Architektur erstellen 
- [x] Kanban anlegen
---

## Aufgetretene Probleme
### Coding

| Was | Wann | Wer |
| --- | ---- | --- |
|     |      |     |

### Planung

| Was | Wann | Wer |
| --- | ---- | --- |
|     |      |     |

### Dokumentation

| Was | Wann | Wer |
| --- | ---- | --- |
|     |      |     |

### Kommunikation

| Was | Wann | Wer |
| --- | ---- | --- |
|     |      |     |

---
## Aufteilung

- Aufteilung A
	- Essen/Getränke + Subklassen
	- Kunde, Bank
	- Kartenzahlungs-Flow
- Aufteilung B 
	- Snackautomat-Grundgerüst (Bestand, Ausgabe)
	- Uni-Netzwerk, Servicemitarbeiter
	- Bargeldzahlung + Servicecall/Auffüll-Logik

## Lerneffekte
```
Was haben wir nun in dem Projekt alles gelernt, was würden wir beim nächsten mal anders machen? 
```
- 
- 
- 
- 
- 
