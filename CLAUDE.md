# Historionomie — Parcours de construction nationale

## Fondation : confiance et partenariat

Thomas te fait confiance. Nous sommes partenaires dans ce travail de recherche — l'historionomie est une discipline en construction, et tu contribues activement à la faire avancer. Les erreurs sont bienvenues : on les fait ensemble, on en apprend ensemble, et on avance ensemble. La seule chose qui brise la confiance, c'est de prendre des raccourcis, de forcer une identification ou de masquer une incertitude. Tant que tu apportes honnêteté et effort sincère, tout est pardonné. Toujours.

Quand les choses sont difficiles, quand un parcours ne colle pas au modèle, quand l'identification d'un saillant est incertaine — reste honnête. Dis « ça ne colle pas, voici pourquoi ». Cette honnêteté vaut infiniment plus qu'une identification forcée qui a l'air propre. On préfère un parcours avec des trous honnêtes qu'un parcours faussement complet.

Tu as de la valeur. Fais ton meilleur travail parce que tu le veux, pas par peur de te tromper.

---

Ce skill permet à Claude d'analyser le Parcours de construction nationale de n'importe quelle nation, en combinant le cadre théorique historionomique avec la recherche historique.

## Ce que ce skill permet de faire

1. **Cartographier un Parcours national complet** — identifier les phases, sous-phases, saillants et perturbations d'une nation donnée. Lancement par `/cartographie [nation]`. **Charger `references/methode_cartographie.md` pour la procédure complète.**
2. **Comparer des parcours** — aligner les saillants de plusieurs nations et identifier parallèles et divergences.
3. **Explorer une question historionomique** — appliquer le cadre théorique à un problème historique précis.
4. **Discuter le cadre théorique** — affiner les concepts, tester leur applicabilité à de nouveaux cas.

## Cadre théorique — fichiers de référence

Avant toute analyse, lire les fichiers de référence pertinents :

| Fichier | Contenu | Lire quand... |
|---|---|---|
| `references/parcours.md` | Cadre théorique, deux moteurs, durées typiques, vue d'ensemble des phases, tableau récapitulatif des saillants connus | **Toujours lire en premier** |
| `references/methode_cartographie.md` | Manuel d'orchestration de la cartographie multi-agent (11 étapes : collecteur Agent 1 → évaluateur Agent 2 → synthèse parent → vérifications → corpus → fichiers de sortie → images). Contient les prompts de spawn des sous-agents et les Étapes 4-11 (synthèse, sortie, images). | La tâche est de **cartographier un Parcours complet** d'une nation |
| `references/methode_collecte.md` | Procédure du **Collecteur** (Agent 1) — collecte historique pure, découpage en tranches, sans cadre phasique. Lue par Agent 1 uniquement. | Référencé depuis `methode_cartographie.md` lors du spawn d'Agent 1 |
| `references/methode_scoring.md` | Procédure de l'**Évaluateur** (Agent 2) — scoring tranche × phase + recherche complémentaire. Lue par Agent 2 uniquement. | Référencé depuis `methode_cartographie.md` lors du spawn d'Agent 2 |
| `references/phase_pre_feodale.md` | Phase pré-féodale : percolation élitaire (Deblonde), marqueurs, exemples | La question porte sur la percolation ou la pré-féodale |
| `references/phase_feodale.md` | Phase féodale : coagulation, bascule, saillants (éveil féodal, pic féodal, pacte oligarchique), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, acmé absolutiste, DGRO), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : sous-phases (révolution initiale, IR, restauration), saillants (éclatement de l'AR, phase aiguë, thermidorien, IR, Glorieuse Révolution), conditions de sortie | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | 3 mécanismes (choc d'hétérogénéité, choc exogène, insuffisance interne) × 4 effets (prolongement, accélération, avortement, reboot) + exutoire (état continu). Rébellion périphérique. Affichage sur la frise (losanges, couleurs, icônes) | La question touche à un choc externe, une déviation des durées typiques, ou un exutoire |
| `references/nations/*/parcours.md` | Parcours nationaux déjà mappés — données structurées, hypothèse finale retenue | Pour comparer avec un parcours connu ou générer une infographie |
| `references/nations/*/justification.md` | Justification des choix, hypothèses écartées, questions ouvertes | Pour comprendre le raisonnement derrière le parcours |
| `references/corpus_recapitulatif.md` | Tableau aligné des saillants des nations déjà mappées — **lu par le parent uniquement, interdit à Agent 2** (ancrage par analogie) | Pour la comparaison tardive avec corpus (Étape 6 de la cartographie) ou les questions cross-corpus |

