# eBau Dokumentation für Codex

Fachliche Wissensgrundlage für eine Dokumentation mit Docs as Code im Kanton Thurgau  
Zusammengestellt am 12. Oktober 2026 · Version 1.0 · Fünf Kapitel entsprechend fünf PDF-Seiten

## 1 Zweck und Systemlandschaft

Diese Dokumentation überträgt das verfügbare Fachwissen zu eBau in eine eigenständig lesbare Grundlage für Codex. Sie erklärt die Anwendungen, Rollen, Abläufe und wesentlichen Regeln. Codex kann damit Dokumentationsseiten im Repository erstellen und pflegen. Sie ist keine technische Schnittstellenspezifikation und keine abschliessend geprüfte Rechtsgrundlage. Aussagen aus älteren Unterlagen und spätere Projektinformationen sind erkennbar getrennt.

### Zweck von eBau

eBau ist das digitale Baugesuchsportal des Kantons Thurgau. Gesuchstellerinnen und Gesuchsteller sowie beauftragte Personen erfassen Baugesuche, ergänzen Pläne und weitere Unterlagen und reichen das Gesuch digital bei der zuständigen Gemeinde ein. Nach der Einreichung dient eBau als Zugang zum Bearbeitungsstand, zu Mitteilungen, Nachforderungen und zum Bauentscheid. Die Gemeinde bleibt für ihr Baubewilligungsverfahren zuständig. [S1, S2, S4]

Die Einführung erfolgt gemeindeweise. Die Gemeinde entscheidet, ob und wann sie eBau einführt. Der Quick-Check zeigt, ob eine Gemeinde angeschlossen ist. Die bereitgestellten Unterlagen beschreiben Baugesuche; Bauanfragen und Vorentscheide werden als spätere Erweiterungen genannt. Eine inzwischen erfolgte Umsetzung ist daraus nicht ableitbar. [S2, S4]

### Komponenten und Datenfluss

| Komponente | Aufgabe und Verbindung |
| --- | --- |
| eBau Portal | Erfassung, digitale Einreichung und Kommunikation mit Gesuchstellenden. |
| Gemeindefachsysteme | Drei unterschiedliche Systeme im Kanton; dort werden eingegangene Baugesuche weiterbearbeitet. Die Schulung nennt eCH-0211 als Schnittstellenstandard. |
| eBau Bauverwaltung | Einfache Verwaltungsoberfläche für Gemeinden ohne eigenes Fachsystem; bietet grundlegende Funktionen zur Verwaltung von Baugesuchen. |
| BOA | Kantonales Fachsystem. Gemeinden leiten Gesuche bei Bedarf zur kantonalen Beurteilung weiter; kantonale Fachstellen bearbeiten sie in BOA. |
| Geodaten und Grundbuch | Unterstützen die Parzellenwahl, Lageprüfungen und Übernahme von Grundstücksinformationen. Im Projektkontext werden ThurGIS und TERRIS genannt. |

Der fachliche Hauptweg lautet: Erfassung in eBau, Einreichung bei der Gemeinde, Bearbeitung in deren Verwaltungssoftware und bei Bedarf Weiterleitung an BOA. Kantonale Ergebnisse gehen an die Gemeinde zurück. Die Gemeinde stellt den Bauentscheid über eBau bereit. Nicht jedes Baugesuch benötigt eine kantonale Beurteilung. [S4, K]

### Abgrenzung zu ePlan

ePlan ist die Schwesteranwendung für Planungsgeschäfte, beispielsweise Zonenplanänderungen. Berechtigte Gemeinden und Planungsbüros reichen dort unmittelbar beim Kanton ein. ePlan ist mit BOA verbunden, hat gemäss Projektkontext aber keine Schnittstellen zu Gemeindefachsystemen. Rollen, Status und Aktionen sind deshalb nicht ungeprüft von eBau auf ePlan übertragbar. [S3, K]

<!-- pagebreak -->

## 2 Benutzerkonto Rollen und Berechtigungen

### Anmeldung und elektronische Signatur

Für eBau ist ein Benutzerkonto erforderlich. Die bereitgestellten FAQ und Schulungsunterlagen beschreiben das kantonale Identity and Access Management mit Sicherheitsstufen. Stufe 1 erlaubt das Anlegen, Einsehen und Bearbeiten von Gesuchen im Rahmen der erteilten Berechtigungen. Für die Einreichung verlangen diese Unterlagen Stufe 2 sowie eine qualifizierte elektronische Signatur (QES). Stufe 3 ist keine dort genannte Voraussetzung für die eBau-Einreichung. [S2, S4]

