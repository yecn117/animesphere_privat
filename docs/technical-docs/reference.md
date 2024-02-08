---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
[Jane Dane]

# [Reference documentation]
{: .no_toc }


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [Section / module]
-------------------------------------------------------------------------------------------------------------
### `func submit_support_request():`

**Route:** `/submit_support_request/`

**Methods:** `POST`

**Purpose:** 

**Anwendungszweck:** Die Funktion verarbeitet POST-Anfragen an die Route /submit_support_request. Wenn ein Benutzer über ein Formular auf der Website Support anfordert, werden die eingegebenen Informationen wie Name, E-Mail, Betreff und Nachricht aus dem Formular ausgelesen.

**Verarbeitung der Anfrage:** Die Funktion überprüft, ob alle erforderlichen Felder ausgefüllt wurden. Falls nicht, wird eine Fehlermeldung angezeigt und der Benutzer zurück zur Kontaktseite geleitet.

**Speichern der Anfrage:** Wenn alle Felder ausgefüllt sind, wird eine neue Support-Anfrage in der Datenbank erstellt und gespeichert.

**Weiterleitung und Erfolgsmeldung:** Nach erfolgreicher Verarbeitung der Anfrage wird der Benutzer zur Kontaktseite weitergeleitet und erhält eine Erfolgsmeldung. (Wichtig!: Aus wahrscheinlich tüchtigen Fehler, vielleicht auch ein Tippfehler wird zwar keine Erfolgsmeldung, wie vorgesehen angezeigt, jedoch werden die Daten an die Datenbank weitergeleitet und gespeichert. Eine Fehlermeldung zur einer Supportanfrage wird trotzdem angezeigt.)
                                      

**Sample output:**

Erfolgsmeldung (normalerweise): 'Your support request has been submitted successfully.'
Fehlermeldung: 'All fields are required.'

-------------------------------------------------------------------------------------------------------------

