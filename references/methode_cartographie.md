# Méthode de cartographie complète d'un Parcours

Manuel d'orchestration de la cartographie d'un Parcours national. À charger quand la tâche est de produire un parcours complet.

La cartographie procède en passes séparées via des sous-agents pour empêcher l'ancrage silencieux que produit une analyse en un seul passage.

---

## Architecture multi-agent

Trois rôles, chacun avec son contexte fermé :

1. **Agent 1 — Collecteur** (`references/methode_collecte.md`)
   - Collecte historique pure, découpage en tranches selon les événements forts
   - Aucun accès au cadre historionomique (interdit : `phase_*.md`, `elites.md`, `perturbations.md`, `nations/*/`, `parcours.md`)
   - Sortie : dossier brut structuré

2. **Agent 2 — Évaluateur** (`references/methode_scoring.md`)
   - Scoring tranche × phase + justifications marker par marker
   - Reçoit dossier d'Agent 1 + identité de la nation
   - Accès au cadre (`phase_*.md`, `elites.md`, `perturbations.md`, `parcours.md`) **mais pas aux `nations/*/`**
   - Peut faire des recherches web complémentaires
   - Sortie : tableau de scoring + justifications + faits supplémentaires

3. **Parent** (Claude principal) — synthèse en dialogue avec l'utilisateur
   - Construit les trois scénarios, fait les vérifications, comparaison tardive avec le corpus, produit `parcours.md` et `justification.md`

L'isolation par contextes séparés est ce qui distingue cette procédure d'une cartographie en un seul passage. Cette architecture empêche structurellement les trois pièges récurrents :
- **Lecture à rebours / télos fixé** → Agent 1 ne connaît pas le cadre, ne peut pas chercher une fin attendue
- **Engagement précoce dans un scénario** → forcé par les trois scénarios divergents à l'Étape 4
- **Ancrage par analogie de surface** → interdiction d'accès aux `nations/*/` pour Agents 1 et 2

Si l'un de ces pièges réapparaît malgré tout dans le résultat final, reprendre la cartographie.

---

## Étape 1 : Lire le cadre théorique

