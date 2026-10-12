# API und Fachsystemintegration

## Quelle und Geltungsbereich

Die öffentlich abrufbare API-Dokumentation der Testumgebung wurde am **12. Oktober 2026** geprüft. Sie beschreibt HTTP-Dienste für eBau/ePlan, insbesondere den Austausch von eCH-0211-Nachrichten mit Fachsystemen. Die Spezifikation verwendet OpenAPI 3.0.0 und nennt die Dokumentversion 1.0.0. Ein Quellenstand liegt im Repository unter `docs/api/ebau-api.swagger.json`. [A1]

Diese Prüfung betrifft die Dokumentation, keine authentifizierten Funktionstests. Es wurden keine Gesuche abgerufen, Dateien hochgeladen oder Nachrichten versendet. Der dokumentierte Stand der Testumgebung bestätigt weder die Verfügbarkeit jeder Funktion in Produktion noch rechtliche Abläufe. Die API-Anmeldung ist von der Benutzeranmeldung mit IAM/AGOV und der QES zu unterscheiden. [A1]

## Anmeldung und Umgebungen

Die meisten Operationen benötigen einen Session-Token im Header `Authorization: Bearer <token>`. `POST /api/v1/login` nimmt `username` und `password` als `application/x-www-form-urlencoded` entgegen und liefert bei Erfolg einen Token. `POST /api/v1/logout` beendet die Session; die Spezifikation verlangt auch dort ein Formular mit Benutzername und Passwort. Eine Token-Laufzeit ist nicht angegeben. [A1]

Für Produktion (`ebau.tg.ch`) und Integration/Qualitätssicherung (`ebau-qs.tg.ch`) nennt die Quelle zusätzlich ein Client-Zertifikat für mTLS. Das Zertifikat ist einer Gemeinde zugeordnet und hat laut Quelle eine Laufzeit von fünf Jahren, sofern es nicht vorher widerrufen wird. Der konkrete Bezugsprozess ist als «TBD» offen. Für das Testsystem enthält dieser Abschnitt keine entsprechende Zusage. [A1]

## Dokumentierte HTTP-Operationen

Die Pfade beziehen sich auf die jeweils freigegebene Zielumgebung. Zugang und Berechtigungen sind mit dem Betrieb zu klären. [A1]

| Methode und Pfad | Zweck |
| --- | --- |
| `POST /api/v1/login` | Session-Token beziehen. |
| `POST /api/v1/logout` | Session beenden. |
| `GET /api/v1/application/{id}` | Vollständige eCH-0211-`baseDelivery` für ein Baugesuch oder Planungsgeschäft anhand der eBau-ID abrufen. |
| `GET /api/v1/message/` | Nachricht der zugeordneten Gemeinde abrufen; `last` ist die zuletzt verarbeitete Nachrichten-ID. Ohne `last` wird die erste Nachricht geliefert. |
| `GET /api/v1/message/{id}` | Einzelne Nachricht anhand ihrer ID erneut abrufen; siehe Unstimmigkeit unten. |
| `POST /api/v1/send/` | XML-Nachricht als `application/xml` in einer eCH-0211-Delivery senden. Die Erfolgsantwort enthält unter anderem `ebauId` und `ebauDisplayStatus`. |
| `POST /api/v1/addDocument/{id}` | Datei einem Baugesuch/Planungsgeschäft zuordnen; `{id}` ist die eBau-ID, `filename` ein erforderlicher Query-Parameter. Die Antwort enthält UUID und API-/UI-Links. |

Zusätzlich beschreibt der Erläuterungstext `GET /api/v1/file/{id}` für Dateidownloads anhand einer numerischen Dokument-ID oder einer gültigen UUID. Dieser Pfad fehlt in der formalen `paths`-Liste. Der Zugriff erfordert Leserechte auf das Dokument. [A1]

## Nachrichtenwarteschlange und Identifikation

