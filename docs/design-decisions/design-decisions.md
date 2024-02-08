---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

# [Design decisions]
{: .no_toc }

<details open markdown="block">nte
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

--------------------------------------------------------------------------------------------------------------------

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

**1. Problemstellung: Auswahl einer geeigneten Authentifizierungsmethode:**

Das Ziel dabei wäre die Implementierung einer sicheren, benutzerfreundlichen und effizienten Methode zur Authentifizierung potentiellen Usern, die es ihnen ermöglicht, sich registrieren und anmelden zu können, um auf die App und ihre Funktionen, wie das Durchstöbern der Chatrooms und das Senden von Nachrichten, zugreifen zu können.

**Sicherheit:** Die Authentifizierungsmethode muss sicherstellen, dass Benutzerdaten geschützt sind und unbefugter Zugriff verhindert wird.

**Benutzerfreundlichkeit:** Die Methode sollte einfach und intuitiv sein, um eine hohe Akzeptanz bei den Benutzern zu erreichen und den Registrierungs- sowie Anmeldeprozess so reibungslos wie möglich zu gestalten.

**Skalierbarkeit:** Die gewählte Lösung sollte in der Lage sein, mit einer wachsenden Anzahl von Benutzern umzugehen, ohne an Leistung zu verlieren.

--------------------------------------------------------------------------------------------------------------------

**2. Problemstellung: Datenbankstruktur:**

Das Ziel besteht darin, eine robuste und skalierbare Datenbankstruktur für die Chat-Anwendung zu entwerfen, die eine effiziente Verwaltung von Benutzerdaten, Chatrooms und Nachrichten ermöglicht. Die Datenbankstruktur sollte die folgenden Hauptentitäten und deren Beziehungen umfassen:

Benutzerkonten: Erfassung von Benutzerinformationen wie Benutzername und Passwort (gehasht) anderen relevanten Informationen. Die Struktur sollte auch Mechanismen zur Authentifizierung und Autorisierung von Benutzern unterstützen.

Chatrooms: Verwaltung von Chatrooms, einschließlich ihrer Titel, Beschreibungen, Mitglieder und möglicherweise auch spezifischer Einstellungen wie Sichtbarkeit, Zugriffsrechte und Moderatoren.

Nachrichtenverläufe: Speicherung von Nachrichten, die in den Chatrooms ausgetauscht werden, einschließlich des Inhalts der Nachricht, des Zeitstempels, des Absenders und der zugehörigen Chatroom-IDs.

Die Datenbankstruktur muss flexibel genug sein, um Änderungen und Erweiterungen zu ermöglichen, wie die Hinzufügung neuer Chatrooms, die Verwaltung von Benutzerrollen oder die Implementierung von Nachrichtenverschlüsselung. Sie sollte auch eine effiziente Datenabfrage und -manipulation ermöglichen, um eine reibungslose und schnelle Leistung der Anwendung sicherzustellen, selbst bei einem wachsenden Datenvolumen und einer zunehmenden Anzahl von Benutzern. Letztendlich sollte die Datenbankstruktur das Herzstück der Chat-Anwendung sein, die eine zuverlässige und sichere Speicherung und Verwaltung von Informationen gewährleistet, um eine optimale Benutzererfahrung zu ermöglichen.


--------------------------------------------------------------------------------------------------------------------

**3. Problemstellung: Frontend-Technologie:**

Das Ziel besteht darin, geeignete Technologien für die Entwicklung der Benutzeroberfläche einer Webanwendung zu wählen. Die Herausforderung liegt darin, eine einfache und benutzerfreundliche Oberfläche zu schaffen, die gut aussieht und auf verschiedenen Geräten funktioniert. Es geht darum, Entscheidungen zu treffen, die sicherstellen, dass die Website schnell lädt, leicht zu bedienen ist und gut aussieht. Dazu gehört auch die Auswahl von Tools und Technologien, die die Entwicklung erleichtern und es ermöglichen, die Website einfach zu aktualisieren und zu warten. Letztendlich wollen wir sicherstellen, dass die Nutzer eine positive Erfahrung machen, wenn sie die Website besuchen, und dass die Entwicklung des Frontends reibungslos verläuft.

--------------------------------------------------------------------------------------------------------------------


### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

 **1. Design-Decision (Authentifizierungsmethode)**

 Wir fokussierten uns auf die Implementierung einer sicheren und benutzerfreundlichen Authentifizierungsmethode unter Verwendung von Passwort-Hashing mit pbkdf2:sha256. Diese Entscheidung basierte auf dem Bedürfnis, ein hohes Sicherheitsniveau zu gewährleisten, indem Nutzerpasswörter sicher gespeichert werden, was besonders in der heutigen Zeit, in der Datenschutz und Sicherheit von größter Bedeutung sind, unerlässlich ist. Die Wahl fiel auf eine Balance zwischen robuster Sicherheit und effizienter Performance, ohne dabei die Benutzererfahrung zu beeinträchtigen. Indem nur gehashte Passwörter gespeichert werden, schützen wir Nutzerdaten effektiv vor potenziellen Datenlecks. Gleichzeitig bleibt das System durch die effiziente Implementierung in Python und SQLite reaktionsschnell und skalierbar. Diese Strategie lässt Raum für zukünftige Erweiterungen, wie beispielsweise die Einführung einer Zwei-Faktor-Authentifizierung, ohne die Notwendigkeit, die Grundarchitektur der Anwendung umfassend zu überarbeiten.

 Entschieden von Luka

--------------------------------------------------------------------------------------------------------------------

**2. Design-Decision (Datenbankstruktur)**

Die Entscheidung zur Strukturierung der Datenbank, trotz der Vorgabe durch den Lehrer, SQLite zu verwenden, basierte auf der Notwendigkeit, eine effiziente und logisch kohärente Organisation der Daten zu gewährleisten, die die Funktionalitäten der Chat-App optimal unterstützt. Durch die Einteilung in vier Haupttabellen – User, Chatroom, Message und Support – wurde eine klare Trennung der verschiedenen Datenkategorien erreicht, die sowohl die Datenintegrität als auch die Abfrageeffizienz verbessert. Die User-Tabelle ermöglicht die eindeutige Identifikation der Benutzer, während die Chatroom-Tabelle die Grundlage für die Erstellung und Verwaltung verschiedener Chaträume bietet. Die Message-Tabelle bildet das Herzstück der Kommunikation, indem sie Nachrichten den entsprechenden Benutzern und Chaträumen zuordnet. Die Support-Tabelle schließlich dient der Verwaltung von Nutzeranfragen, was für die Nutzerbetreuung und das Feedbackmanagement essenziell ist. Diese Strukturierung unterstützt nicht nur die grundlegenden Anforderungen der App, wie Benutzerauthentifizierung, Nachrichtenübermittlung und Supportanfragen, sondern ist auch flexibel genug, um zukünftige Erweiterungen und Funktionalitäten zu integrieren. Die Entscheidung, trotz der Vorgabe von SQLite, eine solche detaillierte und durchdachte Datenbankstruktur zu entwickeln, hat uns ein tieferes Verständnis für die Anforderungen einer skalierbaren und benutzerfreundlichen Chat-App vermittelt.

--------------------------------------------------------------------------------------------------------------------
**3. Design-Decision (Frontend-Technologie)**

Die Entscheidung, das Frontend unter Verwendung bestimmter CSS-Bibliotheken zu gestalten, zeigt ein Bestreben, ein lebendiges und ansprechendes Design zu entwickeln. Ein signifikanter Teil dieser Bemühungen umfasste die Integration der Bootstrap-Bibliothek, die eine grundlegende Rolle bei der Gestaltung der Benutzeroberfläche spielte. Durch die Nutzung von Bootstrap konnten wir nicht nur die Entwicklung beschleunigen, sondern auch sicherstellen, dass unsere Webanwendung auf verschiedenen Geräten und Bildschirmgrößen reibungslos funktioniert, was essentiell für die Bereitstellung einer responsiven und zugänglichen Benutzererfahrung ist. Allerdings stellten wir fest, dass nicht alles reibungslos verlief und das responsive Design nicht immer wie erwartet funktionierte. Dennoch war diese Erfahrung nicht umsonst, denn sie ermöglichte es uns, wertvolle Erkenntnisse zu gewinnen und unsere Fähigkeiten in der Entwicklung von Benutzeroberflächen zu verbessern. Durch diese Designentscheidungen streben wir danach, die Benutzerbindung zu stärken und eine positive Wahrnehmung der Anwendung zu fördern.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

**Zu 1. Design Decision (Authentifizierungsmethode)**

Eine alternative Designentscheidung für die Authentifizierungsmethode könnte die Verwendung von OAuth sein, um die Authentifizierung über externe Dienste wie Google, Facebook oder Twitter zu ermöglichen.

| Vorteile                                   | Nachteile                                  |
|--------------------------------------------|--------------------------------------------|
| Erweiterter Zugang zu verschiedenen        | Erhöhte Komplexität der Anwendung          |
  Nutzergruppen
