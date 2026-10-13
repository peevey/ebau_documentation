# Überblick und Systemlandschaft

## Zweck von eBau

eBau ist das digitale Baugesuchsportal des Kantons Thurgau. Gesuchstellerinnen und Gesuchsteller sowie beauftragte Personen erfassen Baugesuche, ergänzen Pläne und weitere Unterlagen und reichen das Gesuch digital bei der zuständigen Gemeinde ein. Nach der Einreichung dient eBau als Zugang zum Bearbeitungsstand, zu Mitteilungen, Nachforderungen und zum Bauentscheid. Die Gemeinde bleibt für ihr Baubewilligungsverfahren zuständig. [S1, S2, S4]

Die Einführung erfolgt gemeindeweise. Die Gemeinde entscheidet, ob und wann sie eBau einführt. Der Quick-Check zeigt, ob eine Gemeinde angeschlossen ist. Die bereitgestellten Unterlagen beschreiben Baugesuche; Bauanfragen und Vorentscheide werden als spätere Erweiterungen genannt. Eine inzwischen erfolgte Umsetzung ist daraus nicht ableitbar.

Ich möchte hier noch einen **fetten Text** haben und hier etwas *kursives*. [S2, S4]

## Komponenten und Datenfluss

| Komponente | Aufgabe und Verbindung |
| --- | --- |
| eBau Portal | Erfassung, digitale Einreichung und Kommunikation mit Gesuchstellenden. |
| Gemeindefachsysteme | Drei unterschiedliche Systeme im Kanton; dort werden eingegangene Baugesuche weiterbearbeitet. Die Schulung nennt eCH-0211 als Schnittstellenstandard. |
| eBau Bauverwaltung | Einfache Verwaltungsoberfläche für Gemeinden ohne eigenes Fachsystem; bietet grundlegende Funktionen zur Verwaltung von Baugesuchen. |
| BOA | Kantonales Fachsystem. Gemeinden leiten Gesuche bei Bedarf zur kantonalen Beurteilung weiter; kantonale Fachstellen bearbeiten sie in BOA. |
| Geodaten und Grundbuch | Unterstützen die Parzellenwahl, Lageprüfungen und Übernahme von Grundstücksinformationen. Im Projektkontext werden ThurGIS und TERRIS genannt. |

Der fachliche Hauptweg lautet: Erfassung in eBau, Einreichung bei der Gemeinde, Bearbeitung in deren Verwaltungssoftware und bei Bedarf Weiterleitung an BOA. Kantonale Ergebnisse gehen an die Gemeinde zurück. Die Gemeinde stellt den Bauentscheid über eBau bereit. Nicht jedes Baugesuch benötigt eine kantonale Beurteilung. [S4, K]

## Abgrenzung zu ePlan

ePlan ist die Schwesteranwendung für Planungsgeschäfte, beispielsweise Zonenplanänderungen. Berechtigte Gemeinden und Planungsbüros reichen dort unmittelbar beim Kanton ein. ePlan ist mit BOA verbunden, hat gemäss Projektkontext aber keine Schnittstellen zu Gemeindefachsystemen. Rollen, Status und Aktionen sind deshalb nicht ungeprüft von eBau auf ePlan übertragbar. [S3, K]