Nachrichten werden bei Ereignissen in eBau in einer Warteschlange abgelegt und einer Organisation/Gemeinde adressiert. API-Benutzer sind einer Gemeinde zugeordnet und können nur deren Nachrichten beziehen. Die letzte Nachrichten-ID ist laut Parameterbeschreibung unter `delivery.deliveryHeader.messageId` zu finden. Der Erläuterungstext beschreibt sequenziellen Abruf und erneuten Abruf einer bestimmten Nachricht; ein separater Bestätigungs- oder Löschendpunkt ist nicht dokumentiert. [A1]

Das Gesuch wird im XML über `otherID` mit `IdCategory` = `ebauId` identifiziert; die Quelle beschreibt auch die Verarbeitung von `localID` für dieselbe Kennung. `dossierNrGemeinde` in `localID` liefert beim ersten «in progress»-Status die gemeindeseitige Nummer. `ebauDisplayStatus` enthält den angezeigten Portalstatus und ist nicht zwingend ein eCH-Statuswert. Gemeinden werden anhand ihrer UID identifiziert. [A1]

`intendedPurpose` kann mehrere englische Werte als kommaseparierte Liste enthalten: `residential_use`, `commercial_and_industrial_use`, `agricultural_use`, `public_use`, `other_use`. Dies ist eine in der Quelle beschriebene Verwendung eines einzelnen XML-Knotens. [A1]

## Fachliche Nachrichten und Besonderheiten

Für die Geschäftslogik ist der Ereignisknoten massgebend: Der `messageType` im eCH-0058-Header wird laut Quelle nur aus Kompatibilitätsgründen gesetzt und darf nicht als fachlicher Nachrichtentyp interpretiert werden. Die folgenden Codes stammen aus den fachlichen Nachrichtentabellen der API-Dokumentation. [A1]

| Ereignis / Code | Verwendung |
| --- | --- |
| `submit` / `11001` | Einreichung von eBau an das Gemeindefachsystem. |
| `file subsequently` / `07001` | Nachreichung von Unterlagen an die Gemeinde. |
| `claim` / `05001` | Nachforderung; vom Kanton an die Gemeinde oder von der Gemeinde an Gesuchstellende. |
| `task` / `12001` | Weiterleitung an den Kanton sowie Erfüllung kantonaler Nachforderungen. |
| `task` / `12002`, `12003`, `12006` | Mitteilung von Gemeinde an Gesuchstellende, von Gesuchstellenden an Gemeinde beziehungsweise von Kanton an Gemeinde. |
| `notice ruling` / `09003` | Übermittlung des Entscheids; der Erläuterungstext verlangt die Bemerkung im Element `ruling`. |
| `status notification` / `10102` | «in progress», gegebenenfalls mit Gemeindenummer und Verfahrensart. |
| `task` / `12100` | Publikation für ein Baugesuch starten oder bearbeiten/ersetzen, mit `publicationType`. |
| `task` / `12101` | Alle Publikationen eines Baugesuchs entfernen. |

Zwischen BOA und Gemeindefachsystem beschreibt die API keine direkte Kommunikation: Nachrichten laufen über eBau. Da BOA Bemerkungen nicht anzeigen oder erfassen kann, werden kantonale Mitteilungen als Dokumente übertragen. Eine kantonale Nachforderung wird über die Gemeinde abgewickelt, nicht direkt an Gesuchstellende. [A1]

Entscheidinhalt und Status werden getrennt übertragen: Für «Entscheid erteilt» nennt die Quelle `notice ruling` plus eine Statusnachricht; für «Entscheid rechtskräftig» eine weitere Statusnachricht. Bei «objection pending» erlaubt eBau Dokumente an der Statusnachricht und beschreibt dies als Abweichung vom eCH-Standard. Statusänderungen erfolgen gemeindeseitig; Einreichen und erneutes Einreichen sind die beschriebenen Ausnahmen auf Seite der Gesuchstellenden. [A1]

