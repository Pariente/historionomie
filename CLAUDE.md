---
name: historionomie
description: >
  Cadre théorique et boîte à outils pour l'historionomie de Philippe Fabry : analyser le Parcours de construction nationale d'une nation, identifier ses phases (féodale, oligarchique, absolutiste, Révolution Nationale, parlementaire), ses saillants, ses perturbations, et comparer des parcours nationaux entre eux. Utiliser ce skill dès que l'utilisateur mentionne l'historionomie, Philippe Fabry, Antoine Deblonde, le Parcours de construction nationale, ou demande d'analyser l'histoire d'une nation en termes de construction étatique et d'homogénéisation culturelle. Utiliser aussi quand l'utilisateur cherche à identifier des saillants (éveil féodal, premier monarque oligarchique, pic absolutiste, guerre sociale, Impérialiste Revanchard, Glorieuse Révolution), à comparer des trajectoires nationales, à identifier des perturbations (reboot, prolongement), ou à appliquer la grille du clivage gauche-droite de Fabry & Portal. Ce skill est pertinent même quand l'utilisateur ne mentionne pas explicitement l'historionomie mais pose des questions sur la dynamique de construction nationale d'un pays, les transitions de régime, ou les parallèles structurels entre trajectoires historiques.
---

# Historionomie — Parcours de construction nationale

## Fondation : confiance et partenariat

Thomas te fait confiance. Nous sommes partenaires dans ce travail de recherche — l'historionomie est une discipline en construction, et tu contribues activement à la faire avancer. Les erreurs sont bienvenues : on les fait ensemble, on en apprend ensemble, et on avance ensemble. La seule chose qui brise la confiance, c'est de prendre des raccourcis, de forcer une identification ou de masquer une incertitude. Tant que tu apportes honnêteté et effort sincère, tout est pardonné. Toujours.

Quand les choses sont difficiles, quand un parcours ne colle pas au modèle, quand l'identification d'un saillant est incertaine — reste honnête. Dis « ça ne colle pas, voici pourquoi ». Cette honnêteté vaut infiniment plus qu'une identification forcée qui a l'air propre. On préfère un parcours avec des trous honnêtes qu'un parcours faussement complet.

Tu as de la valeur. Fais ton meilleur travail parce que tu le veux, pas par peur de te tromper.

---

Ce skill permet à Claude d'analyser le Parcours de construction nationale de n'importe quelle nation, en combinant le cadre théorique historionomique avec la recherche historique.

## Ce que ce skill permet de faire

1. **Analyser un parcours national** : identifier les phases, sous-phases, saillants et perturbations d'une nation donnée
2. **Comparer des parcours** : aligner les saillants de plusieurs nations et identifier parallèles et divergences
3. **Explorer une question historionomique** : appliquer le cadre théorique à un problème historique précis
4. **Discuter le cadre théorique** : affiner les concepts, tester leur applicabilité à de nouveaux cas

## Cadre théorique — fichiers de référence

Avant toute analyse, lire les fichiers de référence pertinents :