| Datenschutzorientierte Anmeldeoptionen     | Zusätzlicher Wartungsaufwand               |
| Spezifische Zielgruppen ansprechen         | Potenziell verwirrende Benutzererfahrung   |
|                                            | Hohe Abhängigkeit von externen Diensten    |


**Bewertung:**

Die benutzerdefinierte Authentifizierung zu entwickeln, bietet uns die Möglichkeit, tief in die Sicherheitsaspekte der Webentwicklung einzugewöhen. Es erlaubt uns, von Grund auf zu lernen, wie eigentlich Benutzerdaten sicher gespeichert und verwaltet werden. Wir können praktische Erfahrungen mit Passwort-Hashing und der Integration einer Datenbank wie SQLite sammeln. Diese Option fördert ein umfassendes Verständnis der Authentifizierungsprozesse und stärkt unsere Fähigkeiten in der Backend-Entwicklung. Allerdings ist uns bewusst, dass diese Methode zeitaufwendig sein kann und ein hohes Maß an Sorgfalt erfordert, um Sicherheitslücken zu vermeiden.

Auf der anderen Seite bietet die Implementierung von OAuth durch die Nutzung externer Dienste wie Google oder Facebook eine schnellere und möglicherweise sicherere Lösung. Diese Methode ermöglicht es uns, uns auf andere Aspekte der App-Entwicklung zu konzentrieren, da wir uns weniger um die Details der Authentifizierung kümmern müssen. OAuth könnte die Benutzerfreundlichkeit unserer App verbessern, indem es den Nutzern ermöglicht, sich mit bestehenden Konten anzumelden, was die Einstiegshürde senkt. Jedoch besteht die Sorge, dass wir durch die Wahl dieser Methode die Chance verpassen könnten, tiefergehende Kenntnisse in der Authentifizierungstechnik zu erlangen.

Letztendlich glauben wir, dass die Entscheidung für die benutzerdefinierte Authentifizierung für unser Studienprojekt am sinnvollsten ist. Trotz des potenziell höheren Aufwands und der größeren Herausforderung sehen wir darin eine wertvolle Gelegenheit, unser Verständnis und unsere Fähigkeiten in der Webentwicklung zu vertiefen. Diese Entscheidung unterstützt unser Hauptziel, durch praktische Erfahrung zu lernen, auch wenn dies bedeutet, dass wir uns intensiver mit der Behebung von Sicherheitsfragen auseinandersetzen müssen. Wir sind überzeugt, dass die damit verbundenen Lernergebnisse für unsere zukünftige Karriere als Entwickler von unschätzbarem Wert sein werden.

--------------------------------------------------------------------------------------------------------------------

**Zur 2. Design-Decision (Datenbankstruktur)**

Eine alternative Design-Entscheidung für die Datenbankstruktur könnte die Verwendung eines dokumentenorientierten Ansatzes, wie MongoDB, anstelle einer relationalen Datenbankstruktur sein.

| Vorteile                             | Nachteile                            |
|--------------------------------------|--------------------------------------|
| + Flexibilität in Datenspeicherung   | - Weniger strenge Datenintegrität    |
| + Schnelle Entwicklung               | - Komplexität bei Abfragen steigt    |
| + Skalierbarkeit                     | - Sicherheitsbedenken                |


**Bewertung:**

Die Verwendung einer dokumentenorientierten Datenbank wie MongoDB könnte in einigen Szenarien effizienter sein als die ursprüngliche relationale Struktur. Dieser Ansatz bietet Flexibilität und Skalierbarkeit für Anwendungen mit großen, variablen Datenmengen wie einer Chat-App. Jedoch können sich Herausforderungen bei der Datenintegrität und Sicherheit ergeben, da dokumentenorientierte Datenbanken weniger strenge Mechanismen bieten. Die Komplexität bei Abfragen und weniger etablierte ACID-Transaktionen sind ebenfalls zu berücksichtigen.

Nach sorgfältiger Abwägung der Vor- und Nachteile beider Ansätze kommen wir zu dem Beschluss, dass die Verwendung von SQLite besser zu den Anforderungen des Projekts und zum Schema der App selbst passt. Die Entscheidung für SQLite bietet eine solide Grundlage für eine relationale Datenbankstruktur, die gut strukturierte und miteinander verbundene Daten ermöglicht. Dies ist entscheidend für die Verwaltung von Benutzerkonten, Chatrooms, Nachrichten und Supportanfragen in unserer Chat-App. Darüber hinaus bietet SQLite eine einfachere Einrichtung und Integration, was besonders für ein Studienprojekt von Vorteil ist, das möglicherweise begrenzte Ressourcen und Zeit hat.

--------------------------------------------------------------------------------------------------------------------