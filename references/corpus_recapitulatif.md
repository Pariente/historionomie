# Corpus récapitulatif — saillants par nation

⚠️ **Lecture interdite à Agent 2 (Évaluateur).** Ce fichier contient l'alignement des saillants des nations déjà mappées. Y accéder pendant un scoring crée un ancrage par analogie de surface qui contamine l'évaluation.

Ce fichier est lu **par le parent uniquement** :
- Pour la **comparaison tardive** avec le corpus (Étape 6 de `methode_cartographie.md`), une fois le scénario retenu
- Pour générer des visualisations comparatives ou répondre à des questions cross-corpus

Pour le détail par nation, voir `references/nations/*/parcours.md` et `references/nations/*/justification.md`.

---

## Tableau des saillants par nation

| Saillant | Israël antique | Israël (prolongement) | France | Angleterre | Venise | Bavière | Piémont |
|---|---|---|---|---|---|---|---|
| Éveil féodal | Saül (~-1080) | — | Louis VI (1108) | Guillaume (1066, reboot) | Orso Ipato (~726) | Louis Ier (~1204) | Thomas II (~1233) |
| Pic féodal | Salomon (~-960) | — | Philippe le Bel (~1295) | Édouard Ier (~1295) | Orseolo (~991) | Louis IV (~1328) | Philippe Ier d'Achaïe (~1295) |
| Pacte oligarchique | Probable sous Omri (-885), non textuellement attesté | — | Loi salique (1317) | Ordonnances (1311) | Abolition co-régence (1032) | Primogéniture (1506) | Statuta (1430) / Ordini Nuovi (1561) |
| 1er monarque oligarchique | Omri (-885) | — | Philippe VI (1328) | Édouard III (1327) | Contarini (~1043) / système | Guillaume IV (~1508) | Amédée VIII (~1430) / Emmanuel Philibert (1559) |
| Acmé oligarchique | Jéroboam II (~-770) | — | François Ier (~1515) | Édouard III (~1350) | Foscari (~1440) | Albert V (~1555) | Charles Emmanuel Ier (~1600) |
| Fin de l'expansion (olig.) | ~-746 | — | Cateau-Cambrésis (1559) | — | Agnadello (1509) | — | Mort Ch. Emmanuel Ier (1630) |
| Guerre sociale | -700 à -641 | -175 à -140 | Guerres de Religion (~1562-1598) | Guerre des Deux-Roses (~1455-1485) | Tensions institutionnelles (~1628-1669) | ~1564-1597 | Madamisti/Principisti (~1637-1696) |
| 1er monarque absolu | Josias (-640) | Simon Thassi (-140) | Henri IV (1598) | Henri VII (1485) | Inquisiteurs d'État (~1669) | Maximilien Ier (1597) | Victor Amédée II (~1696) |
| Dernière grande révolte oligarchique (DGRO) | — | Jannée (-94) | La Fronde (1648-1653) | Henri VIII (~1534-1540) | — (pas d'assise) | — (pas d'assise) | Affaire Graneri (1722-1723) |
| Acmé absolutiste | — (interrompu) | Hérode (-20) | Louis XIV (~1682) | Élisabeth Ière (~1580) | Morosini (~1688) | Max. III Joseph (~1756) / Louis Ier (~1835) | Ch. Emmanuel III (~1748) |
| Fin de l'expansion (abs.) | — | Mort d'Hérode (-4) | Utrecht (1713) | — | Passarowitz (1718) | Blenheim (1704) | Aix-la-Chapelle (1748) |
| Remontrance | — | Ambassade à Auguste (-4) | Polysynodie (1715) | Apology of the Commons (1604) | Correzione (1761) | Landtag (1848) | Révolte de 1821 |
| Éclatement de l'AR | — | Grande Révolte (66) | 1789 | Guerre civile (1642) | République de Manin (1848) | Eisner (1918) | — (absorbée, 1861) |
| Émergence de l'IR | — | — | Bonaparte (1799) | Cromwell (1653) | — (RN avortée) | — (absorbée) | — (absorbée) |
| Glorieuse Révolution | — | — | 1830 | 1688 | — (absorbée, 1866) | — (absorbée, 1919) | — (absorbée) |

Sous-phase « Ancien régime » (ne pas confondre avec un saillant) : France ~1715-1789 ; Angleterre ~1603-1642 ; Venise ~1718-1848 ; Bavière ~1848-1918 ; Piémont ~1748-1861 (éclipse 1796-1814) ; Israël prolongement -4 à 66.

---

## Tableau des perturbations par nation

Pour les définitions des mécanismes et effets, voir `references/perturbations.md`.