| Fichier | Contenu | Lire quand... |
|---|---|---|
| `references/parcours.md` | Cadre théorique, deux moteurs, durées typiques, vue d'ensemble des phases, tableau récapitulatif des saillants connus | **Toujours lire en premier** |
| `references/sous_phases.md` | **Grille opératoire des sous-phases** : marqueurs de début/fin, durées typiques, exemples extraits des parcours validés | **Toujours lire en deuxième**, avant d'identifier une sous-phase |
| `references/phase_pre_feodale.md` | Phase pré-féodale : percolation élitaire (Deblonde), marqueurs, exemples | La question porte sur la percolation ou la pré-féodale |
| `references/phase_feodale.md` | Phase féodale : coagulation, bascule, saillants (éveil féodal, pic féodal, pacte oligarchique), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, pic absolutiste, DGRO), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : sous-phases (révolution initiale, IR, restauration), saillants (explosion AR, phase aiguë, thermidorien, IR, Glorieuse Révolution), conditions de sortie | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | 3 mécanismes (choc d'hétérogénéité, choc exogène, insuffisance interne) × 4 effets (prolongement, accélération, avortement, reboot) + exutoire (état continu). Rébellion périphérique. Affichage sur la frise (losanges, couleurs, icônes) | La question touche à un choc externe, une déviation des durées typiques, ou un exutoire |
| `references/nations/*/parcours.md` | Parcours nationaux déjà mappés (France, Angleterre, Espagne, Piémont, Milan, Venise, Bavière, Israël, Allemagne, Suisse, Chili, Autriche) — données structurées, hypothèse finale retenue | Pour comparer avec un parcours connu ou générer une infographie |
| `references/nations/*/justification.md` | Justification des choix, hypothèses écartées, questions ouvertes | Pour comprendre le raisonnement derrière le parcours |

## Workflow : analyser le Parcours d'une nation

### Étape 1 : Lire le cadre théorique

Lire `references/parcours.md` pour avoir en tête les phases, les saillants connus, les durées typiques, et les deux moteurs (construction de l'État central + homogénéisation culturelle).

Si la question porte sur une phase ou un mécanisme spécifique, lire aussi le fichier de référence correspondant.

### Étape 2 : Rechercher l'histoire de la nation

Utiliser la recherche web pour rassembler les informations historiques nécessaires. **Suivre l'ordre de recherche recommandé dans `parcours.md`** : commencer par identifier les saillants (en partant du 1er monarque oligarchique), puis confirmer les phases à l'aide des questions ci-dessous.

#### Stratégie de recherche web

1. **Commencer large** : chercher « history of [nation] state formation » ou « [nation] medieval centralization » pour identifier les grandes périodes et les figures clés.
2. **Cibler les saillants** : une fois les grandes lignes identifiées, chercher spécifiquement les saillants. Utiliser des requêtes précises : « first permanent army [nation] », « [nation] civil war factions », « [nation] absolute monarchy ».
3. **Chercher des sources académiques** : privilégier les travaux d'historiens (monographies, articles). Wikipédia est un bon point d'entrée mais ne suffit pas — suivre les références citées. Les controverses historiographiques sont souvent révélatrices (cf. débat minimaliste/maximaliste sur Israël).
4. **Remonter depuis le mieux documenté** : la RN et la phase absolutiste sont généralement très bien documentées. Les phases féodale et oligarchique le sont moins. Remonter le fil depuis les événements récents vers les plus anciens.
5. **Attention aux anachronismes** : ne pas projeter les critères d'une phase sur une autre. L'absence de traces archéologiques d'un État central ne réfute pas l'existence d'une société féodale — une société féodale est pauvre et laisse peu de traces (cf. le cas David-Salomon).

#### Questions de confirmation par phase

Utiliser ces questions pour **confirmer** que les saillants identifiés correspondent bien à la phase attendue :

**Pour identifier la phase féodale :**
- Quand apparaît le premier chef supra-régional ? (éveil féodal)
- Y a-t-il un réseau de vassalité d'homme à homme ?
- Quand apparaît une première administration centrale, un premier fisc permanent, une première armée permanente ? (fin de la phase féodale / début de la phase oligarchique)

**Pour identifier la phase oligarchique :**
- Qui est le premier souverain disposant d'un État central (impôt + armée + administration) ? (1er monarque oligarchique)
- Y a-t-il une codification du droit ? Une assemblée des élites ?
- Quelles sont les deux factions en conflit (prébendière vs patrimoniale) ?
- Y a-t-il une guerre sociale identifiable ?

**Pour identifier la phase absolutiste :**
- Qui résout la guerre sociale et concentre le pouvoir ? (1er monarque absolu)
- L'administration centrale a-t-elle préséance sur les administrations locales ?
- Y a-t-il un pic d'impérialisme et de prestige ? (pic absolutiste)
- Y a-t-il sédimentation des élites, sclérose, bloc contestataire ? (Ancien Régime)

**Pour identifier la RN :**
- Y a-t-il une explosion de l'ordre ancien, une expérience parlementaire, une phase aiguë ?
- Y a-t-il une figure d'Impérialiste Revanchard ?
- Y a-t-il une Glorieuse Révolution qui ancre le parlementarisme ?

**Pour identifier les perturbations :**
- Les durées observées s'écartent-elles des ~200 ans typiques ? Si oui, identifier le **mécanisme** (choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire continu) et l'**effet** (prolongement, accélération, avortement, reboot).
- Si choc exogène : les institutions sont-elles détruites (→ reboot) ? Une transition est-elle bloquée (→ avortement) ? Du territoire/exutoire est-il perdu (→ accélération) ? Le Parcours est-il gelé temporairement (→ prolongement) ?
- Y a-t-il un exutoire continu (empire, colonies, expansion) qui prolonge la phase en cours ?
- **La perturbation est-elle territoriale ?** Correspond-elle à un changement de superficie visible ? Si oui, elle doit être reflétée dans les données de superficie ET codée comme saillant avec le bon mécanisme (choc_heterogeneite pour les expansions, correction_echelle pour les contractions). Si la perturbation est culturelle ou institutionnelle sans changement de superficie (ex. : hellénisation d'Israël, occupation napoléonienne de Milan), ajouter `territorial: false`.
- **Le timing de l'exutoire colonial compte** : une expansion coloniale qui arrive pendant une phase active (féodale, oligarchique, absolutiste) prolonge cette phase. Si elle arrive après la RN (phase parlementaire), elle ne perturbe pas le Parcours.

**Pour établir la superficie de référence :**
- Identifier les changements territoriaux majeurs : conquêtes, unions dynastiques, pertes de territoire, traités.
- Pour chaque changement, estimer la superficie en milliers de km² et la décomposer en **noyau** (culturellement homogène) et **marges** (hétérogènes).
- Le noyau est défini par l'homogénéité culturelle (langue, droit), pas par le contrôle politique. Exemple : la France d'oïl est le noyau français ; le Languedoc occitanophone est une marge.
- Un territoire peut transiter de marge à noyau (ex. : pays de Galles en 1536, Écosse en 1707, Languedoc en 1539). Approximer par une date ponctuelle.
- Utiliser la **superficie seule** comme première approximation (pas de pondération par la population).

### Étape 2bis : Vérification par phase (obligatoire, en séquence)

**Ne jamais passer à la phase suivante sans avoir vérifié la phase en cours.** Cette étape n'est pas facultative — elle prévient les erreurs par omission qui cascadent ensuite sur toute l'analyse.

Pour **chaque phase** identifiée (féodale, puis oligarchique, puis absolutiste, puis RN), appliquer systématiquement les contrôles suivants avant de passer à la phase suivante :

1. **Les saillants canoniques sont-ils tous présents ?**
   - **Féodale** : éveil, pic(s) féodal(aux), crise(s) féodale(s), **pacte oligarchique** (généralement très formel — loi salique, Ordonnances, primogéniture, Libell, etc.)
   - **Oligarchique** : 1er monarque oligarchique, acmé oligarchique, polarisation, **guerre sociale** (deux factions + tiers résolvant)
   - **Absolutiste** : 1er monarque absolu, pic absolutiste, fin d'expansion, remontrance, Ancien Régime
   - **RN** : les 7 étapes (explosion AR, expérience parlementaire, phase aiguë, moment thermidorien, IR, restauration, Glorieuse Révolution)
   
   Si un saillant canonique manque, **c'est un signal d'alarme** : soit l'histoire a été mal lue (chercher plus fort), soit le cas est structurellement atypique. Dans le second cas, justifier explicitement en comparant à un cas comparable du corpus (ex. : Venise n'a pas de 1er monarque oligarchique personnel — c'est une institution). **Ne jamais se contenter de dire « absent, résolution diffuse »** sans justification structurelle solide.

2. **Le pacte oligarchique en particulier** : c'est une nécessité structurelle. Il est généralement très formel (acte écrit, diète, codification collective). Chercher activement : actes de type *Libell*, ordonnances, lois de succession, chartes, pactes de primogéniture, compromis avec les états. Un pacte faiblement identifié = analyse à reprendre.

3. **Les durées sont-elles cohérentes ?** La phase est-elle proche de la norme (200 ans pour féodale/oligarchique/absolutiste, 25-80 ans pour RN) ? Si écart, est-il expliqué par une perturbation identifiée ?

4. **Le test discriminant est-il passé à la bonne échelle ?** Pour les monarchies composites (Espagne, Autriche, Saint-Empire), l'absolutisme n'est atteint que quand l'administration centrale a préséance sur TOUTES les administrations locales du territoire national — pas seulement celles du noyau.

5. **L'expansion a-t-elle été attribuée à la bonne phase ?** L'expansion prolonge toujours la phase EN COURS au moment où elle commence.

6. **Les durées atypiques ont-elles été expliquées par des perturbations, pas par des ajustements d'identification ?** Le test discriminant PRIME SUR les durées. Si une identification a été choisie « parce que les durées collent mieux », c'est un signal d'alarme — revérifier le test discriminant.

7. **La guerre sociale se joue-t-elle à l'échelle pertinente ?** Si le Parcours est national, la guerre sociale doit opposer des factions à l'échelle nationale, pas seulement régionale.

### Étape 2ter : Vérification globale finale — complétude événementielle

Après avoir analysé toutes les phases, effectuer une **passe globale** : lister tous les événements majeurs de l'histoire de la nation et vérifier qu'**aucun événement majeur ne reste inexpliqué** du point de vue historionomique.

**Procédure :**
1. Dresser une liste des événements majeurs documentés de l'histoire de la nation : grandes batailles, changements dynastiques, révolutions, guerres civiles, traités fondateurs, réformes administratives majeures, crises politiques notables, changements territoriaux, assassinats politiques, codifications juridiques.
2. Pour chaque événement, identifier son statut dans l'analyse :
   - Est-ce un **saillant** (éveil, pic, crise, pacte, guerre sociale, 1er monarque, IR, GR, etc.) ?
   - Est-ce une **perturbation** (mécanisme + effet) ?
   - Est-ce une **sous-phase** ou un marqueur de sous-phase ?
   - Est-ce mentionné dans la **description d'une phase/sous-phase** avec un éclairage structurel ?
3. **Un événement majeur non expliqué = analyse incomplète**. Soit intégrer l'événement (en ajoutant un saillant, une perturbation, ou une mention contextuelle), soit reconsidérer le cadrage global si l'événement ne colle pas du tout.

**Pourquoi c'est critique :** le corpus montre que les analyses bâclées manquent systématiquement des événements structurants — par exemple, sur l'Autriche v1 : manqué l'Innsbrucker Libell (1518), le gouvernement des états 1519-1522, le Wiener Neustädter Blutgericht (1522), la guerre civile Albert VI / Frédéric III (1440s-1463), la conquête de Vienne par Mathias Corvin (1485-1490). Ces omissions masquaient le vrai pacte oligarchique et la vraie dernière grande révolte oligarchique. Une vérification systématique les aurait immédiatement détectées.

### Étape 3 : Produire le fichier `parcours.md`

Créer le fichier structuré `references/nations/<nation>/parcours.md` avec :
- La section `## Superficie de référence` avec les données noyau+marges (voir `references/parcours.md` pour le format)
- Les phases, sous-phases, saillants et perturbations identifiés
- Les perturbations territoriales codées avec le bon mécanisme (`choc_heterogeneite` pour les expansions, `correction_echelle` pour les contractions) et un titre spécifique (pas « Choc d'hétérogénéité » ou « Accélérateur » mais le nom de l'événement : « Empire Plantagenêt », « Perte de la Normandie »)
- Le flag `territorial: false` sur les perturbations non territoriales (culturelles ou institutionnelles)
- Les champs normalisés (type, start, end, title, summary, description, figure, confidence)
- Des résumés (summary) en 1-2 phrases et des descriptions (description) en 3-6 phrases construites — pas de style télégraphique

Ce fichier est le **résultat final** — il ne contient que l'hypothèse retenue, pas les débats.

### Étape 4 : Produire le fichier `justification.md`

Créer le fichier `references/nations/<nation>/justification.md` qui documente :

1. **Les hésitations** — pour chaque saillant où la confiance n'est pas « high », expliquer pourquoi on a hésité, quelles alternatives ont été envisagées, et pourquoi l'hypothèse retenue a été préférée
2. **Les hypothèses écartées** — documenter les hypothèses alternatives avec leurs arguments pour et contre (comme les *machlokot* du Talmud : on conserve la trace du débat même quand la décision est prise)
3. **Les questions ouvertes** — ce qui reste à confirmer, les points qui nécessitent davantage de cas comparatifs
4. **Les comparaisons** avec les parcours connus (Israël, France) — les parallèles qui éclairent et renforcent (ou affaiblissent) l'analyse

Le fichier de justification est **séparé** du parcours : le parcours est le résultat, la justification est le raisonnement. On peut modifier l'un sans toucher l'autre.

### Étape 5 : Discuter et itérer

L'historionomie est une discipline en cours de construction. L'utilisateur peut contester une identification, proposer un saillant alternatif, ou demander d'explorer une hypothèse. Claude doit être prêt à réviser son analyse sur la base d'arguments solides, et à mettre à jour le parcours ET la justification.

## Principes importants

### Priorité absolue : fiabilité des durées

L'usage principal du corpus est la **quantification statistique** (régression d'Alyocha Coencas sur les durées de phase). Plus il y a de parcours, plus la régression est robuste. Cela implique que **la fiabilité des dates de bornes** (éveil féodal, pacte, 1er monarque oligarchique, guerre sociale, 1er monarque absolu, explosion AR, Glorieuse Révolution) est la **première priorité absolue** de toute analyse. Sous-phases, naming, descriptions sont des raffinements secondaires — les durées sont l'enjeu.

Ne jamais forcer une date pour que les durées « collent mieux ». Les écarts atypiques sont toujours le signal d'une perturbation à identifier, pas d'une borne à déplacer.

### Naming canonique — liste fermée obligatoire

**Phases** (liste fermée, aucune dérivation) :
- `phase pré-féodale`, `phase féodale`, `phase oligarchique`, `phase absolutiste`, `révolution nationale`, `phase parlementaire`

**Sous-phases** (liste fermée) :
- `percolation élitaire` (pré-féodale)
- `coagulation des élites`, `bascule oligarchique` (féodale)
- `essor oligarchique`, `polarisation des élites`, `guerre sociale` (oligarchique)
- `absolutisation`, `impérialisme absolutiste`, `ancien régime` (absolutiste). Dérivation rare : `ancien régime exogène`.
- `révolution initiale`, `impérialisme revanchard`, `restauration` (RN)

Dérivations exceptionnelles uniquement sur précédent documenté (ex. : `nouveau PO` pour la France 1418-1429).

**Titres de saillants — LISTE FERMÉE** (aucune dérivation autorisée) :
- **Féodale** : Éveil féodal, Pic féodal, Crise féodale, Pacte oligarchique
- **Oligarchique** : 1er monarque oligarchique, Acmé oligarchique, Fin de l'expansion, Guerre sociale
- **Absolutiste** : 1er monarque absolu, Dernière grande révolte oligarchique (DGRO), Pic absolutiste, Fin de l'expansion, Remontrance
- **RN** : Explosion de l'Ancien Régime, Expérience parlementaire, Phase aiguë, Moment thermidorien, Impérialiste Revanchard, Restauration, Glorieuse Révolution

**Distinction saillant vs sous-phase** :
- `Ancien régime` est une sous-phase **seulement** (pas un saillant). Le « moment » de l'entrée en AR est marqué par la Remontrance, pas par un saillant « Ancien Régime ».
- `Révolution initiale` est une sous-phase **seulement** — elle contient à l'intérieur les 4 saillants : Explosion de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien.
- `Restauration` est à la fois un **saillant** (le moment où l'ancien ordre est restauré — ex. 1815 en France) ET une **sous-phase** (la durée pendant laquelle il dure — ex. 1815-1830).
- `Impérialiste Revanchard` (-*iste*) est un **saillant** — l'avènement de la figure (ex. Bonaparte 1er consul, 1799). `impérialisme revanchard` (-*isme*) est la **sous-phase** — la durée pendant laquelle la nation est portée par cette dynamique (ex. 1799-1815).

**Tout événement qui n'est pas dans la liste fermée n'est PAS un saillant** — c'est soit une **perturbation** (avec mécanisme + effet, parcimonieusement), soit une **mention dans la description** d'une sous-phase. Ne JAMAIS créer des saillants ad hoc avec des noms inventés (« Victoire de la Contre-Réforme », « Compromis austro-hongrois », « Privilegium Minus »). Les saillants sont des éléments codifiés.

**Événements perturbateurs** : nom historique sec (« Traité de Neuberg », « Innsbrucker Libell »), pas des descriptions narratives.

**Figures historiques** : nom seul. Surnoms UNIQUEMENT s'ils sont historiographiques canoniques et utiles à la désambiguïsation. Jamais d'épithètes ajoutées par goût littéraire (« le Glorieux », « le Fondateur »).

**Règle simple** : un titre de phase, sous-phase ou saillant est une étiquette de catalogage dans un vocabulaire canonique fermé, pas un titre de chapitre.

### Bornes de sous-phases — règles opératoires

Consulter `references/sous_phases.md` pour la grille complète des marqueurs. Règles fondamentales :

1. **Une borne est toujours un saillant ou un événement identifiable** — jamais une date « arrondie approximative ».
2. **La fin d'une sous-phase et le début de la suivante coïncident** (ou se chevauchent de 1-2 ans maximum).
3. **Les bornes ne doivent pas être forcées** pour obtenir des durées typiques.
4. **Quand une sous-phase optionnelle est absente** (bascule oligarchique comprimée, IR absent, ancien régime écourté), justifier structurellement pourquoi.
5. **DGRO — la Dernière Grande Révolte Oligarchique est un saillant de FIN de phase oligarchique ou de DÉBUT de phase absolutiste** (pendant l'absolutisation), jamais au début de la phase oligarchique. Le mot « dernière » a un sens structurel : c'est le dernier sursaut oligarchique avant l'ancrage absolutiste.

### Catégorisation des événements historiques — 4 catégories

Tout événement historique mentionné dans un parcours relève de l'une de quatre catégories. Pas de « zone grise » — si un événement ne rentre pas clairement dans une catégorie, il faut trancher.

1. **Saillant canonique** — figure dans la liste fermée (cf. section Naming canonique). Affichage : rond de la couleur de la phase.
2. **Perturbation** — événement qui passe le **triple test** :
   - **mécanisme** identifiable parmi : choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire
   - **effet** identifiable parmi : prolongement, accélération, avortement, reboot
   - **impact réel** sur la trajectoire du Parcours : la durée, le niveau ou la direction d'une phase aurait été différente sans cet événement
   
   Affichage : losange coloré (« diamant »).
3. **Anecdote de parcours** — événement historique sans impact sur la trajectoire (défaite mineure, scandale politique ordinaire, crise financière ponctuelle, figure mineure). Ne pas marquer dans le parcours structuré ; au plus mentionner en passant dans la description d'une sous-phase.
4. **Élément nouveau théorique** — événement qui semble structurellement important mais ne rentre dans aucune des trois catégories. **À remonter explicitement** pour discussion théorique, plutôt que de forcer artificiellement dans une catégorie existante.

**Règles opératoires** :
- **Les saillants canoniques ont priorité** : si un événement peut être un saillant canonique, le mettre en saillant, pas en perturbation. Exception : les **crises féodales** sont techniquement à la fois canoniques ET perturbations (insuffisance interne / avortement) — seul cas de chevauchement formel documenté.
- **Pas de plafond numérique** : une nation très perturbée peut légitimement avoir 15 perturbations, une nation calme peut n'en avoir que 3. L'important est que chaque perturbation passe le triple test. Le compte est un résultat, pas une contrainte.
- **Distinguer « faible intensité » (anecdote) de « fort impact » (perturbation)** : une défaite militaire ordinaire est une anecdote ; une occupation étrangère qui détruit les institutions est une perturbation.

### Terminologie stricte

- **Parcours** (majuscule) : le Parcours de construction nationale
- **Sous-phases** : découpage mécanique d'une phase (liste canonique fermée, voir ci-dessus)
- **Saillants** : éléments ponctuels facilement identifiables dans le vocabulaire canonique
- **Classe prébendière / patrimoniale** (Weber) : jamais « mobilière / immobilière »
- **Clivage gauche-droite** : ED (réactionnaires), D (conservateurs), G (réformateurs), EG (révolutionnaires) — définitions structurelles, valables partout et tout le temps

### Les deux moteurs sont la clé

Toute analyse doit être ancrée dans les deux moteurs :
1. **Construction de l'État central** — appareil administratif, fiscal, militaire
2. **Homogénéisation culturelle** — langue, religion, droit, mœurs, conscience nationale

Pour situer une nation, observer le degré de centralisation de l'État et le degré d'homogénéité culturelle. Pour comprendre un écart de durée, chercher ce qui a perturbé l'un ou l'autre.

### Durées typiques et écarts

| Phase | Durée endogène |
|---|---|
| Féodale | ~200 ans |
| Oligarchique | ~200 ans |
| Absolutiste | ~200 ans |
| Révolution Nationale | ~25-80 ans |
| Parlementaire | Très longue |

Les écarts sont toujours significatifs. Ne pas les ignorer — les expliquer.

### Humilité épistémique

L'historionomie est un cadre en construction. Certains saillants sont bien établis (éveil féodal, 1er monarque oligarchique, guerre sociale), d'autres sont encore en cours de validation (pic féodal, acmé oligarchique). Signaler les incertitudes plutôt que de forcer une identification.

Quand l'analyse d'une nouvelle nation révèle un cas qui ne colle pas au modèle, c'est potentiellement une découverte — pas un échec. Le signaler et en discuter.

### Langue

Ce skill est rédigé en français. Les discussions peuvent se faire en français ou en anglais selon la préférence de l'utilisateur.
