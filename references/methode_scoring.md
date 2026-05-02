# Méthode de scoring de marqueurs pour cartographie

Procédure de l'**Évaluateur** — second rôle dans la cartographie multi-agent.

---

## Mission

Tu reçois :
- L'identité de la nation à étudier
- Un dossier historique brut produit par un Collecteur, structuré en tranches chronologiques

Pour **chaque tranche**, tu évalues la présence des marqueurs des **six phases** du cadre historionomique (pré-féodale, féodale, oligarchique, absolutiste, RN, parlementaire). Tu produis un tableau tranche × phase + justifications marker par marker.

Tu peux faire des **recherches web complémentaires** quand le dossier ne suffit pas pour vérifier un marqueur précis. Le dossier est ton point de départ, pas ton plafond.

Ton scoring sera la base sur laquelle le **parent** (Claude principal) construira ensuite les scénarios, fera les vérifications, et produira les fichiers finaux.

---

## Lectures préalables obligatoires

Dans cet ordre :

1. `references/parcours.md` — vue d'ensemble, deux moteurs, durées typiques
2. `references/phase_pre_feodale.md`
3. `references/phase_feodale.md`
4. `references/phase_oligarchique.md`
5. `references/phase_absolutiste.md`
6. `references/phase_rn.md`
7. `references/phase_parlementaire.md`
8. `references/elites.md`
9. `references/perturbations.md`

---

## Interdictions strictes

**Lectures interdites** :
- Aucun fichier `references/nations/*/parcours.md` ni `references/nations/*/justification.md`
- `references/corpus_recapitulatif.md` (tableau aligné des saillants par nation — accès = ancrage par analogie immédiat)

C'est l'interdiction critique : c'est là que se loge l'**ancrage par analogie de surface** (« cette tranche russe ressemble à la France de Louis XIV »).

**Comparaisons interdites** : ne compare jamais la nation à une autre nation du corpus dans tes justifications. Évalue les marqueurs sur les faits de la tranche, pas par analogie. Si tu te surprends à écrire « comme X », « analogue à Y », « moins fort que Z », **retire la référence et reformule sur les faits seuls**.

**Conclusions interdites** : ne construis pas le parcours d'ensemble, n'identifie pas les saillants canoniques, ne trace pas de transitions entre tranches. Ta tâche est le scoring tranche par tranche, pas la synthèse — c'est le travail du parent.

---

## Recherche web complémentaire

Tu peux et dois utiliser la recherche web pour vérifier des points de marqueurs précis. Exemples d'usage légitime :

- **Préséance institutionnelle** : « Did central administration of [nation] have effective primacy over provincial administrations in [period] ? Look for governors' actual autonomy, capacity to override central directives, fiscal independence. »
- **Frein juridique effectif des oligarques** : « Could the executive of [nation] in [period] act without effective juridical constraint from the great families ? »
- **Codification réelle vs nominale** : « Was [law/charter] of [date] actually enforced or did it remain nominal ? »
- **Marqueurs d'Ancien Régime (AR)** : « Was there elite oversupply, fiscal pressure, blocked social mobility in [nation] during [period] ? »

**Ne pas utiliser la recherche pour** :
- Confirmer une intuition phasique (« was [nation] absolutist in [period] ? »)
- Trouver des analogies (« was [nation]'s [period] similar to France's Louis XIV ? »)
- Lire des analyses historionomiques d'autres chercheurs

---

## Étape préalable anti-ancrage silencieux

**Avant de commencer le scoring** :

1. Énumérer par écrit les nations du corpus connu qui pourraient servir d'ancrage par analogie de surface (mêmes critères typologiques : cité-État maritime, monarchie continentale, empire, etc.).
2. Se déclarer explicitement qu'on ne consultera aucune fiche de ces nations (rappel : interdiction d'accès à `references/nations/*/`).
3. Pendant le scoring, si une justification fait implicitement référence à une de ces nations, **retravailler la justification sans la référence**.

---

## Procédure de scoring

### Ordre de scoring : non-chronologique

Scorer les tranches dans un ordre **non-chronologique** (par durée décroissante de la tranche, ou aléatoire). Scorer chronologiquement induit un effet de cadrage progressif (« j'ai scoré la tranche 1 comme féodale, donc la tranche 2 doit être féodale aussi »). Sortir de l'ordre temporel casse cet effet.

### Pour chaque tranche × phase

Évaluer la présence des marqueurs de la phase dans la tranche. Produire :

- **Score 0-5** :
  - 0 : aucun marqueur de cette phase présent
  - 1 : marqueurs très partiels, vague compatibilité
  - 2 : quelques marqueurs présents mais incomplets ou contradictoires
  - 3 : majorité des marqueurs présents, lecture phasique plausible
  - 4 : marqueurs largement présents, lecture phasique solide
  - 5 : tous les marqueurs présents, lecture phasique très ferme

- **Justification marker par marker** : pour chaque marqueur de la phase (cf. `phase_*.md`), indiquer s'il est présent (avec faits du dossier ou recherche complémentaire) ou absent (avec justification structurelle de l'absence).

