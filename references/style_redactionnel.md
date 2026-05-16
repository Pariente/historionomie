# Style rédactionnel des Parcours

Ce fichier capture les conventions de style pour la rédaction des fichiers `parcours.md` des nations. **À lire avant la rédaction finale** (étape de synthèse parent dans `methode_cartographie.md`) et **à appliquer en relecture** avant de présenter un parcours fini.

Les règles ici complètent — sans les répéter — celles de `CLAUDE.md` (naming canonique, catégorisation des événements, anti-patterns universels) et `perturbations.md` (cadre théorique).

---

## 1. Titres

### Saillants canoniques

Le titre est exactement le vocabulaire canonique fermé de `CLAUDE.md` : `Pic féodal`, `Crise féodale`, `Pacte oligarchique`, `1er monarque oligarchique`, `Acmé oligarchique`, `Guerre sociale`, `1er monarque absolu`, `Acmé absolutiste`, `Réformes échouées`, `Éclatement de l'AR`, `Expérience parlementaire`, `Phase aiguë`, `Moment thermidorien`, `Émergence de l'IR`, `Restauration`, `Glorieuse Révolution`, etc.

**Pas de variante**, pas d'ajout, pas de qualifiant. La désambiguïsation entre plusieurs occurrences (deux pics féodaux, trois RN avortées) se fait au niveau du **subtitle**, pas du titre.

### Saillants ad-hoc et perturbations

Le titre est un **nom historique sec** ou un **label événementiel concret** :

✓ Bons : `Quattro Vicari`, `Conjuration de Squarcialupo`, `Terre Nuove`, `Croisade des Albigeois`, `Traité de Troyes`, `Effondrement des institutions`, `Expulsion des juifs`, `Empire de Cnut`.

✗ Mauvais : `Étouffement aragonais 1392`, `Bouclage avorté 1377`, `Crise dynastique post-Frédéric IV`, `Premier cycle factionnel raté`. Trop analytiques, trop narratifs, ou trop datés.

---

## 2. Subtitles

### Format attendu

- **Court** : 3 à 6 mots
- **Event-focused** : nomme la conséquence concrète, l'agent clé, ou le moment décisif — pas la lecture analytique
- **Pas de date redondante** avec le champ `start` (la date est déjà affichée sur la frise)
- **Pas de label analytique** type `Bouclage avorté — clivage X/Y`

### Exemples comparatifs (corpus)

| Saillant | ✗ À éviter | ✓ À privilégier |
|---|---|---|
| Pic féodal — Frédéric II | « Frédéric II Hohenstaufen 1198-1250 » | « Stupor Mundi » |
| Crise féodale (Sicile 1250) | « Effondrement de la dynastie Hohenstaufen 1250-1268 » | « Bénévent et captation angevine » |
| Pacte oligarchique (France) | « Loi salique 1317 sous Philippe V » | « Loi salique » |
| Quattro Vicari | « Bouclage avorté — clivage latine/catalane » | « Liquidation de la faction latine » |
| Phase aiguë (Sicile 1848) | « Bombardement de Messine 1848 » | « Re Bomba » |
| Acmé absolutiste (Sicile) | « Charles de Bourbon — Caserta entamée 1752 » | « Charles de Bourbon » |
| Éclatement de l'AR (Sicile 1812) | « Constitution sicilienne (Westminster) 1812 » | « Westminster » |
| Expérience parlementaire (1812) | « Parlement bicaméral 1812-1816 » | « Parlement bicaméral » |
| Éclatement de l'AR (Sicile 1820) | « Soulèvement de Palerme — 15 juillet 1820 » | « Soulèvement de Palerme » |

### Pattern récurrent : « Liquidation de la faction X »

Pour les perturbations qui marquent l'écrasement d'une faction insurgée par intervention extérieure, le subtitle nomme **la faction liquidée**, pas le mécanisme. Ex. « Liquidation de la faction latine », « Liquidation de la faction indigène ».

---

## 3. Summary

### Format attendu