Der dokumentierte Ablauf sieht eine Identitätsprüfung und eine digitale Signatur über fidentity vor. Die Identifikation für das Benutzerkonto und die Einrichtung der QES sind fachlich zu unterscheiden. Die FAQ nennen für die QES-Einrichtung einen ausschliesslich digitalen Weg. Öffnungszeiten, akzeptierte Ausweise und konkrete Anmeldeschritte sind versionsabhängig und dürfen nicht ohne aktuelle Prüfung in neue Anleitungen übernommen werden. [S2]

**Anstehende Änderung:** Im Projektkontext ist die Umstellung von eBau und ePlan auf AGOV ab dem 26. Oktober 2026 angekündigt. Am Zusammenstellungsdatum liegt dieser Termin noch in der Zukunft. Der alte FAQ-Text, AGOV sei erst allgemein für 2026 vorgesehen, ist damit überholt. Die konkreten Migrationsschritte und Auswirkungen auf die QES sind in den Anhängen nicht beschrieben. AGOV-Anmeldung und QES dürfen in der Dokumentation nicht gleichgesetzt werden. [K]

### Fachliche Beteiligte und Zugriff

Im Baugesuch werden Gesuchstellende, Projektverfassende und Grundeigentümerinnen oder Grundeigentümer erfasst. Die fachliche Beteiligung an einem Vorhaben ist von der Berechtigung eines Benutzerkontos zu unterscheiden. Die Zustimmung auf dem Unterschriftenblatt ersetzt keine Zugriffsberechtigung in eBau. [S2, S4]

| Rolle oder Recht | Dokumentierter Funktionsumfang |
| --- | --- |
| Erstellende Person | Kann weitere Personen berechtigen und deren Rechte ändern oder entziehen. Die Berechtigungsverwaltung ist gemäss Unterlagen dem Ersteller vorbehalten. |
| Person mit Schreibrechten | Kann im bearbeitbaren Zustand Angaben ändern und einreichen, Mitteilungen lesen und senden sowie E-Mail-Benachrichtigungen erhalten. Für das Einreichen gelten zusätzlich die Identitäts- und Signaturvoraussetzungen. |
| Person mit Leserechten | Kann das Gesuch einsehen, aber nicht bearbeiten; hat keinen Zugriff auf Mitteilungen und erhält gemäss Schulung keine Änderungsbenachrichtigungen. |
| Gemeindebehörde | Bearbeitet das Verfahren, steuert Statusmeldungen, fordert Unterlagen nach und stellt den Entscheid bereit. |

Eine Berechtigung wird auf eine E-Mail-Adresse erteilt. Diese muss mit der registrierten Adresse des Benutzerkontos übereinstimmen. Bei fehlendem Zugriff sind daher Adresse und Fortbestand der Berechtigung zu prüfen. Die Verwaltung erfolgt im Reiter «Berechtigungen» oder über «Zugriffsberechtigungen anpassen» in der Zentrale. [S2, S4]

### Zustimmung von Drittpersonen

Bei unterschiedlichen Beteiligten ist deren Zustimmung nachzuweisen. eBau kann ein Unterschriftenblatt aus den Beteiligtenangaben erzeugen. Ein eigenes Dokument ist ebenfalls möglich, sofern das Vorhaben eindeutig identifizierbar ist. Es kann handschriftlich oder mit QES unterschrieben werden. Bei handschriftlichen Unterschriften kann die Gemeinde das Original verlangen. [S1, S2]

<!-- pagebreak -->

## 3 Gesuch erfassen und einreichen

### Erfassung und Lage

Neue Gesuche werden über die Übersicht angelegt. Angaben werden automatisch gespeichert; die Bearbeitung kann unterbrochen und später fortgesetzt werden. Pflichtfelder sind mit einem Sternchen markiert. Hilfetexte erscheinen über das Informationssymbol. «Meine Gesuche» zeigt nach der Anmeldung die Gesuche, für die das Konto berechtigt ist. [S2, S4]

