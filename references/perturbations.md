# Perturbations du Parcours

Le Parcours de construction nationale peut être perturbé par des événements qui modifient sa vitesse, sa direction ou son niveau de progression. Une perturbation se décompose en un **mécanisme** (ce qui cause la perturbation) et un **effet** (ce qui arrive au Parcours). Les perturbations peuvent être **ponctuelles** (un événement) ou **étendues** (une période) — un événement ponctuel peut déclencher une perturbation étendue (ex. : destruction du Temple → exil babylonien).

---

## 1. Vue d'ensemble

### Les 4 effets

| Effet | Ce qui arrive | Couleur (frise) |
|---|---|---|
| **Prolongement** | La phase en cours est rallongée | 🟠 orange |
| **Accélération** | La phase en cours est raccourcie | 🔵 bleu |
| **Avortement** | Le passage à la phase suivante est bloqué | 🔴 rouge |
| **Reboot** | Redémarrage de la phase ou retour à une phase antérieure | 🟤 cramoisi |

### Les 5 mécanismes (4 ponctuels + 1 état continu)

| Mécanisme | Type | Icône (frise) |
|---|---|---|
| **Choc d'hétérogénéité** | Ponctuel ou graduel | `open_in_full` |
| **Choc exogène** | Ponctuel | `bolt` |
| **Insuffisance interne** | Ponctuel | `close` |
| **Correction d'échelle** | Ponctuel ou graduel | `compress` |
| **Exutoire** | **Continu** | *(pas de marqueur — implicite)* |

### Couplage mécanisme × effet

|  | Prolongement 🟠 | Accélération 🔵 | Avortement 🔴 | Reboot 🟤 |
|---|---|---|---|---|
| **Choc d'hétérogénéité** | ✓ | | (peut avorter une sous-phase) | |
| **Choc exogène** | ✓ | ✓ | ✓ | ✓ |
| **Insuffisance interne** | | | ✓ | |
| **Correction d'échelle** | | ✓ | | |
| **Exutoire** (continu) | ✓ | | | |

Le **choc exogène** est le seul mécanisme polyvalent — son effet dépend de ce que le choc fait. Les autres mécanismes sont chacun couplés à un effet dominant.

### Principe structurel : prolongement/accélération encodent une variation d'homogénéité

Au-delà du tableau de couplage, les effets `prolongement` et `accélération` répondent à une logique structurelle universelle : **ils encodent une variation de l'homogénéité effective du corps politique de la nation**.

