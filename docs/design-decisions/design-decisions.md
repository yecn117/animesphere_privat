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

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

**1. Problemstellung: Auswahl einer geeigneten Authentifizierungsmethode:**

Das Ziel dabie wäre die Implementierung einer sicheren, benutzerfreundlichen und effizienten Methode zur Authentifizierung potentiellen Usern, die es ihnen ermöglicht, sich registrieren und anmelden zu können, um auf die App und ihre Funktionen, wie das Durchstöbern der Chatrooms und das Senden von Nachrichten, zugreifen zu können.

**Sicherheit:** Die Authentifizierungsmethode muss sicherstellen, dass Benutzerdaten geschützt sind und unbefugter Zugriff verhindert wird.

**Benutzerfreundlichkeit:** Die Methode sollte einfach und intuitiv sein, um eine hohe Akzeptanz bei den Benutzern zu erreichen und den Registrierungs- sowie Anmeldeprozess so reibungslos wie möglich zu gestalten.

**Skalierbarkeit:** Die gewählte Lösung sollte in der Lage sein, mit einer wachsenden Anzahl von Benutzern umzugehen, ohne an Leistung zu verlieren.



**2. Problemstellung: Auswahl einer geeigneten Authentifizierungsmethode:**

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

 **1. Design-Decision (Authentifizierungsmethode)**

 Wir fokussierten uns auf die Implementierung einer sicheren und benutzerfreundlichen Authentifizierungsmethode unter Verwendung von Passwort-Hashing mit pbkdf2:sha256. Diese Entscheidung basierte auf dem Bedürfnis, ein hohes Sicherheitsniveau zu gewährleisten, indem Nutzerpasswörter sicher gespeichert werden, was besonders in der heutigen Zeit, in der Datenschutz und Sicherheit von größter Bedeutung sind, unerlässlich ist. Die Wahl fiel auf eine Balance zwischen robuster Sicherheit und effizienter Performance, ohne dabei die Benutzererfahrung zu beeinträchtigen. Indem nur gehashte Passwörter gespeichert werden, schützen wir Nutzerdaten effektiv vor potenziellen Datenlecks. Gleichzeitig bleibt das System durch die effiziente Implementierung in Python und SQLite reaktionsschnell und skalierbar. Diese Strategie lässt Raum für zukünftige Erweiterungen, wie beispielsweise die Einführung einer Zwei-Faktor-Authentifizierung, ohne die Notwendigkeit, die Grundarchitektur der Anwendung umfassend zu überarbeiten.

 Entschieden von Luka


### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

**Zu 1. Design Decision**

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
---