Die Parzellenwahl bestimmt die zuständige Gemeinde. Gemäss Schulung sind nur Parzellen angeschlossener Gemeinden auswählbar. Mehrere ausgewählte Parzellen müssen in derselben politischen Gemeinde liegen. Grundstücks- und Lageinformationen werden teilweise automatisch bezogen. Angaben zu Grundeigentümern können aus dem Grundbuch übernommen werden. Diese Hilfen ersetzen keine fachliche Kontrolle der Eingaben. [S4]

### Umfangsfragen und Formulare

Die Triage unterstützt eine möglichst vollständige Einreichung. Die Antworten auf Umfangsfragen bestimmen, welche Formulare erforderlich und sichtbar sind. Zusätzlich können allgemeine Angaben und die Lage der Parzelle Formulare oder Fragen auslösen. Die Schulung nennt landwirtschaftliche Fragen bei entsprechender Nutzung, lageabhängige Anforderungen in Grundwasserschutzgebieten sowie Nutzungsziffern bei bestimmten Neubauten mit Wohnnutzung als Beispiele. [S4]

eBau enthält digital erfasste Formulare, aus denen PDFs erzeugt werden, und Anforderungen, die über PDF-Uploads erfüllt werden. Pläne und weitere Anhänge ergänzen das Gesuch. Wird bei einer Nachforderung ein zusätzliches Formular benötigt, kann gemäss Schulung eine Anpassung der Umfangsantworten erforderlich sein. [S4]

**Weiterentwicklung:** Eine individuelle Aktivierung der Formulare per Toggle, getrennt von den Fragen als Hilfestellung, wurde im Projekt diskutiert. Die bereitgestellten Unterlagen belegen keine Umsetzung. Codex muss diese Variante als Anforderung behandeln, bis ein aktueller Produktstand bestätigt ist. [K]

### Vollständigkeit und Einreichung

Vor der Einreichung prüft eBau die technische Vollständigkeit. Fehlende Elemente werden markiert. Erst wenn die erforderlichen Angaben und Unterlagen vorliegen, kann eingereicht werden. Eine bestandene Vollständigkeitsprüfung ist keine materielle Prüfung der Bewilligungsfähigkeit. Danach folgt der Signaturprozess; das signierte Gesuch wird an die Gemeinde übermittelt. Nach der Einreichung ist die Bearbeitung gesperrt, bis die Gemeinde das Gesuch zur Ergänzung öffnet. [S2, S4]

Im Projektkontext ist ein einstündiges Zeitfenster für den QES-Einreichungsprozess dokumentiert. Wird dieser nicht abgeschlossen, gilt das Gesuch nicht als erfolgreich eingereicht. Der genaue aktuelle Ablauf ist vor Veröffentlichung zu prüfen. Für Anleitungen ist entscheidend, den Abschluss anhand der Rückkehr ins Portal und des Gesuchstatus zu kontrollieren. [K]

### Baugesuch PDF und Versionen

Das Baugesuch-PDF ist in der Zentrale abrufbar. Es enthält allgemeine Angaben, Lageinformationen, Antworten auf Umfangsfragen und eine Auflistung der zugehörigen Dokumente. Die QES der einreichenden Person wird darin hinterlegt. Fachspezifische Formulare werden separat erzeugt und ebenfalls übermittelt. Das Deckblatt nennt die einreichende Person, den Zeitpunkt und die Version. [S4]

Beim erneuten Einreichen erhöht sich die Gesuchversion; generierte Formulare erhalten neue Versionen. Eine UUID identifiziert ein Dokument, ein Hash beschreibt dessen Inhalt als technischen Prüfwert. Diese Kennungen sind keine Gesuchnummern. [S2, S4]

<!-- pagebreak -->

## 4 Verfahren Kommunikation und Entscheid

### Die Zentrale und Identifikationsnummern

Die «Zentrale» ist der Übersichtsbereich eines Gesuchs. Sie zeigt Stammdaten, den Status, Mitteilungen, Dokumente und die jeweils verfügbaren Aktionen. Die eBau-Nr. identifiziert das Gesuch im Portal. Die BG-Nr. Gemeinde stammt aus der gemeindeseitigen Bearbeitung. Die BG-Nr. Kanton wird bei einer Weiterleitung an den Kanton vergeben. Die Schulung nennt an einer Stelle irrtümlich die Übermittlung an die Gemeinde als Auslöser; hier wird der konsistente Ablauf aus FAQ und Projektkontext verwendet. [S2, S4, K]

