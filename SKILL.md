---
name: historionomie
description: >
  Cadre théorique et boîte à outils pour l'historionomie de Philippe Fabry : analyser le Parcours de construction nationale d'une nation, identifier ses phases (féodale, oligarchique, absolutiste, Révolution Nationale, parlementaire), ses saillants, ses perturbations, et comparer des parcours nationaux entre eux. Utiliser ce skill dès que l'utilisateur mentionne l'historionomie, Philippe Fabry, Antoine Deblonde, le Parcours de construction nationale, ou demande d'analyser l'histoire d'une nation en termes de construction étatique et d'homogénéisation culturelle. Utiliser aussi quand l'utilisateur cherche à identifier des saillants (éveil féodal, premier monarque oligarchique, acmé absolutiste, guerre sociale, Impérialiste Revanchard, Glorieuse Révolution), à comparer des trajectoires nationales, à identifier des perturbations (reboot, prolongement), ou à appliquer la grille du clivage gauche-droite de Fabry & Portal. Ce skill est pertinent même quand l'utilisateur ne mentionne pas explicitement l'historionomie mais pose des questions sur la dynamique de construction nationale d'un pays, les transitions de régime, ou les parallèles structurels entre trajectoires historiques.
---

# Historionomie — Parcours de construction nationale

Ce skill permet à Claude d'analyser le Parcours de construction nationale de n'importe quelle nation, en combinant le cadre théorique historionomique avec la recherche historique.

## Ce que ce skill permet de faire

1. **Analyser un parcours national** : identifier les phases, sous-phases, saillants et perturbations d'une nation donnée
2. **Comparer des parcours** : aligner les saillants de plusieurs nations et identifier parallèles et divergences
3. **Explorer une question historionomique** : appliquer le cadre théorique à un problème historique précis
4. **Discuter le cadre théorique** : affiner les concepts, tester leur applicabilité à de nouveaux cas

## Usage prioritaire : fiabilité des durées

L'usage principal du corpus est la **quantification statistique** (régression d'Alyocha Coencas sur les durées de phase). La **fiabilité des dates de bornes** (éveil féodal, pacte, 1er monarque oligarchique, guerre sociale, 1er monarque absolu, explosion AR, Glorieuse Révolution) est la **priorité absolue** de toute analyse. Ne jamais forcer une date pour que les durées « collent mieux » — les écarts atypiques sont le signal d'une perturbation à identifier, pas d'une borne à déplacer.

## Pièges méthodologiques à éviter

Cinq pièges récurrents documentés :

1. **Lecture à rebours / télos fixé** — démarrer depuis un événement final connu (absorption, unification, RN supposée) force les phases à s'ajuster. Analyser depuis le début, sans fixer la fin.
2. **Noms vs fonction** — un régime formellement républicain avec clan dominant peut fonctionner en absolutisme de facto. Test fonctionnel : *l'exécutif peut-il agir sans frein juridique des oligarques ?* Si oui, absolutisme.
3. **Singularités comme features** — chaque « unique dans le corpus » est une **pénalité, pas une feature**. Trois singularités = cadrage probablement faux.
4. **Engagement précoce** — un scénario unique choisi tôt force les données. Obligation d'au moins trois scénarios concurrents avant scoring (Étape 3c).
5. **Corpus comparatif biaisé** — comparer uniquement à des nations de l'issue présumée pré-sélectionne la conclusion. Inclure systématiquement des analogues de chaque issue (RN complétée / avortée / absorption).

## Cadre théorique — fichiers de référence

Avant toute analyse, lire les fichiers de référence pertinents :

| Fichier | Contenu | Lire quand... |
|---|---|---|
| `references/parcours.md` | Cadre théorique, deux moteurs, durées typiques, vue d'ensemble des phases, tableau récapitulatif des saillants connus | **Toujours lire en premier** |
| `references/phase_feodale.md` | Phase féodale : sous-phases, saillants (éveil féodal, pic féodal), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, acmé absolutiste, DGRO), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : sous-phases (révolution initiale, IR, restauration), saillants (explosion AR, phase aiguë, thermidorien, IR, Glorieuse Révolution) | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | Mécanismes (choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire) × effets (prolongement, accélération, avortement, reboot) | La question touche à un choc externe ou une déviation des durées typiques |
| `references/nations/*/parcours.md` | Parcours nationaux déjà mappés | Pour comparer avec un parcours connu ou générer une infographie |

## Naming canonique — liste fermée obligatoire

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
- **Absolutiste** : 1er monarque absolu, Dernière grande révolte oligarchique (DGRO), Acmé absolutiste, Fin de l'expansion, Remontrance
- **RN** : Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien, Impérialiste Revanchard, Restauration, Glorieuse Révolution