- **Prolongement** : l'hétérogénéité augmente — par intégration effective d'une marge culturellement distincte (choc d'hétérogénéité), ou par détournement continu de l'énergie élitaire vers l'extérieur (exutoire) qui ralentit le moteur d'homogénéisation. La phase en cours dure plus longtemps.
- **Accélération** : l'homogénéité augmente — par perte d'un territoire effectivement digéré qui ramène le noyau à son échelle naturelle (correction d'échelle), par modernisation administrative imposée qui homogénéise par contrainte (choc exogène modernisateur), ou par suppression d'un exutoire qui force le recentrage interne (choc exogène fin d'exutoire militaire). La phase en cours se résout plus vite.

**Le canal territorial est le plus fréquent, pas l'automatique**. La conquête ou la perte est le canal habituel, mais le critère décisif n'est jamais le changement nominal de souveraineté — c'est la **digestion effective** : administration directe par du personnel issu du noyau, droit imposé depuis le noyau, mobilisation durable des élites centrales. Trois cas-type pour ancrer l'intuition :

- *Doublement bavarois sous Napoléon (1806)* : intégration directe par administration Montgelas → choc d'hétérogénéité / prolongement.
- *Possessions européennes des Habsbourg avant 1714* : laissées en union personnelle, jamais digérées par le noyau castillan → **pas de perturbation structurelle**, malgré l'ampleur territoriale.
- *Stato da Mar vénitien* : administré par provveditori issus du patriciat → choc d'hétérogénéité / prolongement, exutoire principal de la phase oligarchique.

Le canal non territorial existe aussi : modernisation administrative imposée par une puissance occupante, conquête culturelle qui hétérogénéise par voie linguistique ou élitaire sans changer la superficie (codée `territorial: false`). Cf. §3 pour la dimension territoriale détaillée.

### Affichage sur la frise

Les perturbations sont affichées comme des **losanges** (◆) pour les distinguer des saillants normaux (●). La **couleur** encode l'effet, l'**icône** encode le mécanisme.

- **Perturbation ponctuelle** (cas par défaut) : losange à la date de l'événement, codé `type: saillant` + `perturbation: true` + `mechanism` + `effect`.
- **Perturbation étendue** (cas rare) : losange pour le déclencheur + bande hachurée pour la durée, codé `type: perturbation` + `start` + `end` + `mechanism` + `effect`.
- **Exutoire** : pas de marqueur (mentionné dans la description de la durée de la phase).
- **Fin de l'exutoire** : saillant canonique « fin de l'expansion » (●, couleur de la phase — pas un losange de perturbation).

#### Règle par défaut : perturbation ponctuelle

**Par défaut, toute perturbation est ponctuelle**. La forme étendue (bande hachurée sur la frise) est **réservée aux périodes où le Parcours est structurellement mis en pause ou prolongé sur une durée significative** — pas à un événement ponctuel dont les conséquences se déploient ensuite. Avant de coder une perturbation comme étendue, se demander explicitement : *« le Parcours est-il réellement en pause structurellement sur cette période, ou s'agit-il d'un événement ponctuel dont je suis tenté d'étirer la représentation ? »*.

Cas véritablement étendus dans le corpus actuel :
- **Exil babylonien** (Israël antique, 587-538 av. J.-C.) — Parcours mis en pause par déportation collective.
- **Effondrement valois** (France, 1392-1420) — institutions effondrées, Parcours en pause jusqu'à reconstitution sous Charles VII.
- **Guerres d'Italie** (Milan, 1499-1535) — reboot prolongé de l'absolutisme milanais en phase oligarchique.

Ces cas partagent la propriété : *la dynamique phasique est structurellement interrompue pendant la durée de la perturbation*. Un retour de souverain, un écrasement de révolution, une transition dynastique sont des événements ponctuels (même si leurs effets durent ensuite) — ils se codent comme saillants ponctuels avec flag `perturbation: true`, pas comme bandes étendues.

---

## 2. Qualifier un événement

### Le triple test

Pour qu'un événement soit qualifié comme perturbation, il faut satisfaire les **trois critères** simultanément :

1. **Mécanisme identifiable** parmi les 5 (choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire).
2. **Effet identifiable** parmi les 4 (prolongement, accélération, avortement, reboot).
3. **Impact réel sur la trajectoire** : sans cet événement, la durée, le niveau ou la direction d'une phase aurait été différente.

Si l'un des trois fait défaut, l'événement n'est pas une perturbation au sens strict.

### Ce qui n'est PAS une perturbation

**Saillant canonique** — priorité de qualification : si un événement peut être un saillant canonique (cf. liste fermée dans CLAUDE.md), le mettre en saillant, pas en perturbation. *Exception unique* : les **crises féodales** sont à la fois saillant canonique ET perturbation (insuffisance interne / avortement).

**Anecdote de parcours** — événement réel mais sans impact identifiable sur la trajectoire (la phase aurait fait la même chose sans lui). Ne pas le marquer dans le parcours structuré.

**Boucle en phase féodale** — la phase féodale est ponctuée de pics féodaux suivis de crises féodales. Si l'homogénéité des élites reste insuffisante pour produire un Pacte Oligarchique, le Parcours **boucle** : un nouveau pic émerge, la crise se répète, et ainsi de suite jusqu'à ce que les conditions soient atteintes. Ce n'est pas une perturbation au sens strict — c'est le mécanisme structurel intra-phase de la phase féodale. La durée totale dépend du nombre de cycles avant convergence des conditions de Deblonde ; ce n'est pas la boucle qui prolonge la phase, c'est la non-convergence qui produit la boucle.

> *Distinction* : une perturbation fait *trébucher* le Parcours ; une boucle le fait *tourner en rond* sans avancer. Chaque crise féodale individuelle dans une boucle est cependant à la fois un saillant canonique « Crise féodale » et une perturbation insuffisance interne / avortement (cf. §4.4).

**Rébellion périphérique** — un soulèvement aux marges d'un empire à son acmé absolutiste relève du Parcours impérial, non du Parcours de la communauté soumise. À ne pas confondre avec une étape du Parcours national.

> *Test* :
> - *Rébellion périphérique* : le soulèvement mobilise des populations marginales d'un empire à son acmé absolutiste, et coïncide avec un effort de centralisation/homogénéisation forcée du centre impérial. Le Parcours national de la communauté soumise n'est pas en transition — la rébellion est provoquée par la dynamique du Parcours impérial.
> - *Étape du Parcours national* : le soulèvement mobilise le corps civique de la nation, intervient à un moment cohérent avec sa dynamique phasique propre, et résout (ou déclenche) une transition structurelle interne. La supra-entité impériale est l'arrière-plan, pas le moteur.

**Élément nouveau théorique** — événement structurellement important qui ne rentre dans aucune catégorie existante (saillant canonique, perturbation, anecdote). À **remonter explicitement** pour discussion théorique, plutôt que forcer dans une catégorie existante.

---

## 3. Dimension territoriale

### Noyau territorial et marges

La **superficie de référence** d'une nation à un moment donné se décompose en deux composantes :

- **Noyau territorial** : le territoire culturellement homogène avec le cœur de la nation — même langue, même droit, mêmes institutions. C'est le territoire qui *est* la nation.
- **Marges** : les territoires hétérogènes sous contrôle de la même couronne — langue différente, droit différent, culture différente. C'est le territoire que la nation *possède* sans l'avoir assimilé.

La distinction noyau/marges est la traduction territoriale des deux moteurs du Parcours. Le noyau correspond au territoire où l'homogénéisation culturelle est accomplie ; les marges au territoire où elle ne l'est pas encore.

**Transitions marge → noyau** : un territoire peut commencer comme marge et rejoindre le noyau quand l'homogénéisation culturelle y est accomplie. Ces transitions sont approximées par des dates ponctuelles d'accomplissement juridique et linguistique (édit, loi d'union, abolition des particularismes).

### Perturbations territoriales vs non territoriales

La plupart des perturbations de type `choc_heterogeneite` et `correction_echelle` sont **territoriales** — elles correspondent à un changement de superficie visible sur le graphique d'aire (expansion ou contraction).

Certaines perturbations utilisent le même mécanisme mais ne sont **pas territoriales** — elles opèrent par le canal culturel ou institutionnel sans modifier la superficie. Dans ce cas, on ajoute le champ `territorial: false` dans les données du saillant.

### Mécanismes et territoire

| Mécanisme | Territorial ? | Direction |
|---|---|---|
| Choc d'hétérogénéité | Presque toujours oui | Expansion (la superficie augmente) |
| Correction d'échelle | Toujours oui | Contraction (la superficie diminue) |
| Choc exogène | Souvent oui, parfois non | Variable (invasion, traité, défaite) |
| Insuffisance interne | Rarement | — |
| Exutoire (continu) | Implicitement | Expansion continue |

### Affichage : perturbations territoriales et graphique de superficie

Sur la frise, les perturbations territoriales (sans `territorial: false`) dont l'effet est `prolongement` ou `acceleration` sont affichées **au-dessus du graphique de superficie** plutôt que dans la rangée principale des saillants. Cela permet de :
- Associer visuellement l'expansion/contraction au changement de superficie visible sur le graphique
- Désengorger la rangée principale des saillants

Les perturbations avec effet `reboot` ou `avortement` restent dans la rangée principale, même si elles sont territoriales — elles relèvent de la dynamique politique du Parcours, pas seulement du territoire.

---

## 4. Les mécanismes en détail

### 4.1 Choc d'hétérogénéité

**Définition** : événement ou processus par lequel une expansion territoriale, un afflux de population, ou l'intégration d'une marge **effectivement digérée** par le noyau hétérogénéise brutalement la société, déclenchant un prolongement de la phase en cours. La condition de digestion est essentielle : sans mobilisation effective des élites du noyau pour intégrer la marge, il n'y a pas de choc.

**Empire intégré vs empire en union personnelle** — distinction critique :

1. **Empire intégré** (administration commune) : les marges sont administrées directement par des fonctionnaires issus du noyau (magistrats, gouverneurs, intendants, juges), soumises au droit du noyau (ou à un droit imposé depuis le noyau), et leurs élites locales sont soit cooptées dans l'élite du noyau soit écartées. Chaque nouvelle acquisition crée des postes à pourvoir, des responsabilités à distribuer, un travail d'homogénéisation à faire. **C'est un vrai choc d'hétérogénéité qui prolonge structurellement le Parcours.**

2. **Empire en union personnelle** (administration séparée) : les marges conservent leurs propres institutions (diète, assemblée, parlement), leur propre droit coutumier, leurs propres administrateurs locaux. Le souverain partage un titre avec le noyau mais « change de chapeau » institutionnellement quand il passe d'une couronne à l'autre. Les élites du noyau ne sont pas mobilisées pour digérer les marges — elles restent concentrées sur le territoire noyau. **L'union personnelle ne produit pas de choc d'hétérogénéité structurel ; au plus, elle fonctionne comme une soupape militaire (exutoire de guerre, débouché de carrières) qui absorbe temporairement l'énergie élitaire sans la diriger vers un travail d'homogénéisation.**

**Datation correcte** : dans une monarchie composite où une marge passe progressivement de l'union personnelle à l'administration directe, le choc d'hétérogénéité doit être placé **au moment de l'intégration administrative** (codification, union juridique, abolition des particularismes), pas au moment de l'acquisition dynastique.

**Intensité variable** : un choc par intégration d'une marge culturellement proche (langue apparentée, droit similaire, confession commune) est moins intense qu'un choc par intégration d'une marge culturellement distante.

**Avortement de sous-phase** : un choc d'hétérogénéité peut avorter une sous-phase en cours. Si la société entrait en ancien régime (stratification, sédimentation), l'hétérogénéisation défait cette stratification et relance la dynamique d'homogénéisation — ce qui peut rebooter la sous-phase d'impérialisme absolutiste.

**Trois cas-type** :

- **Empire intégré** : administration directe par du personnel issu du noyau (provveditori, intendants, vice-rois, corregidores, gouverneurs). Chaque acquisition crée des postes à pourvoir, un butin à partager, un travail d'intégration. C'est le cas pur, et il produit les phases oligarchiques les plus longues.
- **Choc par expansion brutale + administration uniforme imposée** : doublement de territoire (typiquement par traité ou modernisation napoléonienne) appliquant un modèle administratif unique sur des populations hétérogènes (langue, confession, droit). Avorte parfois une entrée en ancien régime en cours et relance un cycle d'impérialisme absolutiste sous forme modernisatrice.
- **Choc non territorial** : conquête extérieure qui ne change pas la superficie mais hétérogénéise par voie culturelle (langue administrative imposée, élites cooptées par l'occupant, circuits commerciaux réorientés). Codé `choc_exogene / prolongement` avec `territorial: false`.

### 4.2 Choc exogène

**Définition** : événement extérieur ponctuel qui frappe le Parcours. C'est le mécanisme **polyvalent** — son effet dépend de ce que le choc fait :

| Ce que le choc fait | Effet |
|---|---|
| Ralentit sans détruire (gel temporaire, occupation) | Prolongement 🟠 |
| Supprime un exutoire militaire externe, force le recentrage interne | Accélération 🔵 |
| Bloque une transition sans détruire les institutions | Avortement 🔴 |
| Détruit les institutions et les réseaux humains | Reboot 🟤 |

**Cas particulier 1 : choc exogène culturel non territorial**. Conquête extérieure qui ne change pas la superficie mais hétérogénéise par voie culturelle (langue administrative imposée, élites cooptées par l'occupant, circuits commerciaux réorientés). Codé `choc_exogene / prolongement` avec `territorial: false`. C'est le pendant non territorial du choc d'hétérogénéité.

**Cas particulier 2 : choc exogène avec fin d'exutoire militaire**. Quand une défaite externe supprime un territoire **en union personnelle** (jamais digéré par le noyau), c'est `choc_exogene / acceleration` — pas une `correction_echelle`.

> *Distinction critique* :
> - `correction_echelle / acceleration` : le territoire perdu était intégré, sa perte contracte le noyau digéré et force une réduction d'échelle. Accélération par retour à l'échelle naturelle plus petite.
> - `choc_exogene / acceleration` (fin d'exutoire militaire) : le territoire perdu était un exutoire externe (union personnelle, possession continentale lointaine), sa perte supprime la soupape militaire qui détournait l'énergie élitaire. Accélération par recentrage sur le jeu interne.
>
> Les deux produisent le même effet observable mais par des mécanismes distincts. La correction d'échelle suppose et valide une digestion préalable ; le choc exogène n'en suppose pas.

Cas typique de la fin d'exutoire militaire : perte d'une possession continentale en union personnelle qui servait de débouché militaire à des factions oligarchiques. La perte coupe les factions de leur exutoire externe et précipite leur affrontement interne (souvent saillant comme guerre sociale subséquente).

### 4.3 Correction d'échelle

**Définition** : contraction territoriale du noyau effectivement digéré, qui ramène le Parcours vers son « échelle naturelle » plus petite et accélère la phase en cours.

**Critère strict** : il faut que le territoire perdu ait été effectivement **digéré** par le noyau — administration directe par du personnel issu du noyau, droit imposé depuis le noyau, mobilisation durable des élites centrales. Seules ces pertes ramènent réellement le Parcours vers un noyau naturel plus petit et accélèrent la suite.

**Test pratique** : (1) le territoire était-il administré par des fonctionnaires issus du noyau, soumis à son droit ? (2) cette administration intégrée a-t-elle duré assez longtemps pour mobiliser durablement les élites centrales (au moins quelques décennies, idéalement un siècle ou plus) ? Si oui aux deux questions, c'est une correction d'échelle. Si non — institutions locales préservées, élites locales restées maîtresses — la perte ne produit pas de correction d'échelle structurelle, même si elle est militairement spectaculaire (voir alors §4.2 cas particulier 2).

**Corollaire symétrique** : si une acquisition territoriale n'a pas produit de choc d'hétérogénéité (parce qu'elle est restée en union personnelle, non digérée par le noyau), alors sa perte ne peut pas non plus produire de correction d'échelle structurelle. Une possession qu'on n'a jamais digérée n'est pas un poids dont la perte « ramène vers l'échelle naturelle » — c'est juste un chapeau qui tombe. L'effet sur le cycle est nul dans les deux sens.

### 4.4 Insuffisance interne

**Définition** : blocage interne du Parcours qui empêche une transition phasique. Mécanisme exclusivement avortant : la phase en cours ne peut pas accoucher de la suivante parce que ses conditions structurelles ne sont pas réunies.

**Cas-type 1 : crise féodale sans Pacte Oligarchique**. Un pic féodal s'effondre en crise, mais l'homogénéité des élites est insuffisante pour produire un Pacte Oligarchique. La transition vers la phase oligarchique est avortée ; la phase féodale recommence un cycle pic → crise. Chaque crise individuelle est à la fois saillant canonique « Crise féodale » ET perturbation insuffisance interne / avortement — c'est une **occasion prématurée** où le pacte ne peut se faire. La répétition de ces cycles est la **boucle féodale** (cf. §2 « Ce qui n'est PAS une perturbation ») : la phase féodale dure tant que les conditions de Deblonde n'ont pas convergé. Ce n'est pas la boucle qui prolonge la phase, c'est la non-convergence qui produit la boucle.

**Cas-type 2 : absolutisation avortée**. Une figure tente de résoudre la guerre sociale et imposer un cadre absolutiste, mais échoue par défaut de soutien (ni les clientèles délaissées, ni la classe moyenne administrative ne convergent suffisamment). Aucun nouveau cadre n'émerge ; la phase oligarchique se poursuit jusqu'à une nouvelle tentative de résolution — qui pourra venir d'un autre tiers, d'une dynastie issue d'une faction, ou d'une intervention exogène.

### 4.5 Exutoire (état continu)

**Définition** : état durable où l'énergie élitaire est canalisée vers l'extérieur (empire, colonies, mercenariat, expansion militaire continue). Pas un événement ponctuel — c'est une **condition** du Parcours, qui n'a pas de marqueur losange propre sur la frise.

**Cycle de l'exutoire** :
- *Apparition* : déclenchée par un choc d'hétérogénéité qui crée le débouché extérieur, ou par une dynamique militaire/commerciale continue.
- *Fin* : marquée par le saillant canonique **« fin de l'expansion »** (rond, couleur de la phase — pas un losange de perturbation). Cause : choc exogène qui supprime l'exutoire, ou épuisement interne des moyens de l'expansion.

**Distinction choc d'hétérogénéité vs exutoire** : le choc d'hétérogénéité ajoute de la diversité vers l'intérieur (gain territorial digéré, afflux culturel) ; l'exutoire projette l'énergie vers l'extérieur. Les deux produisent un prolongement mais par des voies différentes : le choc repousse le seuil d'homogénéité, l'exutoire absorbe les tensions élitaires. Ils coexistent souvent (un héritage impérial peut créer à la fois l'hétérogénéité par la digestion d'une marge et l'exutoire par l'expansion militaire continue).

**Timing : phase active vs phase parlementaire**.
- *Pendant une phase active* (féodale, oligarchique, absolutiste) : l'exutoire colonial ou militaire prolonge la phase en cours en absorbant les tensions internes.
- *Après la RN* (phase parlementaire) : l'exutoire colonial ne perturbe pas le Parcours, car la phase parlementaire est l'aboutissement et n'a pas de transition à venir à retarder.

---

## 5. Les effets en détail

### 5.1 Reboot

**Définition** : perturbation qui détruit les institutions et anéantit les réseaux humains de l'appareil central. Le Parcours régresse à une phase antérieure parce que l'État central doit être reconstruit. Mécanisme typique : choc exogène destructeur (conquête, déportation, écrasement militaire massif).

Le reboot est provoqué par une rupture institutionnelle et démographique majeure : destruction physique de l'État, élimination ou déportation des élites, effondrement de l'économie. Ce qui a mis des siècles à se construire — les réseaux et la structure de l'État central, les équilibres entre classes — est rasé. Si l'homogénéité culturelle du peuple est préservée malgré la destruction institutionnelle, le redémarrage peut être rapide.

**Profondeur du reboot** :
- Si l'**État central** est détruit mais que les **équilibres entre classes d'élites** subsistent (au moins partiellement), le Parcours régresse d'**une phase**.
- Si l'État central ET la **structure des élites** sont anéantis, le Parcours peut régresser de **plusieurs phases**.

**Reprise des sous-phases** : toujours par la **première sous-phase** de la phase de destination, puisque l'État central doit être reconstruit.

**Trois cas-type** :
- **Régression d'une phase, élites préservées** : déportation collective ou exil sans génocide. La communauté élitaire conserve sa structure ; au retour, les conditions de redémarrage sont rapidement réunies et le Parcours reprend une phase en arrière.
- **Régression d'une phase, vide oligarchique** : révolte écrasée, factions oligarchiques liquidées sauf une. La présence simultanée d'un pouvoir central fort (souvent étranger) et d'une homogénéité culturelle forte recrée directement les conditions d'entrée en phase absolutiste — d'où des configurations où une révolte ultérieure prend la forme d'une guerre d'indépendance d'un monarque absolu, pas d'un nouveau cycle révolutionnaire.
- **Régression de plusieurs phases (reboot profond)** : aristocratie remplacée intégralement, redistribution foncière, nouveau système juridique imposé. Les réseaux humains et les équilibres entre classes sont anéantis. Le Parcours redémarre en phase féodale.

**Variante : transfert de territoire**. Le Parcours n'est pas attaché à un territoire fixe mais à une communauté humaine. Si le territoire d'origine est détruit mais que les porteurs survivent et se déplacent, le Parcours peut se transférer sur un nouveau territoire. Le transfert le perturbe et l'allonge mais ne l'interrompt pas. Conditions favorisant un transfert réussi : noyau de réfugiés conservant son homogénéité culturelle, territoire d'accueil de petite taille permettant une concentration rapide, absence d'absorption dans une autre communauté élitaire dominante.

### 5.2 Prolongement

**Définition** : perturbation qui ne détruit pas les institutions mais hétérogénéise la société et désorganise les élites ainsi que les réseaux dont dépend le pouvoir central. Le Parcours ne recule pas — il **stagne**, le temps que les factions se recomposent autour des nouveaux clivages. Mécanismes typiques : choc d'hétérogénéité, choc exogène ralentisseur, exutoire (état continu).

La différence avec le reboot est que les institutions survivent : assemblées en fonction, cadre juridique préservé, magistratures suprêmes intactes. Mais les élites prébendières perdent ce qui faisait leur puissance — leur intégration aux structures impériales antérieures —, et la société se fragmente culturellement. Le temps de stagnation est celui que mettent les factions à se recomposer autour des nouveaux clivages avant qu'une guerre sociale ne puisse réellement se résoudre.

**Reprise des sous-phases** : reprend **là où le Parcours était bloqué**. Les institutions ayant survécu, il n'est pas nécessaire de repasser par les sous-phases antérieures.

### 5.3 Avortement

**Définition** : perturbation qui bloque le passage à la phase suivante sans détruire les institutions. La phase en cours ne se résout pas et se prolonge jusqu'à ce qu'un autre événement (résolution endogène ou nouvelle perturbation) débloque la transition.

**Causes typiques** :
- **Insuffisance interne** : conditions structurelles non réunies (homogénéité insuffisante en féodale, défaut de cadre central résolvant en oligarchique tardive). Cf. §4.4.
- **Choc exogène bloquant** : intervention extérieure qui empêche une transition (puissance étrangère qui écrase une RN naissante, par exemple).
- **Choc d'hétérogénéité avortant une sous-phase** : intégration d'une marge qui défait la stratification d'un ancien régime entrant et relance l'impérialisme absolutiste. Cf. §4.1.

### 5.4 Accélération

**Définition** : perturbation qui raccourcit la phase en cours en supprimant un exutoire, en réduisant l'hétérogénéité, ou en forçant une modernisation. Le Parcours avance plus vite vers la phase suivante.

**Causes typiques** :
- **Correction d'échelle** : perte d'un territoire effectivement digéré qui ramène le noyau à son échelle naturelle plus petite. Cf. §4.3.
- **Choc exogène avec fin d'exutoire militaire** : perte d'un débouché externe (union personnelle, possession continentale) qui force le recentrage sur le jeu interne. Cf. §4.2 cas particulier 2.
- **Choc exogène modernisateur** : intervention extérieure qui impose un cadre administratif moderne et balaie les structures anciennes (occupation napoléonienne par exemple).

---

## 6. Flux diagnostique

Pour un événement qu'on cherche à classer, poser les questions dans l'ordre :

**Q1 — Est-ce une perturbation ?**
Appliquer le triple test : mécanisme + effet + impact réel sur la trajectoire. Si l'un fait défaut → l'événement est saillant canonique, anecdote, ou élément nouveau théorique (voir §2). Sinon, continuer.

**Q2 — Les institutions sont-elles détruites ?**
- Oui → **reboot**. Évaluer la profondeur (régression d'une phase / de plusieurs).
- Non → continuer.

**Q3 — Quel mouvement du Parcours ?**
- Stagne ou ralentit → **prolongement**.
- Accélère → **accélération**.
- Transition bloquée (la phase en cours ne peut pas se résoudre) → **avortement**.

**Q4 — Quel mécanisme ?**
- Expansion territoriale + administration commune effective ? → **choc d'hétérogénéité**.
- Perte d'un noyau effectivement digéré ? → **correction d'échelle**.
- Perte d'une possession en union personnelle (jamais digérée) ? → **choc exogène fin d'exutoire militaire** (pas correction d'échelle).
- Conditions structurelles non réunies en interne ? → **insuffisance interne**.
- État continu d'expansion extérieure (pas un événement ponctuel) ? → **exutoire**.
- Intervention extérieure ne rentrant dans aucun cas spécial ? → **choc exogène** générique.

**Q5 — Territorial ?**
- La superficie change (gain ou perte de territoire effectivement digéré) ? → territorial (sans flag).
- Le mécanisme opère par le canal culturel ou institutionnel sans changer la superficie ? → `territorial: false`.