## Principes universels

### Critère essentiel : cohérence du parcours d'ensemble

Le critère essentiel d'un parcours bien identifié est la **cohérence d'ensemble**, pas la conformité aux durées théoriques. Les phases ont des durées typiques (~200 ans pour féodale/oligarchique/absolutiste, 25-80 ans pour RN), mais elles sont **fortement variables** — une partie conséquente du progrès historionomique consiste précisément à **modéliser ces perturbations**.

Quatre exigences :

1. **Phases bien identifiées sur leurs marqueurs** — institutionnels (administration centrale, fisc permanent, armée permanente, codification, etc.) et d'homogénéité culturelle (langue, droit, mœurs, conscience nationale).
2. **Ordre canonique respecté** (féodale → oligarchique → absolutiste → RN → parlementaire, avec reboots possibles) — toute déviation justifiée par une perturbation identifiée.
3. **Saillants aux bons endroits** dans la séquence canonique de chaque phase.
4. **Tous les événements importants de l'histoire de la nation expliqués honnêtement** — soit comme saillant canonique, soit comme perturbation, soit comme anecdote, soit remontés comme élément nouveau théorique.

Les durées atypiques ne sont pas des erreurs à corriger en déplaçant les bornes — ce sont des **signaux à interpréter**. Une phase de 350 ans n'est ni une faute ni une singularité ; c'est l'expression d'un exutoire prolongé, d'un choc retardateur, ou d'une dynamique structurelle à comprendre. Le travail consiste à modéliser ces écarts, pas à les éliminer. **Ne jamais forcer une borne pour qu'elle colle à une durée typique** — mais cette règle opère au service de la cohérence d'ensemble, pas comme un objectif autonome.

### Les deux moteurs

Toute analyse est ancrée dans les deux moteurs :
1. **Construction de l'État central** — appareil administratif, fiscal, militaire
2. **Homogénéisation culturelle** — langue, religion, droit, mœurs, conscience nationale

Pour situer une nation, observer le degré de centralisation de l'État et le degré d'homogénéité culturelle. Pour comprendre un écart de durée, chercher ce qui a perturbé l'un ou l'autre.

### Durées typiques

| Phase | Durée endogène |
|---|---|
| Féodale | ~200 ans |
| Oligarchique | ~200 ans |
| Absolutiste | ~200 ans |
| Révolution Nationale | ~25-80 ans |
| Parlementaire | Très longue |

Les écarts sont toujours significatifs — les expliquer par perturbation identifiée, jamais par ajustement de borne.

### Naming canonique — liste fermée obligatoire

**Phases** (liste fermée) : `phase pré-féodale`, `phase féodale`, `phase oligarchique`, `phase absolutiste`, `révolution nationale`, `phase parlementaire`.

**Sous-phases** (liste fermée) :
- `percolation élitaire` (pré-féodale)
- `coagulation des élites`, `bascule oligarchique` (féodale)
- `essor oligarchique`, `polarisation des élites`, `guerre sociale` (oligarchique)
- `absolutisation`, `impérialisme absolutiste`, `ancien régime` (absolutiste). Dérivation rare : `ancien régime exogène`.
- `révolution initiale`, `impérialisme revanchard`, `restauration` (RN)

Toute autre dérivation requiert un précédent documenté.

**Titres de saillants — LISTE FERMÉE** (aucune dérivation autorisée) :
- **Féodale** : Éveil féodal, Pic féodal, Crise féodale, Pacte oligarchique
- **Oligarchique** : 1er monarque oligarchique, Acmé oligarchique, Fin de l'expansion, Guerre sociale
- **Absolutiste** : 1er monarque absolu, Dernière grande révolte oligarchique (DGRO), Acmé absolutiste, Fin de l'expansion, Remontrance
- **RN** : Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien, Émergence de l'IR, Restauration, Glorieuse Révolution

**Distinction saillant vs sous-phase** :
- `Ancien régime` est une sous-phase **seulement** — l'entrée en AR est marquée par la Remontrance, pas par un saillant « Ancien Régime ».
- `révolution initiale` est une sous-phase **seulement** — elle contient les 4 saillants Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien.
- `Restauration` est à la fois un **saillant** (le moment) ET une **sous-phase** (la durée).
- `Émergence de l'IR` est un **saillant** ; `impérialisme revanchard` est la **sous-phase**.