Lire `references/parcours.md` (cadre, deux moteurs, durées typiques, vue d'ensemble des phases). Si la nation a des particularités identifiables d'emblée (cité-État, taille non-standard, position géographique exceptionnelle), lire aussi les fichiers conceptuels pertinents (`phase_*.md`, `elites.md`, `perturbations.md`).

Ne lire **aucun** `nations/*/parcours.md` ni `justification.md` — la comparaison avec le corpus est interdite avant l'Étape 6.

---

## Étape 2 : Invoquer Agent 1 — Collecteur

Spawner un sous-agent avec :

> Tu es Agent 1 — Collecteur. La nation à étudier est : **[NATION]**.
> 
> Lis intégralement `references/methode_collecte.md` et exécute la procédure complète.
> 
> Interdiction critique : aucun accès aux fichiers `references/phase_*.md`, `references/elites.md`, `references/perturbations.md`, `references/nations/*/`, ni `references/parcours.md`.

Récupérer le dossier produit. Le conserver intégralement.

---

## Étape 3 : Invoquer Agent 2 — Évaluateur

Spawner un second sous-agent avec :

> Tu es Agent 2 — Évaluateur. La nation est : **[NATION]**.
> 
> Voici le dossier produit par le Collecteur :
> 
> ```
> [DOSSIER D'AGENT 1]
> ```
> 
> Lis intégralement `references/methode_scoring.md` puis les fichiers du cadre (`parcours.md`, `phase_*.md`, `elites.md`, `perturbations.md`). Exécute la procédure complète.
> 
> Interdiction critique : aucun accès aux `references/nations/*/`.

Récupérer le scoring produit.

---

## Étape 4 : Synthèse — Scénarios par fourches d'ambiguïté

Plutôt que de générer trois scénarios divergents arbitrairement (qui dégénèrent presque toujours en un scénario fort + deux hommes de paille), procéder par **fourches d'ambiguïté** : identifier les éléments interprétatifs où les données admettent plusieurs lectures, et générer les scénarios par combinaison de ces lectures.

### 4a : Identifier les fourches d'ambiguïté

Repérer dans le dossier + scoring les **deux éléments interprétatifs les plus ambigus** (parfois trois si la nation est très atypique, parfois un seul si la suite du parcours est consensuelle). Un élément est ambigu quand :

- Le scoring d'Agent 2 montre des scores élevés pour **plusieurs phases sur la même tranche** (ex. tranche scorée 4 en oligarchique et 4 en absolutiste)
- Un événement majeur peut raisonnablement être lu comme **deux saillants différents** (ex. pic féodal vs 1er monarque oligarchique pour la même figure)
- La **datation d'un saillant** n'est pas évidente (ex. PO via chemin A en année X ou chemin B en année X+50)
- Une **transition** peut être un reboot par choc ou un prolongement endogène
- Une **figure ou un acte** peut résoudre la guerre sociale dans deux patterns différents (tiers populiste vs faction-gagnante)

### 4b : Expliciter les lectures plausibles de chaque fourche

Pour chaque fourche identifiée, formuler **les deux (rarement plus) lectures plausibles**, en documentant pour chacune :
- Les éléments du dossier qui la soutiennent
- Les éléments du dossier qui la contraignent
- Le score d'Agent 2 qui la conforte ou la met en tension

### 4c : Construire les scénarios par combinaison

Avec **deux fourches × deux lectures**, jusqu'à **quatre scénarios** ; certaines combinaisons sont écartées comme structurellement incompatibles. Avec une seule fourche, deux scénarios suffisent.

Chaque scénario doit être **explicitement argumenté** : sur quoi repose le choix de la fourche A₁ + B₂ plutôt que A₂ + B₁ ? Les scénarios restent **historionomiquement cohérents** : phases dans l'ordre canonique (avec reboots possibles), durées plausibles ou écarts expliqués par perturbations identifiées.

Si un scénario apparaît clairement faible (ses lectures de fourche sont impossibles à argumenter sérieusement), c'est un signal qu'il n'est pas un strawman légitime à conserver pour la forme — l'élaguer.

Cette méthode produit des scénarios **fondés dans l'ambiguïté réelle des données**, pas dans une recherche artificielle de divergence. Le scénario retenu (Étape 7) gagne parce qu'il argumente mieux ses choix de fourches, pas parce qu'il est le seul présentable.

---

## Étape 5 : Vérification de cohérence interne

Pour **chaque scénario**, appliquer les contrôles suivants. Le scénario qui passe le plus de contrôles avec le moins d'ajustements forcés gagne.

### 5a : Vérification phase par phase (saillants + marqueurs)

Pour chaque phase du scénario, vérifier la présence des saillants canoniques attendus et le satisfaction des marqueurs.

#### Phase féodale
**Saillants attendus** : éveil féodal, pic(s) féodal(aux), crise(s) féodale(s), pacte oligarchique.
**Vérifications** :
- Quand apparaît le premier chef supra-régional ? (éveil féodal)
- Y a-t-il un réseau de vassalité d'homme à homme ?
- Quand apparaît une première administration centrale, un fisc, une armée permanente ? (fin de la phase féodale)

#### Phase oligarchique
**Saillants attendus** : 1er monarque oligarchique, acmé oligarchique, polarisation, guerre sociale.
**Vérifications** :
- Qui est le premier souverain disposant d'un État central (impôt + armée + administration) ?
- Y a-t-il un acte collectif garantissant la stabilité aux successions — **chemin A** (codification de la succession) OU **chemin B** (codification de l'exercice du pouvoir) ? Une nation peut combiner les deux successivement (cf. `phase_feodale.md`).
- Trois éléments structurels du PO à vérifier : codification (acte formel daté), caractère collectif (assemblée — diète, états, Landtag, Cortès, parlement, arengo, Lords Ordainers), moment de faiblesse (conditions de Deblonde : homogénéité + faiblesse du suzerain).
- **Cas textuellement invisible** : si le test discriminant est passé (succession stable, dynastie reconnue, fisc et armée permanents) sans acte attesté, considérer un PO **structurellement probable mais textuellement invisible** (précédent : Israël antique sous Omri).
- Quelles sont les deux factions en conflit (prébendière vs patrimoniale) ?
- Y a-t-il une guerre sociale identifiable, et à l'échelle nationale (pas seulement régionale) ?

#### Phase absolutiste
**Saillants attendus** : 1er monarque absolu (cf. `phase_absolutiste.md` pour les 5 formes admises — à épuiser avant de conclure à l'absence), DGRO, acmé absolutiste, fin d'expansion, remontrance, Ancien Régime.
**Vérifications** :
- Qui résout la guerre sociale et concentre le pouvoir ? Tester les deux patterns : tiers populiste neutre ET faction-gagnante qui crée un nouveau cadre.
- L'administration centrale a-t-elle préséance sur les administrations locales — sur **TOUTES** dans le cas des monarchies composites ?
- Y a-t-il un pic d'impérialisme et de prestige ? (acmé absolutiste)
- Y a-t-il sédimentation des élites, sclérose, bloc contestataire ? (Ancien Régime)
- Pour les cités-États : tester activement la **forme 4** (consortium institutionnalisé de créanciers-actionnaires oligarques qui capture progressivement les fonctions d'État).

#### Révolution Nationale
**Saillants attendus** : éclatement de l'AR, expérience parlementaire, phase aiguë, moment thermidorien, IR, restauration, Glorieuse Révolution.
**Vérifications** :
- La phase précédente porte-t-elle bien les marqueurs d'un Ancien Régime absolutiste ? **Sans AR préalable avéré, pas de RN.**
- Pattern des saillants présent ?
- Pour les cités-États ou nations de taille non-standard : ne pas s'attendre à une RN pleine. Certains saillants (IR endogène, thermidorien distinct, Glorieuse Révolution séparée) peuvent être absents ou compressés. La RN reste **aboutie** si un nouveau cadre stable émerge, **avortée** si l'ordre ancien est restauré à l'identique (cf. `phase_rn.md`).

#### Vérifications transversales

- **Durées** : écarts vs durées typiques expliqués par perturbations identifiées (mécanisme + effet) ? Rappel : la cohérence d'ensemble prime sur les durées — ne jamais déplacer une borne pour faire coller une durée.
- **Échelle** : test discriminant absolutiste à l'échelle de TOUS les territoires de la nation ; guerre sociale à l'échelle nationale.
- **Expansion** : attribuée à la phase qui était en cours quand elle a commencé (l'expansion prolonge la phase active).
- **Saillant manquant** : signal d'alarme. Soit l'histoire a été mal lue (recherche complémentaire), soit le cas est structurellement atypique (justifier alors structurellement). **Ne jamais se contenter de « absent, résolution diffuse »** sans justification solide.

### 5b : Test événement par événement

Revenir sur **chaque événement majeur** du dossier d'Agent 1 et pour chacun, poser explicitement :

> Mon interprétation de cet événement est-elle cohérente avec le scénario ? L'événement pourrait-il être autre chose que ce que j'ai supposé ?

Exemples :
- François Ier interprété comme monarque absolu alors qu'il est une acmé oligarchique ?
- Cette réforme bicamérale lue comme pacte renouvelé alors qu'elle est Glorieuse Révolution ?
- Cette figure classée comme 1er monarque absolu alors qu'elle est un pic féodal isolé ?
- Cette révolte classée en anecdote alors qu'elle ouvre une RN ?

Documenter les événements à interprétation non triviale dans `justification.md`.

**Un événement majeur non expliqué ou mal expliqué = analyse à reprendre.**

---

## Étape 6 : Comparaison tardive avec les saillants du corpus

**Seulement après l'Étape 5** : comparer les saillants retenus avec les saillants équivalents dans le corpus. Tu peux maintenant lire les `references/nations/*/parcours.md` et `justification.md` pertinents. Cette comparaison est **une validation**, pas un cadrage.

**Règle stricte** : la comparaison se fait saillant par saillant (dates, caractéristiques structurelles), jamais par récit global. Toujours « le 1er monarque absolu de cette nation présente les caractéristiques X, Y, Z ; dans le corpus, les cas comparables sont A, B, C ; les différences sont... ».

Détecte :
- **Anomalies de datation** : saillant placé très en dehors des fenêtres typiques du corpus
- **Saillants atypiques** : 1er monarque absolu sans les marqueurs habituels, guerre sociale sans tiers résolvant identifiable
- **Configurations nouvelles** : éléments structurels inédits à remonter comme éléments théoriques nouveaux

**Filtrage facultatif** : on peut restreindre le corpus pertinent par taille (grande nation / cité-État / petite nation) ou projection (type d'exutoire), mais comme outil de filtrage, jamais comme cadrage.

Si la comparaison révèle des tensions fortes (ex. durée absolutiste +200 ans par rapport à toutes les autres nations comparables), c'est un signal de retour à l'Étape 4 ou 5 — pas de réajustement ad hoc.

---

## Étape 7 : Scoring final et scénario retenu

Pour chaque scénario, scorer sur :
- **Cohérence avec le scoring d'Agent 2** — la succession des phases suit-elle les scores les plus hauts de chaque tranche ?
- **Complétude des saillants canoniques** (5a) — tous présents, ou absences structurellement justifiées ?
- **Cohérence événementielle** (5b) — aucun événement majeur mal interprété ou ignoré
- **Durées endogènes** — écarts expliqués par perturbations identifiées
- **Concordance avec le corpus** (Étape 6) — saillants plausibles
- **Nombre de singularités** — chaque affirmation « unique dans le corpus » est une **pénalité**. Trois singularités = présomption forte d'erreur de cadrage.

Le scénario avec le meilleur scoring gagne. Les scénarios écartés sont documentés dans `justification.md` avec leurs arguments pour et contre (machlokot — on conserve la trace du débat).

---

## Étape 8 : Produire le fichier `parcours.md`

Créer `references/nations/<nation>/parcours.md` avec :
- Section `## Superficie de référence` (noyau + marges, format dans `references/parcours.md`)
- Phases, sous-phases, saillants, perturbations identifiés
- Perturbations territoriales codées avec le bon mécanisme (`choc_heterogeneite` pour expansion, `correction_echelle` pour contraction) et un titre spécifique (nom de l'événement, pas le label du mécanisme)
- Flag `territorial: false` sur les perturbations non territoriales
- Champs normalisés (type, start, end, title, summary, description, figure, confidence)
- Résumés (summary) en 1-2 phrases, descriptions (description) en 3-6 phrases construites — pas de style télégraphique

Ce fichier est le **résultat final** : il ne contient que l'hypothèse retenue, pas les débats.

---

## Étape 9 : Produire le fichier `justification.md`

Créer `references/nations/<nation>/justification.md` qui documente :

1. **Hésitations** — pour chaque saillant à confiance non-high, expliquer les alternatives envisagées et la raison du choix
2. **Hypothèses écartées** — scénarios alternatifs avec arguments pour/contre (machlokot)
3. **Questions ouvertes** — ce qui reste à confirmer
4. **Comparaisons** — parallèles avec parcours connus qui éclairent ou nuancent
5. **Apports d'Agent 2** — faits supplémentaires découverts par recherche complémentaire qui ont conduit à des choix particuliers

Le fichier de justification est **séparé** du parcours : le parcours est le résultat, la justification est le raisonnement.

---

## Étape 10 : Discuter et itérer

L'historionomie est une discipline en cours de construction. L'utilisateur peut contester une identification, proposer un saillant alternatif, ou demander d'explorer une hypothèse. Être prêt à réviser l'analyse sur la base d'arguments solides, et à mettre à jour le parcours ET la justification.