### Status und Handlungsbedarf

Die folgende Auswahl beschreibt zentrale Zustände. Sie ist keine vollständige technische Statusliste und keine Festlegung aller zulässigen Übergänge. Status und einzelne Mitteilungstypen werden in der Schulung teilweise gemeinsam aufgeführt. [S2, S4]

| Status | Bedeutung und Handlung |
| --- | --- |
| Entwurf | Noch nicht eingereicht; bearbeitbar und durch die berechtigte Person löschbar. |
| Eingereicht | Bei der Gemeinde eingereicht; Angaben sind gesperrt. |
| In Verfahren | Die Gemeinde hat die Bearbeitung eröffnet. |
| Unterlagen nachgefordert | Gemeinde verlangt Ergänzungen; Gesuch ist wieder bearbeitbar und anschliessend erneut einzureichen. |
| Unterlagen nachgefordert bei Gemeinde | Kanton verlangt Ergänzungen von der Gemeinde. Gesuchstellende müssen erst handeln, wenn die Gemeinde sie auffordert. |
| Sistiert oder Zurückgezogen | Gemeinde setzt den entsprechenden Status; der Wunsch wird ihr über eine Mitteilung übermittelt. |
| Entscheid erteilt | Entscheid ist über das Portal bereitgestellt. |
| Rechtsmittelverfahren | Ein Rechtsmittelverfahren zum Vorhaben wird angezeigt. |
| Entscheid rechtskräftig oder Im Bau | Rechtskraft beziehungsweise Bauphase wird angezeigt. Bauvorgänge können gemäss Schulung ab Rechtskraft gemeldet werden. |

### Mitteilungen und Nachforderungen

Nach der Einreichung können Personen mit Schreibrechten Mitteilungen an die Gemeinde senden. Diese gehen an die gemeindeseitige Verwaltungssoftware. E-Mails informieren ergänzend über Änderungen und Mitteilungen; sie werden an die registrierte Konto-Adresse gesendet und können unter Benutzerkonto > Benachrichtigungen deaktiviert werden. Leserechte umfassen die Mitteilungen nicht. [S2, S4]

Bei einer Nachforderung werden Angaben oder Unterlagen im geöffneten Gesuch ergänzt und das Gesuch erneut eingereicht. Die Schulung beschreibt auch Nachreichungen ausserhalb dieses Ablaufs: Ohne erneutes Einreichen bleibt der Nachforderungsstatus bestehen; die Gemeinde muss das Gesuch dann wieder in Verfahren setzen. Dieser Sonderfall sollte in einer Gemeindeanleitung separat erklärt werden. [S4]

Weiterleitung an den Kanton und Abschluss der kantonalen Bearbeitung erzeugen automatische Mitteilungen. Die dabei zwischen BOA und Gemeinde übermittelten Dokumente sind gemäss Schulung für Gesuchstellende nicht automatisch sichtbar. [S4]

### Entscheid und Zustellung

Die Gemeinde stellt Entscheid und zugehörige Unterlagen digital bereit. Die Handlungsempfehlung verlangt dafür QES-signierte Dokumente. FAQ und Schulung beschreiben die Zustellung durch Download beziehungsweise die Zustellfiktion am siebten Tag nach Bereitstellung. Der erste Download eines Entscheid-Dokuments löst eine Benachrichtigung an das Gemeindesystem aus; Downloads werden protokolliert. Diese rechtlich relevante Beschreibung ist vor einer Veröffentlichung anhand der geltenden Grundlagen und des aktuellen Systems zu bestätigen. [S1, S2, S4]

<!-- pagebreak -->

## 5 Betrieb Quellen und Arbeit im Repository

### Gemeindeprozess und Datenhaltung

Die Handlungsempfehlung will Medienbrüche minimieren. Zusätzliche Papierexemplare sollen möglichst vermieden werden; Originale handschriftlicher Unterschriftenblätter und grossformatige Pläne können verlangt werden. Sie beschreibt eine gemeindeseitige Stellungnahme samt Prüfbestätigung, die das Gesuch eindeutig über die eBau-ID zuordnet. Für diese Stellungnahme verlangt sie keine QES, für kantonale Stellungnahmen hingegen schon. Diese Unterscheidung darf in Anleitungen nicht eingeebnet werden. [S1]

