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
| `references/phase_feodale.md` | Phase féodale : sous-phases, saillants (éveil féodal, pic féodal), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, pic absolutiste), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : les 7 étapes, saillants (IR, Glorieuse Révolution), conditions de sortie | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | Reboot, prolongement, transfert de territoire, rébellion périphérique | La question touche à un choc externe ou une déviation des durées typiques |
| `references/nations/*/parcours.md` | Parcours nationaux déjà mappés (Israël, France) — données structurées, hypothèse finale retenue | Pour comparer avec un parcours connu ou générer une infographie |
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
- Les durées observées s'écartent-elles des ~200 ans typiques ? Si oui, chercher un choc externe.
- Ce choc a-t-il détruit les institutions (→ reboot) ou simplement hétérogénéisé la société (→ prolongement) ?

### Étape 3 : Produire le fichier `parcours.md`

Créer le fichier structuré `references/nations/<nation>/parcours.md` avec :
- Les phases, sous-phases, saillants et perturbations identifiés
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
