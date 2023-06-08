Empfohlene neue Ansätze zur Darstellung von Daten:

https://academic.oup.com/bib/article/13/5/627/412507

https://plotly.com/python/sankey-diagram/


Was wir bis jetzt getan haben und was wir als nächstes tun wollen:

Wir haben bereits die Grundlage dafür erarbeitet, wie wir die Rohdaten erhalten, sie analysieren und aussagekräftige Informationen präsentieren können. Wir haben uns unterschiedliche Python-Bibliothek, z.B. Circos Plot angeschaut und erste Visulaisierungen erstellt. Das meiste bedarf an Verbesserung. Da uns für die Circos Plots eine gute Dokuemntation fehlte, besteht der nächste Schritt darin, das Gelernte auf die empfohlenen Plot-Bibliotheken zu übertragen.


Um eine bessere Übersicht zu schaffen, ist unser Schritt 

1. github mit Ordnern strukturieren
2. how to: die Struktur von Scholia und Wikidata versteht
3. how to: Sankey-Diagramm
4. Übertragen der erarbeiteten Ansätze in ein Sankey-Diagramm
5. how to: Hive-Diagramm
6. Übertragen der erarbeiteten Ansätze in ein Hive Plot
7. Diskussion der Ergebnisse --> Bei der Durchführung des Workflows haben wir festgestellt, dass uns ein konkretes Ziel fehlte. Dies liegt an den nicht immer vorhandenen Daten auf Wikidata und unserer Versuche, stets unterschiedliche Krankheiten und Metriken zu analysieren.



Definition von Zielen:

- Die Prävalenz von bestimmten Krankheiten in verschiedenen Altersgruppen und Geschlechtern.
- Die Assoziation von bestimmten Genen mit bestimmten Krankheiten.
- Die Häufigkeit von Komorbiditäten bei Patienten mit bestimmten Krankheiten.
- Die Rolle von Umweltfaktoren bei der Entstehung bestimmter Krankheiten.
- Die Auswirkungen von bestimmten Medikamenten auf die Symptome von Krankheiten.
- Die geographische Verteilung von Krankheiten auf der Weltkarte.
- Die Häufigkeit von bestimmten Symptomen bei Patienten mit bestimmten Krankheiten.
- Die Verbindung von bestimmten Krankheiten mit sozioökonomischen Faktoren wie Bildung und Einkommen.
- Die Entwicklung der Häufigkeit von bestimmten Krankheiten im Laufe der Zeit.
- Die Verwendung von bestimmten Biomarkern zur Diagnose und Überwachung von Krankheiten.


Fragen:
- Sollen wir uns auf eine bestimmte Krankheit fokussieren oder auf die verschiedenen Krankheiten verknüpfen?
- Haben wir die nötigen Daten dafür? (also mehr als nur die "possibly related diseases" zu implementieren)
<br>



__UPDATE:__

Das ursprüngliche Projektziel ist ein Circos Plot gewesen. Nun wollen wir ein Dashboard mit mehreren Visualisierungen erstellen.


*Alte Zielformulierung:*

__Wir visualisieren die verschiedenen Krankheiten__, welche auf https://scholia.toolforge.org/  vorhanden sind.
Wir konzentrieren uns dabei auf die Circos Plots, um die Verbindungen der Krankheiten und deren Paper zu visualisieren. 
Das ideale Ergebnis ist eine vollständige Visualisierung aller Krankheiten, die auf Scholia zu finden sind. Die Visualisierung soll dabei sehr aufschlussreich sein und sehr viele Informationen beinhalten, ohne die Übersichtlichkeit zu verringern. Im Idealfall ist die Visualisierung so gut, dass sie bei Scholia integriert werden kann. <br>


Die Zielformulierung hat in der Gruppe zu unkalren Arbeitsschritten geführt. Durch die ungenaue Fomulierung hatte jeder unterschiedliche Ideen zur Umsetzung. Dieses Problem wollten wir in einer neuen Forumulierung unseres Ziels umgehen, all die Ideen jedoch nicht verwerfen. Somit ist das aktuelle Ziel das Erstellen eines Dashboards. In diesem können wir die unterschiedlichen Ideen festhalten und dem Endnutzer zu den verschiedensten Krankheiten und Gruppen von Krankheiten Einblicke bieten.