Die Erweiterung `proceedingType` akzeptiert `Ordinary procedure` und `Simplified procedure`. `publicationType` beschreibt unter anderem Parzelle, Titel, Zone, Adresse, Publikationsbeginn und -ende sowie Beteiligte. Die dokumentierten Publikationsnachrichten ergänzen den bisherigen Projektkontext; ein produktiver Betrieb der öffentlichen Auflage bleibt zu bestätigen. Die Sistierungserweiterung wird als kantonsseitige Referenz beschrieben; gegenüber Drittsystemen verwendet eBau/ePlan nur einen Ein-/Aus-Zustand. [A1]

## Dokumente, Upload und Versionierung

Die Quelle nennt **100 MB für API-Uploads** und **50 MB für Uploads in der Benutzeroberfläche**. Dateien werden zuerst hochgeladen und anschliessend in eCH-Nachrichten über ihre UUID referenziert. UUID und Gesuchnummer sind unterschiedliche Identifikatoren. [A1]

- Eine gültige, noch nicht verwendete UUID wird übernommen.
- Ohne UUID prüft eBau auf denselben Datei-Hash innerhalb des Gesuchs. Bei einem Duplikat wird die bestehende UUID zurückgegeben.
- Bei vorhandener UUID und geändertem Datei-Hash entsteht eine neue Dokumentversion. UUID und interne Dokument-ID bleiben gleich; der bisherige Inhalt wird als separate Version aufbewahrt.
- Erzeugte Nachrichten enthalten Version und Hash; ohne Versionsangabe setzt die Quelle Version 0 an. Das Beispiel verwendet `sha256`.

Die Quelle bezeichnet erzeugte UUIDs als Version 7, verwendet dabei jedoch die Bezeichnung «RFC 4122 Version 7». Dies ist eine terminologische Unstimmigkeit und keine hier geprüfte Normkonformität. Dokumentkategorien werden über `documentKind` übertragen; sie können laut Quelle über die öffentliche API nicht gesetzt oder geändert werden. [A1]

## Fehlerbehandlung und offene technische Fragen

Anwendungsfehler werden laut Beschreibung wegen der WAF mit HTTP 400 zurückgegeben. Clients müssen deshalb zusätzlich `success` sowie `error.code` und `error.msg` auswerten. Ein HTTP-Status allein genügt nicht zur fachlichen Fehlerdiagnose. Die Quelle nennt beispielsweise Code `104` für ein nicht gefundenes Gesuch, `1000` für einen unbekannten Status und `1001` für einen unzulässigen Statusübergang. [A1]

Vor einer Implementierung sind folgende Unstimmigkeiten zu klären: [A1]

- Beim Upload ist `uuid` als optionaler Path-Parameter deklariert, obwohl der Pfad keinen UUID-Platzhalter enthält. Das Multipart-Request-Body-Schema fehlt. Einen verbindlichen Upload-Aufruf kann man daraus nicht ableiten.
- `GET /api/v1/message/{id}` ist im Operationstext als Abruf der nächsten Nachricht beschrieben, im allgemeinen Text jedoch als erneuter Abruf einer bestimmten Nachricht. Auch die Parameterbeschreibung verwendet uneindeutig «eBau-ID».
- Der Downloadpfad ist nur im Erläuterungstext vorhanden. Einige Operationen enthalten ältere `consumes`-/`produces`-Felder innerhalb der OpenAPI-3-Datei; generierte Clients benötigen daher eine gesonderte Prüfung.
- Die Fehlerübersicht nennt `404` für «Zugriff verweigert», das Access-Denied-Beispiel `403`; `404` wird an anderer Stelle auch für «file not found» verwendet. HTTP- und Anwendungsfehlercodes sind getrennt zu behandeln.
- Zertifikatsbezug, Session-Laufzeit, Abruf bei leerer Queue, Retry-/Duplikatverhalten beim Senden, Limits und produktiver Funktionsstand sind nicht abschliessend spezifiziert.

Die vollständige Referenz mit weiteren Statusnachrichten, XML-Beispielen und Wertelisten ist unter [API-Dokumentation](https://ebau-test.tg.ch/api-doc/index.html) und als [OpenAPI-Datei](https://ebau-test.tg.ch/api-doc/ebau-api.swagger.json) verfügbar. [A1]