| Perturbation | Nation | Mécanisme | Effet | Territorial ? | Marqueur |
|---|---|---|---|---|---|
| **Israël** |
| Choc assyrien (-722) | Israël | Choc exogène | Reboot + transfert 🟤 | Oui | ◆🟤 `bolt` |
| Conquête babylonienne (-586) | Israël | Choc exogène | Reboot 🟤 | Oui | ◆🟤 `bolt` |
| Hellénisation (-332) | Israël | Choc exogène | Prolongement 🟠 | **Non** (culturel) | ◆🟠 `bolt` |
| Destruction du Temple (70) | Israël | Choc exogène | Reboot 🟤 | Oui | ◆🟤 `bolt` |
| **Angleterre** |
| Empire de Cnut (~1016) | Angleterre | Choc exogène | Prolongement 🟠 | Oui | ◆🟠 `bolt` |
| Conquête normande (1066) | Angleterre | Choc d'hétérogénéité | Reboot 🟤 | Oui | ◆🟤 `restart_alt` |
| Perte de la Normandie (1204) | Angleterre | Choc exogène (fin d'exutoire militaire) | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| Boucles féodales anglaises | Angleterre | Insuffisance interne | Avortement 🔴 | Non | ◆🔴 `close` |
| Perte de la France (1453) | Angleterre | Choc exogène (fin d'exutoire militaire) | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| **France** |
| Croisade des Albigeois (1229) | France | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Crécy-Poitiers (~1346) | France | Choc exogène | Prolongement 🟠 | Oui | ◆🟠 `bolt` |
| Azincourt-Troyes (1415-1420) | France | Choc exogène | Reboot 🟤 | Oui | ◆🟤 `bolt` |
| Intégration Bourgogne-Provence (1477-1481) | France | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Traité d'Utrecht (1713) | France | Choc exogène | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| **Espagne** |
| Empire colonial américain (1521-1533) | Espagne | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Intégration de l'Aragon (1716) | Espagne | Choc d'hétérogénéité (modéré, proximité culturelle) | Prolongement 🟠 | Non (administratif) | ◆🟠 `open_in_full` |
| Perte de l'empire colonial américain (1808-1826) | Espagne | Correction d'échelle | Accélération 🔵 | Oui | ◆🔵 `compress` |
| Désastre de 1898 | Espagne | Choc exogène | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| **Venise** |
| Stato da Màr (1204) | Venise | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Conquête de la Terraferma (1428) | Venise | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Perte de la Crète (1669) | Venise | Correction d'échelle | Accélération 🔵 | Oui | ◆🔵 `compress` |
| Chute de la République (1797) | Venise | Choc exogène | Avortement 🔴 | Oui | ◆🔴 `bolt` |
| RN écrasée (1849) | Venise | Choc exogène | Avortement 🔴 | Oui | ◆🔴 `bolt` |
| **Milan** |
| Empire Visconti (1395) | Milan | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| Fragmentation Visconti (1402) | Milan | Correction d'échelle | Accélération 🔵 | Oui | ◆🔵 `compress` |
| Invasion française (1499) | Milan | Choc exogène | Reboot 🟤 | Oui | ◆🟤 `bolt` |
| Occupation napoléonienne (1796) | Milan | Choc exogène | Accélération 🔵 | **Non** (institutionnel) | ◆🔵 `bolt` |
| **Bavière** |
| Partitions (1255, 1349, 1392) | Bavière | Insuffisance interne | Avortement 🔴 | Non | ◆🔴 `close` |
| Doublement napoléonien (1806) | Bavière | Choc d'hétérogénéité | Prolongement 🟠 | Oui | ◆🟠 `open_in_full` |
| **Piémont** |
| Invasion française (1536) | Piémont | Choc exogène | Reboot 🟤 | Oui | ◆🟤 `bolt` |
| Éclipse napoléonienne (1796-1814) | Piémont | Choc exogène | Prolongement 🟠 | Oui | ◆🟠 `bolt` |
| **Autriche** |
| Crise féodale — extinction Babenberg (1246) | Autriche | Insuffisance interne | Avortement 🔴 | Non | ◆🔴 `close` |
| Crise féodale — Neuberg (1379) | Autriche | Insuffisance interne | Avortement 🔴 | Non | ◆🔴 `close` |
| Crise féodale — guerre civile Albert VI (1440s-1463) | Autriche | Insuffisance interne | Avortement 🔴 | Non | ◆🔴 `close` |
| Crise féodale — occupation Corvin (1485-1490) | Autriche | Choc exogène | Avortement 🔴 | Oui | ◆🔴 `bolt` |
| Intégration de la Bohême (1627) | Autriche | Choc d'hétérogénéité | Prolongement 🟠 | Non (administratif) | ◆🟠 `open_in_full` |
| Perte de la Silésie (1742) | Autriche | Correction d'échelle | Accélération 🔵 | Oui | ◆🔵 `compress` |
| Solferino — perte de la Lombardie (1859) | Autriche | Choc exogène (fin d'exutoire militaire) | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| Sadowa — exclusion de l'Allemagne (1866) | Autriche | Choc exogène (fin d'exutoire militaire) | Accélération 🔵 | Oui | ◆🔵 `bolt` |
| **Suisse** |
| Invasion française (1798) | Suisse | Choc exogène | Accélération 🔵 | Non | ◆🔵 `bolt` |

---

## Tableau récapitulatif — phase féodale

Parcours canoniques uniquement (Bohême, Chili, Hongrie en débat — non inclus). Pour les définitions des saillants, voir `references/phase_feodale.md`.

| Parcours | Éveil féodal | Pics féodaux | Pacte oligarchique | Durée |
|---|---|---|---|---|
| Israël antique | Saül (~-1080) | David (~-1003), Salomon (~-960) | Probable sous Omri (-885), non textuellement attesté | ~195 ans |
| Venise | Orso Ipato (~726) | Galbaio (~764), Partecipazio (~811), Candiano (~959), Orseolo (~991) | Abolition co-régence (1032) | ~306 ans |
| Angleterre [1] (avortée) | Ecgberht (~829) | Æthelstan (~930), Edgar (~965), Cnut (~1025) | — (avortée, reboot normand) | ~237 ans |
| Milan | Landolfo II (979) | Ariberto (~1018) | Commune (1097) | ~118 ans |
| Espagne | Ferdinand Ier (~1035) | Alphonse VI (~1085), Ferdinand III (1230), Alphonse X (~1265), Alphonse XI (1340) | Trastámara (1369) | ~334 ans |
| Angleterre [2] | Guillaume (1066) | Henri Ier (~1120), Henri II (~1170), Édouard Ier (~1295) | Ordonnances (1311) | ~261 ans |
| France | Louis VI (~1108) | Philippe Auguste (~1214), Philippe le Bel (~1295) | Loi salique (1317) | ~220 ans |
| Autriche [1] (avortée) | Léopold VI (~1198) | — | — (avortée, extinction Babenberg 1246) | ~48 ans |
| Bavière | Louis Ier (~1204) | Louis IV (~1328), Ludwig IX (~1450) | Primogéniture (1506) | ~326 ans |
| Piémont | Thomas II (1233) | Philippe Ier d'Achaïe (~1295), Amédée d'Achaïe (~1380) | Statuta Sabaudiae (1430) | ~197 ans |
| Suisse | Bundesbrief (1291) | Sempach (1386), Guerres de Bourgogne (~1474) | Stanser Verkommnis (1481) | ~190 ans |
| Autriche [2] | Rudolf IV (1358) | — | Innsbrucker Libell (1518) | ~160 ans |
| USA | ~1776 | Lincoln/Grant (~1865), McKinley/T. Roosevelt (~1905) | Fed + IRS (1913) | ~137 ans |

---

## Tableau récapitulatif — phase oligarchique

Pour les définitions des saillants, voir `references/phase_oligarchique.md`.

| Parcours | 1er monarque oligarchique | Acmé oligarchique | Guerre sociale | 1er monarque absolu |
|---|---|---|---|---|
| Israël antique | Omri (-885) | Jéroboam II (~-770) | -700 à -641 | Josias (-640) |
| Israël (prolongement) | — | — | -175 à -140 | Simon Thassi (-140) |
| Venise | Contarini (~1043) / système | Foscari (~1440) | ~1628-1669 | Inquisiteurs d'État (~1669) |
| Milan | Système communal (1097) | Paix de Constance (1183) | Torriani vs Visconti (1240-1277) | Ottone Visconti (1277) |
| Angleterre | Édouard III (1327) | Édouard III (~1350) | Guerre des Deux-Roses (~1455-1485) | Henri VII (1485) |
| France | Philippe VI (1328) | François Ier (~1515) | Guerres de Religion (~1562-1598) | Henri IV (1598) |
| Espagne | Henri II Trastámara (1369) | Rois Catholiques (~1492) | Succession d'Espagne (1700-1714) | Philippe V (1714) |
| Piémont | Amédée VIII (1430) | Charles Emmanuel Ier (~1600) | Madamisti vs Principisti (1637-1696) | Victor Amédée II (1696) |
| Suisse | Tagsatzung (~1501) | Occupation de Milan (~1512) | Paysans / Villmergen (1653-1712) | Patriciat trans-confessionnel (1712) |
| Bavière | Guillaume IV (1508) | Albert V (~1555) | ~1564-1597 | Maximilien Ier (1597) |
| Autriche | Maximilien Ier (1518) | Léopold Ier (~1683) | Succession d'Autriche (1740-1748) | Marie-Thérèse (1749) |

---

## Tableau récapitulatif — phase absolutiste

Pour les définitions des saillants, voir `references/phase_absolutiste.md`.

| Parcours | 1er monarque absolu | Acmé absolutiste | Ancien régime | Début de la RN |
|---|---|---|---|---|
| Israël antique | Josias (-640) | — (interrompu en -609) | — (interrompu) | — |
| Israël (prolongement) | Simon Thassi (-140) | Hérode (~-20) | -4 à 66 | Grande Révolte (66) |
| Milan | Ottone Visconti (1277) | Gian Galeazzo Visconti (~1395) | ~1447-1499 | — (absorbée) |
| Angleterre | Henri VII (1485) | Élisabeth Ière (~1580) | ~1603-1642 | Guerre civile (1642) |
| Bavière | Maximilien Ier (1597) | Max. III Joseph (~1756) | ~1848-1918 | Eisner (1918) |
| France | Henri IV (1598) | Louis XIV (~1682) | ~1715-1789 | 1789 |
| Venise | Inquisiteurs d'État (~1669) | Morosini (~1688) | ~1718-1848 | République de Manin (1848) |
| Piémont | Victor Amédée II (~1696) | Ch. Emmanuel III (~1748) | ~1748-1861 | — (absorbée) |
| Allemagne (Prusse) | Frédéric-Guillaume Ier (1713) | Frédéric le Grand (~1760) | ~1890-1918 | Révolution de Novembre (1918) |
| Espagne | Philippe V (1714) | Charles III (~1770) | ~1788-1808 | Dos de Mayo (1808) |
| Suisse | Patriciat trans-confessionnel (1712) | — | ~1780-1798 | République helvétique (1798) |
| Autriche | Marie-Thérèse (1749) | Joseph II (~1780) | ~1815-1918 | Révolution (1918) |

---

## Tableau récapitulatif — Révolution Nationale

Pour les définitions des saillants et des sous-phases, voir `references/phase_rn.md`.

| Sous-phase / Saillant | France | Angleterre | Israël (avortée) | Venise (avortée) |
|---|---|---|---|---|
| **Révolution initiale** | 1789-1799 | 1640-1653 | 66-70 | 1848-1849 |
| → Éclatement de l'AR | 1789 | 1642 | 66 | mars 1848 |
| → Expérience parlementaire | 1789-1791 | 1640-1648 | 66-67 | mars 1848 - août 1849 |
| → Phase aiguë | 1792-1794 | 1649 | 67-70 | Amorce : mars 1849 (pouvoirs illimités) |
| → Moment thermidorien | 1794-1799 | 1649-1653 | — (écrasée) | — (écrasée) |
| **Impérialiste Revanchard** | 1799-1815 | 1653-1658 | — | — |
| → Émergence de l'IR | Bonaparte (1799) | Cromwell (1653) | — | — |
| **Restauration** | 1815-1830 | 1660-1688 | — | — |
| → Glorieuse Révolution | 1830 | 1688 | — | — |

---

## Tableau récapitulatif — phase pré-féodale (percolation élitaire)

Pour la définition de la phase, voir `references/phase_pre_feodale.md`.

| Parcours | Début | Fin (éveil féodal) | Durée |
|---|---|---|---|
| France | 987 (Hugues Capet nominal) | 1108 (Louis VI le Gros) | ~121 ans |
| Angleterre | ~600 (Heptarchie) | ~829 (Ecgberht) | ~229 ans |
| Israël antique | ~-1200 (Juges) | ~-1080 (Saül) | ~120 ans |
| Milan | 888 (fragmentation carolingienne) | 979 (Landolfo II) | ~91 ans |
| Castille | ~930 (Fernán González) | ~1035 (Ferdinand Ier) | ~105 ans |

---

## Tableau récapitulatif — phase parlementaire (entrée en ENP)

Pour la définition de la phase, voir `references/phase_parlementaire.md`.

| Nation | Date d'entrée | Note |
|---|---|---|
| Angleterre | 1688 | Depuis la Glorieuse Révolution |
| France | 1830 | Depuis 1830 (avec des interruptions) |