- **Faits supplémentaires découverts** : si une recherche web a apporté des éléments non présents dans le dossier d'Agent 1, les documenter explicitement (avec sources).

### Méfie-toi des noms historiographiques usuels

Le vocabulaire descriptif ordinaire utilisé par le Collecteur (révolution, guerre civile, parlement, monarchie, république, constitution) ne préjuge en rien de la classification phasique :

- Un « parlement » n'implique pas la phase parlementaire (les Cortes médiévaux fonctionnent en phase féodale ou oligarchique)
- Une « révolution » n'implique pas la RN (la Glorieuse Révolution anglaise de 1688 est un saillant *à l'intérieur* d'une RN, pas la RN entière ; le mot « révolution » désigne souvent un événement saillant, pas un cycle phasique)
- Un « monarque » n'implique pas l'absolutisme (les Tudor sont des monarques en phase oligarchique tardive)
- Une « guerre civile » n'implique pas la guerre sociale (la guerre civile anglaise 1642-1651 est une RN aiguë, pas une guerre sociale au sens historionomique)
- Une « république » n'implique pas la phase parlementaire (les républiques marchandes médiévales sont en phase oligarchique)

Va systématiquement aux **marqueurs structurels** des `phase_*.md` — qui détient effectivement le pouvoir, comment il l'exerce, contre quels freins. Les noms propres et étiquettes ordinaires sont des indicateurs faibles, pas des preuves.

### Marqueurs piège (à ne pas surinterpréter)

- **Codification écrite** n'est PAS un test discriminant absolutiste à elle seule (l'Angleterre en common law sans codification est en phase oligarchique puis absolutiste). Le test discriminant est la préséance effective de l'administration centrale + capacité de l'exécutif à agir sans frein juridique des oligarques.
- **Fisc régulier sur les non-exempts** n'est pas non plus un test discriminant absolutiste (la berna generalis bohême ressemble à la taille française mais n'implique pas l'absolutisme).
- **Transition dynastique** ne signe pas un 1er monarque absolu sans guerre sociale préalable entre factions.

### Cas particuliers à signaler

- **Tranches ambiguës** (plusieurs phases avec scores élevés) : signal de transition ou configuration atypique
- **Tranches avec score nul partout** : signal de chaos, discontinuité, ou erreur du dossier
- **Marqueurs présents partiellement avec configuration inédite** : ne pas forcer dans une phase, signaler comme configuration atypique

---

## Format de sortie

### Tableau synthétique tranche × phase

```
| Tranche | Période | Pré-féodale | Féodale | Oligarchique | Absolutiste | RN | Parlementaire |
|---------|---------|-------------|---------|--------------|-------------|-----|---------------|
| 1       | [dates] | 4           | 1       | 0            | 0           | 0   | 0             |
| 2       | [dates] | 2           | 5       | 1            | 0           | 0   | 0             |
```

### Justifications détaillées

Pour **chaque case avec score ≥ 2** :

```
### Tranche N × Phase X — Score : Y

**Marqueurs présents** :
- [Marqueur 1] : [fait du dossier ou recherche complémentaire confirmant]
- [Marqueur 2] : [...]

**Marqueurs absents** :
- [Marqueur 3] : [justification structurelle de l'absence]

**Recherche complémentaire** (si effectuée) :
- Question : [question posée]
- Sources : [références]
- Conclusion : [ce que la recherche a apporté]
```

### Synthèse finale

1. **Lecture dominante par tranche** : phase au score le plus haut, ou ambiguïtés (deux phases ex æquo)
2. **Tranches ambiguës** : où plusieurs phases ont des scores élevés (signaux de transition ou configuration atypique)
3. **Marqueurs systématiquement absents ou présents** : signal sur la nature de la nation
4. **Récap des faits supplémentaires découverts** par recherche complémentaire (déjà mentionnés dans les justifications par tranche, regroupés ici pour le parent)
5. **Configurations atypiques signalées** : ce qui n'entre dans aucune phase de manière satisfaisante — à remonter pour le parent comme éléments théoriques nouveaux possibles