- 1 à 3 phrases denses (~30-80 mots)
- Donne **les acteurs nommés** (figures, institutions, événements concrets)
- Donne **les dates clés** (l'événement central, parfois ses bornes)
- Donne **les faits chiffrés notables** (nombre de morts, taille de l'armée, ans de durée — quand c'est structurellement parlant)
- Énonce **la lecture historionomique** : test discriminant satisfait/non, mécanisme retenu, position vis-à-vis des alternatives écartées
- Direct, factuel, pas de méta-commentaire

### Anti-patterns

- Summary qui se contente de répéter `titre + start-end`
- Summary sans aucun nom d'acteur ni date précise
- Summary qui ne dit pas **pourquoi** cette lecture est retenue (test, mécanisme, comparaison)
- Summary purement narratif sans ancrage historionomique

---

## 4. Description

### Format attendu

- Multi-paragraphe quand pertinent (1 à 3 paragraphes)
- **Chronologie détaillée** avec noms et dates explicites
- **Acteurs nommés** : figures historiques précises (Andrea Chiaramonte, pas « les barons rebelles »), institutions (Sénat de Messine, parlement à trois bras, Magna Curia), événements datés (bataille de Bénévent 26 février 1266)
- **Lecture historionomique explicite** : test discriminant appliqué, mécanisme structurel, articulation avec les deux moteurs
- **Conséquences structurelles** : ce que change cet événement pour la suite du Parcours
- **Alternatives écartées** quand pertinent : pourquoi pas X, pourquoi pas Y
- **Comparaisons cross-corpus** quand elles éclairent (parallèle avec France, Angleterre, Florence, etc.)

### Anti-pattern principal

Description qui **paraphrase le summary en plus long** sans ajouter de détails. La description doit *ajouter* — chronologie, acteurs, raisonnement, comparaisons — pas reformuler.

### Test pratique

Si on retire la description, le summary devrait perdre des **faits**, pas seulement de la longueur.

---

## 5. Highlights (faits marquants)

### Format

```
- highlight_N: Titre incisif | Description | URL_image | phase_tag
```

### Règles

- **Nombre** : 3 à 5, idéalement 4
- **Longueur description** : 50-70 mots (jamais > 80)
- **Markdown bold supporté** : `**texte**` → **texte** en gras (rendu HTML par `generate_timeline.py`). Aucun autre markdown (italic, code, headers, listes).
- **Image** : URL Wikimedia Commons préférée, format `https://commons.wikimedia.org/wiki/Special:FilePath/Nom_de_fichier.jpg?width=120`
- **Phase tag** : `feodale`, `oligarchique`, `absolutiste`, `rn`, `parlementaire`

### Structure de la description

1. **Fait clé daté** (1ère phrase)
2. **Mécanisme historionomique** (2-3 phrases)
3. **Conséquence structurelle** (phrase finale)

### Bold stratégique

Réservé aux **concepts structurants** (« exutoire intérieur », « parlement à trois bras »), aux **dates ancrantes** (« **1391-1392** : Martin le Jeune... »), et aux **faits chiffrés saillants** (« sans interruption pendant **520 ans** »). Pas plus de 5-7 emphases par highlight.

### Anti-patterns

- Listes de chiffres comparatifs détaillés → vont dans la description du saillant correspondant, pas dans le highlight
- Description > 80 mots
- Markdown autre que bold (italic `*…*`, code `\`…\``, etc.) — non rendu
- Bold sur des passages > 6 mots (l'emphase perd sa valeur)
- Bold sur tout (l'emphase perd sa valeur aussi)

---

## 6. Conventions visuelles

### Icônes des perturbations (effet-based)

Cf. `perturbations.md` §1. La convention actuelle map l'icône à **l'effet**, pas au mécanisme :

| Effet | Couleur | Icône Material |
|---|---|---|
| Prolongement | 🟠 orange | `open_in_full` |
| Accélération | 🔵 bleu | `fast_forward` |
| Avortement | 🔴 rouge | `block` |
| Reboot | 🟤 cramoisi | `restart_alt` |

Le mécanisme reste lisible dans le tooltip et la description du saillant — pas besoin de l'encoder dans l'icône.

### Métadonnées des perturbations

Toujours renseigner les quatre champs : `perturbation: true`, `mechanism`, `effect`, `territorial` (true/false).

---

## 7. Anti-patterns spécifiques observés

Au-delà des anti-patterns universels de `CLAUDE.md` (noms vs fonction, singularités comme features, forcer une identification), les pièges récurrents de la rédaction :

1. **Subtitle redondant avec start** — la date apparaît déjà sur la frise, ne la répète pas dans le subtitle.
2. **Subtitle analytique** — préfère l'événement concret au label structurel.
3. **Summary descriptif sans ancrage HN** — toujours articuler avec un test, un mécanisme, une lecture.
4. **Description qui paraphrase** — ajoute des faits, pas de la longueur.
5. **Highlight surchargé de chiffres** — l'effet structurel suffit, les chiffres détaillés vont dans le saillant.
6. **Markdown qui ne rend pas** — actuellement seul `**bold**` est supporté dans les highlights.
7. **Tableau récapitulatif désaligné** — chaque ligne doit pointer un saillant canonique exact (avec valeur ou « — » + raison structurelle si absent).

---

## 8. Checklist de relecture finale

À passer avant de présenter un parcours fini :

### Naming et structure
- [ ] Tous les titres canoniques figurent dans la liste fermée (`CLAUDE.md`)
- [ ] Tous les titres de saillants ad-hoc / perturbations sont des noms historiques secs
- [ ] Aucun épithète ajouté par goût littéraire
- [ ] Toutes les sous-phases utilisent les noms canoniques de la liste fermée

### Subtitles
- [ ] Tous les subtitles sont event-focused (≤ 6 mots, nomment l'événement/agent/conséquence)
- [ ] Aucune date redondante avec `start` dans un subtitle
- [ ] Aucun label analytique de type « Bouclage avorté — clivage X »

### Summaries et descriptions
- [ ] Tous les summaries des saillants importants contiennent : nom d'acteur + date précise + lecture historionomique
- [ ] Toutes les descriptions développées **ajoutent** au summary (chronologie, acteurs, raisonnement, comparaisons)
- [ ] Aucune description n'est une simple paraphrase étendue

### Highlights
- [ ] 3 à 5 highlights, idéalement 4
- [ ] Chacun ≤ 70 mots
- [ ] Bold stratégique uniquement (concepts clés, dates, faits chiffrés)
- [ ] Aucun markdown autre que `**bold**`
- [ ] Phase tag valide (`feodale`/`oligarchique`/`absolutiste`/`rn`/`parlementaire`)
- [ ] Image URL valide

### Visuel et perturbations
- [ ] Conventions d'icônes effet-based respectées (cf. `perturbations.md` §1)
- [ ] Toutes les perturbations ont `mechanism` + `effect` + `territorial`
- [ ] Tableau récapitulatif final aligne chaque saillant canonique avec un cas concret ou une absence justifiée

### Cohérence transversale
- [ ] Le subtitle des metadata correspond à la lecture finale du Parcours
- [ ] Les highlights ne contredisent pas les saillants/sous-phases du corps
- [ ] Le tableau récapitulatif final reflète l'état actuel du parcours, pas une version antérieure