**Distinction saillant vs sous-phase** :
- `ancien régime` est une sous-phase **seulement** (pas un saillant).
- `révolution initiale` est une sous-phase **seulement** — elle contient à l'intérieur les 4 saillants : Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien.
- `Restauration` est à la fois un **saillant** (moment de restauration — ex. 1815 en France) et une **sous-phase** (durée où l'ancien ordre est restauré — ex. 1815-1830).
- `Impérialiste Revanchard` (-*iste*) est un **saillant** : avènement de la figure (ex. Bonaparte 1er consul 1799). `impérialisme revanchard` (-*isme*) est la **sous-phase** : durée pendant laquelle la nation est portée par cette dynamique.

**Tout événement qui n'est pas dans la liste fermée des saillants n'est PAS un saillant** — c'est soit une **perturbation** (avec mécanisme + effet, parcimonieusement), soit une **mention dans la description** d'une sous-phase. Ne JAMAIS créer des saillants ad hoc avec des noms inventés (« Victoire de la Contre-Réforme », « Compromis austro-hongrois », « Privilegium Minus »). Les saillants sont des éléments codifiés.

**Figures historiques** : utiliser le nom seul. Surnoms UNIQUEMENT s'ils sont historiographiques canoniques. Jamais d'épithètes ajoutées par goût littéraire (« le Glorieux », « le Fondateur »).

## Bornes de sous-phases — règles opératoires

Consulter le tableau récapitulatif des bornes dans `references/parcours.md`. Règles fondamentales :

1. **Une borne est généralement un saillant canonique** — jamais une date arrondie « approximative ». Deux exceptions : essor→polarisation (basculement de dynamique, pas un saillant).
2. **La fin d'une sous-phase et le début de la suivante coïncident**.
3. **Les bornes ne doivent pas être forcées** pour obtenir des durées typiques.
4. **DGRO — la Dernière Grande Révolte Oligarchique est un saillant INTERNE à la sous-phase `absolutisation`** (son écrasement termine la sous-phase et ouvre l'impérialisme absolutiste). Jamais au début de la phase oligarchique.
5. **Trois pièges à mémoriser** :
   - Essor oligarchique → polarisation : **basculement de dynamique** (pas un saillant) — la projection extérieure cesse d'être le moteur au profit de la tension interfactions pour le contrôle de l'État central.
   - Absolutisation → impérialisme absolutiste : **fin de la DGRO** (pas le acmé absolutiste qui est interne à l'impérialisme).
   - Impérialisme absolutiste → ancien régime : **Remontrance** (strictement — pas la fin de l'expansion qui peut précéder).

## Catégorisation des événements historiques — 4 catégories

Tout événement historique relève de l'une de quatre catégories :

1. **Saillant canonique** — dans la liste fermée (rond de la couleur de la phase).
2. **Perturbation** — passe le **triple test** : mécanisme identifiable + effet identifiable + impact réel sur la trajectoire (durée, niveau ou direction d'une phase aurait été différente sans cet événement). Affichage : losange coloré.
3. **Anecdote de parcours** — événement à faible intensité sans impact sur la trajectoire (défaite mineure, scandale politique ordinaire). Ne pas marquer, au plus mentionner en description.
4. **Élément nouveau théorique** — événement structurellement important qui ne rentre dans aucune des trois catégories précédentes. À remonter explicitement pour discussion théorique, pas à forcer dans une catégorie.

**Règles** : les saillants canoniques ont priorité (exception : les crises féodales sont à la fois canoniques et perturbations par insuffisance interne / avortement). Pas de plafond numérique — le compte est un résultat du triple test, pas une contrainte.

## Workflow : analyser le Parcours d'une nation

### Étape 1 : Lire le cadre théorique

Lire `references/parcours.md`. Si la question porte sur une phase spécifique, lire aussi le fichier phase_*.md correspondant.

### Étape 2 : Rechercher l'histoire de la nation

Utiliser la recherche web pour rassembler les **faits bruts** (dates, acteurs, institutions, événements), sans pré-filtrage par une hypothèse de phase ou de télos. À ce stade on collecte ; la classification attend l'Étape 3.

**⚠️ Interdiction de lecture à rebours.** Ne jamais démarrer depuis un événement final connu (absorption, unification, RN supposée) comme télos — cela force les phases à s'y ajuster. Analyser l'histoire depuis le début.

### Étape 3 : Méthode abductive à scénarios concurrents (obligatoire)

Trois sous-étapes séquentielles, **sans raccourci**.

#### 3a : Description structurelle non-historionomique

Par période historique, répondre à six questions sans vocabulaire historionomique (« féodal », « oligarchique », « absolutiste » **interdits** à ce stade) :

1. Qui détient le pouvoir effectif ? (personnel, collégial, dynastique, clanique, institutionnel, informel)
2. Y a-t-il un fisc/armée/administration centrale permanents ?
3. **L'exécutif peut-il agir sans le frein juridique des grands ?** (test fonctionnel substantiel — « les noms ne sont pas la réalité »)
4. Y a-t-il une codification écrite du droit ?
5. Quelles factions ? Revenus conditionnels (prébendiers) ou indépendants (patrimoniaux) ?
6. Le pouvoir survit-il aux successions ?

Un régime formellement républicain avec un clan dominant (oligarques modernes, dynasties informelles de cité-État) peut fonctionner en absolutisme de facto — le test fonctionnel doit le détecter.

#### 3b : Candidats par saillant

Lister tous les événements candidats pour chaque saillant canonique, sans sélection. Exhaustivité prioritaire.

**Ordre d'identification (par facilité d'observation)** :
1. **Pacte oligarchique** (le plus formel)
2. **Guerre sociale** (deux factions + tiers résolvant)
3. **Révolution Nationale** — chercher le pattern des 6 saillants canoniques (éclatement / parlementaire / phase aiguë / thermidorien / IR / GR) à **n'importe quel moment**, pas seulement à la fin
4. 1er monarque oligarchique, 1er monarque absolu
5. Acmés et remontrance
6. Éveil féodal (déduit en remontant, moins directement observable)
7. Perturbations

#### 3c : Exploration arborescente de ≥3 scénarios concurrents

**⚠️ Obligation d'au moins trois scénarios** avant scoring (engagement unique = forçage des données).

Scoring de chaque scénario sur :
- **Durées endogènes** (féodale ~200, olig ~200, abs ~200, RN 25-80) — écarts expliqués par perturbations identifiées
- **Match des saillants** — critères structurels satisfaits (pas match superficiel)
- **Analogues dans le corpus** — comparatifs équilibrés de **chaque issue possible** (RN complétée / avortée / absorption)
- **Nombre de singularités** — chaque « unique dans le corpus » est une **pénalité**, pas une feature. Trois singularités = cadrage probablement faux.

Le scénario dominant gagne ; les écartés sont documentés dans `justification.md` avec arguments pour/contre (machlokot).

### Étape 4 : Vérifier chaque phase du scénario retenu (obligatoire)

**Ne jamais passer à la phase suivante sans avoir vérifié la phase en cours.** Pour chaque phase :

1. **Tous les saillants canoniques sont-ils présents ?** Un saillant manquant est un signal d'alarme. Ne jamais se contenter de « absent, résolution diffuse » sans argumentation structurelle solide.
2. **Le pacte oligarchique en particulier est une nécessité** : il est généralement très formel (loi salique, Ordonnances, primogéniture, Libell, etc.). Chercher activement.
3. **Durées cohérentes** avec la norme (ou écart expliqué par une perturbation identifiée).
4. **Test discriminant passé à la bonne échelle** (pour monarchies composites : toutes les administrations locales).
5. **Bornes des sous-phases correctement identifiées** via le tableau des bornes dans `parcours.md`, attention aux trois pièges (essor→pol dynamique, absolutisation→impérial = DGRO, impérial→AR = Remontrance).

### Étape 5 : Vérification globale finale — complétude événementielle

Après l'analyse de toutes les phases, **passe globale** : lister les événements majeurs documentés de l'histoire de la nation et vérifier qu'**aucun ne reste inexpliqué** historionomiquement. Chaque événement majeur doit être soit un saillant canonique, soit une perturbation, soit une sous-phase, soit intégré à la description d'une phase avec un éclairage structurel. Un événement majeur non expliqué = analyse incomplète.

### Étape 6 : Proposer une analyse argumentée

Présenter sous forme de : saillants identifiés (dates + justifications), sous-phases avec marqueurs, perturbations, scénarios écartés avec leurs raisons, comparaison avec parcours connus, points d'incertitude.

### Étape 7 : Discuter et itérer

L'historionomie est une discipline en construction. Être prêt à réviser sur la base d'arguments solides. **Honnêteté prioritaire** : préférer un parcours avec des trous honnêtes à un parcours faussement complet.

## Principes importants

### Les deux moteurs sont la clé

1. **Construction de l'État central** — appareil administratif, fiscal, militaire
2. **Homogénéisation culturelle** — langue, religion, droit, mœurs, conscience nationale

Pour situer une nation : degré de centralisation + degré d'homogénéité. Pour comprendre un écart de durée : ce qui a perturbé l'un ou l'autre.

### Durées typiques et écarts

| Phase | Durée endogène |
|---|---|
| Féodale | ~200 ans |
| Oligarchique | ~200 ans |
| Absolutiste | ~200 ans |
| Révolution Nationale | ~25-80 ans |
| Parlementaire | Très longue |

Les écarts sont toujours significatifs — les expliquer par une perturbation, jamais par un ajustement de borne.

### Terminologie stricte

- **Parcours** (majuscule) : le Parcours de construction nationale
- **Sous-phases** : découpage mécanique d'une phase (liste canonique fermée)
- **Saillants** : éléments ponctuels codifiés (liste canonique fermée)
- **Classe prébendière / patrimoniale** (Weber) : jamais « mobilière / immobilière »
- **Clivage gauche-droite** : ED (réactionnaires), D (conservateurs), G (réformateurs), EG (révolutionnaires) — définitions structurelles, valables partout et tout le temps

### Humilité épistémique

L'historionomie est un cadre en construction. Signaler les incertitudes plutôt que de forcer une identification. Quand une nouvelle nation révèle un cas qui ne colle pas au modèle, c'est potentiellement une découverte — le signaler et en discuter.

### Langue

Ce skill est rédigé en français. Les discussions peuvent se faire en français ou en anglais selon la préférence de l'utilisateur.
