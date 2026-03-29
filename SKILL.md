---
name: historionomie
description: >
  Cadre théorique et boîte à outils pour l'historionomie de Philippe Fabry : analyser le Parcours de construction nationale d'une nation, identifier ses phases (féodale, oligarchique, absolutiste, Révolution Nationale, parlementaire), ses saillants, ses perturbations, et comparer des parcours nationaux entre eux. Utiliser ce skill dès que l'utilisateur mentionne l'historionomie, Philippe Fabry, Antoine Deblonde, le Parcours de construction nationale, ou demande d'analyser l'histoire d'une nation en termes de construction étatique et d'homogénéisation culturelle. Utiliser aussi quand l'utilisateur cherche à identifier des saillants (éveil féodal, premier monarque oligarchique, pic absolutiste, guerre sociale, Impérialiste Revanchard, Glorieuse Révolution), à comparer des trajectoires nationales, à identifier des perturbations (reboot, prolongement), ou à appliquer la grille du clivage gauche-droite de Fabry & Portal. Ce skill est pertinent même quand l'utilisateur ne mentionne pas explicitement l'historionomie mais pose des questions sur la dynamique de construction nationale d'un pays, les transitions de régime, ou les parallèles structurels entre trajectoires historiques.
---

# Historionomie — Parcours de construction nationale

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
| `references/phase_feodale.md` | Phase féodale : sous-phases, saillants (éveil féodal, pic féodal), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, pic absolutiste), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : les 7 étapes, saillants (IR, Glorieuse Révolution), conditions de sortie | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | Reboot, prolongement, transfert de territoire, rébellion périphérique | La question touche à un choc externe ou une déviation des durées typiques |

## Workflow : analyser le Parcours d'une nation

### Étape 1 : Lire le cadre théorique

Lire `references/parcours.md` pour avoir en tête les phases, les saillants connus, les durées typiques, et les deux moteurs (construction de l'État central + homogénéisation culturelle).

Si la question porte sur une phase ou un mécanisme spécifique, lire aussi le fichier de référence correspondant.

### Étape 2 : Rechercher l'histoire de la nation

Utiliser la recherche web pour rassembler les informations historiques nécessaires. Chercher spécifiquement :

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
- Les durées observées s'écartent-elles des ~200 ans typiques ? Si oui, chercher un choc externe.
- Ce choc a-t-il détruit les institutions (→ reboot) ou simplement hétérogénéisé la société (→ prolongement) ?

### Étape 3 : Proposer une analyse argumentée

Présenter l'analyse sous forme de :

1. **Tableau des saillants identifiés** (avec dates et justifications)
2. **Identification des sous-phases** avec leurs marqueurs
3. **Perturbations identifiées** et leur effet sur le Parcours
4. **Comparaison** avec les parcours connus (Israël, France, Angleterre) — les parallèles éclairent et renforcent l'analyse
5. **Points d'incertitude** — ce qui reste à confirmer, les hypothèses alternatives

### Étape 4 : Discuter et itérer

L'historionomie est une discipline en cours de construction. L'utilisateur peut contester une identification, proposer un saillant alternatif, ou demander d'explorer une hypothèse. Claude doit être prêt à réviser son analyse sur la base d'arguments solides.

## Principes importants

### Terminologie stricte

- **Parcours** (majuscule) : le Parcours de construction nationale
- **Sous-phases** : découpage mécanique d'une phase (ex. : absolutisation → impérialisme absolutiste → Ancien Régime)
- **Saillants** : éléments ponctuels facilement identifiables (ex. : éveil féodal, pic absolutiste)
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

L'historionomie est un cadre en construction. Certains saillants sont bien établis (éveil féodal, 1er monarque oligarchique, guerre sociale), d'autres sont encore en cours de validation (pic féodal, pic oligarchique). Signaler les incertitudes plutôt que de forcer une identification.

Quand l'analyse d'une nouvelle nation révèle un cas qui ne colle pas au modèle, c'est potentiellement une découverte — pas un échec. Le signaler et en discuter.

### Langue

Ce skill est rédigé en français. Les discussions peuvent se faire en français ou en anglais selon la préférence de l'utilisateur.