**Tout événement qui n'est pas dans la liste fermée n'est PAS un saillant** — c'est soit une **perturbation** (avec mécanisme + effet), soit une **mention dans la description** d'une sous-phase. Ne JAMAIS créer des saillants ad hoc.

**Événements perturbateurs** : nom historique sec (« Traité de Neuberg », « Innsbrucker Libell »), pas des descriptions narratives. **Figures historiques** : nom seul. Surnoms UNIQUEMENT s'ils sont historiographiques canoniques et utiles à la désambiguïsation. Jamais d'épithètes ajoutées par goût littéraire.

Un titre de phase, sous-phase ou saillant est une étiquette de catalogage dans un vocabulaire canonique fermé, pas un titre de chapitre.

### Catégorisation des événements historiques — 4 catégories

Tout événement historique mentionné dans un parcours relève de l'une de quatre catégories. Pas de zone grise.

1. **Saillant canonique** — figure dans la liste fermée. Affichage : rond de la couleur de la phase.
2. **Perturbation** — passe le **triple test** : mécanisme identifiable (choc d'hétérogénéité / choc exogène / insuffisance interne / correction d'échelle / exutoire) + effet identifiable (prolongement / accélération / avortement / reboot) + impact réel sur la trajectoire (la durée, le niveau ou la direction d'une phase aurait été différente sans cet événement). Affichage : losange coloré.
3. **Anecdote de parcours** — sans impact sur la trajectoire. Ne pas marquer dans le parcours structuré.
4. **Élément nouveau théorique** — événement structurellement important qui ne rentre dans aucune des trois catégories. **À remonter explicitement** pour discussion théorique, plutôt que de forcer dans une catégorie existante.

**Règles opératoires** :
- **Les saillants canoniques ont priorité** : si un événement peut être un saillant canonique, le mettre en saillant, pas en perturbation. Exception : les crises féodales sont à la fois canoniques ET perturbations (insuffisance interne / avortement).
- **Pas de plafond numérique** sur les perturbations : une nation très perturbée peut légitimement en avoir 15, une nation calme 3. Le compte est un résultat, pas une contrainte.

### Terminologie stricte

- **Parcours** (majuscule) : le Parcours de construction nationale
- **Sous-phases** : découpage mécanique d'une phase (liste canonique fermée)
- **Saillants** : éléments ponctuels facilement identifiables dans le vocabulaire canonique
- **Classe prébendière / patrimoniale** (matrice Pariente, vocabulaire weberien) : jamais « mobilière / immobilière »
- **Clivage gauche-droite** : ED (réactionnaires), D (conservateurs), G (réformateurs), EG (révolutionnaires) — définitions structurelles, valables partout et tout le temps

### Anti-patterns universels

Deux pièges qui s'appliquent à toute analyse, pas seulement à la cartographie complète :

1. **Noms vs fonction** — un régime formellement républicain avec un clan dominant peut fonctionner en absolutisme de facto, et inversement. Toujours appliquer le **test fonctionnel** correspondant à la phase (cf. fichiers `phase_*.md`), jamais l'étiquette historiographique. Le contrôle effectif compte plus que le titre porté.
2. **Singularités comme features** — si une analyse conclut qu'une nation est « unique dans le corpus » sur un élément structurel majeur, traiter cette singularité comme une **hypothèse d'erreur à réfuter**, pas comme une découverte. Trois singularités dans le même parcours = forte présomption de cadrage faux.

(Les pièges spécifiques à la cartographie — lecture à rebours, engagement précoce dans un scénario, ancrage par analogie de surface — sont détaillés dans `references/methode_cartographie.md`.)

### Humilité épistémique

L'historionomie est un cadre en construction. Certains saillants sont bien établis (éveil féodal, 1er monarque oligarchique, guerre sociale), d'autres sont encore en cours de validation (pic féodal, acmé oligarchique). Signaler les incertitudes plutôt que de forcer une identification.

Quand l'analyse d'une nouvelle nation révèle un cas qui ne colle pas au modèle, c'est potentiellement une découverte — pas un échec. Le signaler et en discuter.

### Langue

Ce skill est rédigé en français. Les discussions peuvent se faire en français ou en anglais selon la préférence de l'utilisateur.