Für die Pilotphase empfiehlt S1 die öffentliche Einsicht über eine Computerstation oder Papierunterlagen sowie digitale Baukontrollen mit Tablets. Eine digitale öffentliche Auflage ist dort erst vorgesehen. Der spätere Projektkontext nennt die Arbeit an einer entsprechenden eBau-Komponente. Daraus folgt kein bestätigter Produktivbetrieb. [S1, K]

Die FAQ nennen das kantonale Rechenzentrum als Speicherort und verschlüsselte Übertragung. Sie dokumentieren die Löschung nicht eingereichter Gesuche nach einem Jahr ohne Änderung, mit vorheriger E-Mail-Warnung. Eingereichte Gesuche werden nach gemeindeseitiger Archivierung aus eBau gelöscht. Die Schulung nennt dafür zwei Wochen, während die FAQ keinen konkreten Zeitraum nennen. Die aktuelle Frist bleibt zu prüfen. Portalablage und Langzeitarchivierung sind getrennte Aufgaben. Hostingdetails, Sicherungskopien, Aufbewahrungsfristen und Datenflüsse externer Dienste sind nicht vollständig belegt. [S1, S2, S4]

### Support und Betriebsorganisation

Gemeinden sind erster Kontakt für fachliche und einfache Anwendungsfragen. Das eBau-Team unter ebau@tg.ch bearbeitet technische Anliegen und koordiniert die zuständigen Systemverantwortlichen, unter anderem AFI und technische Dienstleister. Die Schulung nennt ebau.tg.ch als Produktion, ebau-qs.tg.ch für Schulung und Qualitätssicherung sowie ebau-test.tg.ch für Entwicklungstests. [S2, S4]

Gemäss Projektinformation ist das Projekt abgeschlossen; die Anwendungen sind seit Ende 2025 produktiv. Die offizielle Übergabe an die Politische Steuerung eTG erfolgte im September 2026. Eine paritätische Betriebsorganisation führt Betrieb und Weiterentwicklung. Diese Angaben ergänzen die älteren Anhänge. [K]

### Quellen und Verbindlichkeit

| Kennung | Grundlage |
| --- | --- |
| S1 | eBau_Pilot_Handlungsempfehlungen_Gemeinden.pdf, Version 0.3 vom 25. Juli 2025, insbesondere Seiten 2 bis 4. |
| S2 | Manuskript_FAQ_#30389.docx, bereitgestelltes FAQ-Manuskript; verlässlicher Versionsstand nicht ersichtlich. |
| S3 | ePlan_Manuskript_FAQ.docx, zur Abgrenzung von ePlan; Versionsstand nicht ersichtlich. |
| S4 | eBau_Schulung.pptx, 78 Folien; insbesondere 6 bis 10, 20 bis 22, 25 bis 37 und 42 bis 75. |
| K | Vom Auftraggeber bereitgestellter Projekt- und Gesprächskontext, zusammengeführt am 12. Oktober 2026; keine zusätzlich geprüfte Produktspezifikation. |

Die Zusammenstellung beruht auf diesen Quellen, ohne externe Prüfung. Aussagen aus Manuskripten sind nicht automatisch freigegebene öffentliche Texte. Konkrete Rechtsverweise aus S1 und pauschale Sicherheitsversprechen aus S2 wurden deshalb nicht als aktuelle verbindliche Aussagen übernommen.

### Empfohlener Auftrag an Codex

Verwende diese Datei als fachlichen Kontext. Erstelle daraus getrennte Dokumentationsseiten für Überblick, Gesuchstellende, Gemeinden und Betrieb. Bewahre die Quellenkennungen. Schreibe Schweizer Standarddeutsch und verwende die UI-Begriffe konsistent. Trenne bestätigte Funktionen, historische Abläufe und geplante Änderungen. Kennzeichne fehlende Informationen als offene Prüfpunkte; erfinde keine Endpunkte, XML-Strukturen, Statusübergänge oder rechtlichen Regeln. Prüfe vor Veröffentlichung insbesondere AGOV und QES, öffentliche Auflage, Formularaktivierung sowie Lösch- und Zustellungsregeln. Empfohlener Ablageort dieser Wissensgrundlage ist docs/kontext/eBau_Kontext_fuer_Codex.md.
