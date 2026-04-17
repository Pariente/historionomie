# Prompt canonique de lancement — nouveau Parcours national

Ce fichier contient le prompt standard à utiliser pour lancer l'analyse historionomique d'un nouveau parcours national. Le prompt est conçu pour forcer la lecture de la méthodologie consolidée, rappeler les règles subtiles qui ne sont pas évidentes à la première lecture, et encourager l'honnêteté épistémique.

**Usage** : copier-coller le bloc ci-dessous et remplacer `[NATION]` par le nom de la nation à analyser.

---

## Prompt

```
Produis une proposition de Parcours de construction nationale pour [NATION].

**Préparation obligatoire (avant toute recherche historique)** :
1. Lis `references/parcours.md` (cadre théorique général, question fondamentale des « égaux », tableau des bornes de sous-phases). Pour chaque phase analysée, consulter aussi le fichier `phase_*.md` correspondant.
2. Lis `references/elites.md` (matrice 2×2, losange politique de Deblonde, formes du clivage factionnel, mécanismes d'absolutisation) et `references/perturbations.md` (mécanismes × effets, empire intégré vs union personnelle, correction_echelle vs choc_exogene fin d'exutoire).
3. Revois les feedback memories chargées automatiquement (naming canonique, catégorisation des événements, bornes de sous-phases, trois pièges, vérification par phase, critère formel du pacte, guerre sociale enjeu/forme).
4. Si la nation a un statut particulier (empire multi-national, nation tardivement unifiée, cas de reboot, interférence avec un Parcours voisin), lis aussi au moins deux parcours analogues dans `references/nations/` pour avoir des points de comparaison.

**Règles strictes de l'analyse** :

- **Priorité absolue : fiabilité des dates de bornes de phase** (usage principal : régression quantitative d'Alyocha Coencas sur les durées). Ne jamais forcer une borne pour obtenir une durée typique — les écarts atypiques sont des signaux de perturbation à identifier, pas des erreurs d'identification.

- **Naming strictement canonique** :
  - Phases, sous-phases et saillants uniquement dans les listes fermées de CLAUDE.md. Aucune dérivation hors `ancien régime exogène` ou `nouveau PO`, et uniquement si un précédent documenté l'exige.
  - Jamais de saillant ad hoc avec un nom inventé pour un événement historique important (ex. : « Victoire de la Contre-Réforme », « Compromis austro-hongrois », « Privilegium Minus » sont des mentions en description de sous-phase, pas des saillants).
  - Figures historiques : nom seul, sans épithètes décoratives ajoutées par goût littéraire (« le Glorieux », « le Fondateur », « le Belliqueux »). Surnoms uniquement s'ils sont historiographiques canoniques et nécessaires à la désambiguïsation.

- **Catégorisation à 4 niveaux** pour chaque événement historique mentionné dans l'analyse :
  1. **Saillant canonique** (liste fermée) → rond de la couleur de la phase
  2. **Perturbation** — passe le triple test : mécanisme identifiable + effet identifiable + impact réel sur la trajectoire (durée, niveau ou direction de la phase aurait été différente) → losange coloré
  3. **Anecdote de parcours** (faible intensité, sans impact) → non marquée, au plus mentionnée en description
  4. **Élément nouveau théorique** (structurellement important mais hors catégorie) → à remonter explicitement pour discussion

  Pas de plafond numérique sur les perturbations — le compte est un résultat du triple test, pas une contrainte.

- **DGRO en fin de phase oligarchique / pendant la sous-phase absolutisation**, jamais au début de la phase oligarchique. Le mot « dernière » a un sens structurel : c'est le dernier sursaut oligarchique avant l'ancrage absolutiste, pas une résistance au pacte fondateur.

- **Trois pièges de bornes de sous-phases** (cf. tableau des bornes dans `parcours.md` et `feedback_bornes_sous_phases_pieges.md`) :
  - **Essor oligarchique → polarisation des élites** : basculement de dynamique, pas un saillant. La sous-phase se termine quand la dynamique principale cesse d'être la projection vers l'extérieur et devient la tension entre factions pour le contrôle de l'État central.
  - **Absolutisation → impérialisme absolutiste** : borne = fin de la DGRO (consensus absolutiste établi), pas l'acmé absolutiste (qui est interne à l'impérialisme absolutiste).
  - **Impérialisme absolutiste → ancien régime** : borne = Remontrance stricte, pas « fin de l'expansion » qui peut coïncider ou précéder.

- **Pacte oligarchique = nécessité structurelle** entre la coagulation/bascule et l'essor oligarchique. Critère formel strict (Coencas) : **première codification négociée et entérinée des responsabilités du suzerain** — acte écrit, collectif, issu d'une assemblée des oligarques (diète, états, Landtag, Cortès). Distingue le pacte des créations institutionnelles unilatérales (Philippe le Bel crée le Parlement de Paris et la Chambre des comptes, mais unilatéralement — le vrai pacte français est la loi salique de 1317 ; Omri crée l'État israélite unilatéralement, d'où l'absence de pacte canonique identifié). Vérifié sur 11/12 parcours du corpus. Ne jamais conclure « absent, résolution diffuse » sans justification structurelle solide appuyée sur un cas comparable (ex. : Venise, pacte institutionnel et non personnel).

- **Guerre sociale — enjeu universel, formes variables** (cf. `elites.md`, `phase_oligarchique.md`) :
  - **Enjeu structurel invariant** : contrôle de l'État central pour l'accès aux prébendes. Ce n'est jamais un conflit confessionnel, régional ou dynastique en soi — la religion, la région, la dynastie sont des **modes d'expression** du clivage.
  - **Forme variable** : économique pure (prébendier vs patrimonial au sens weberien strict — Lancaster/York, giovani/vecchi), géographique (deux blocs majoritairement patrimoniaux polarisés sur la fracture cœur/marges — France Guerres de Religion), ou mixte (le plus fréquent — Espagne). Ne pas forcer la lecture prébendier/patrimonial quand les deux factions sont du même type.
  - **Critère de résolution** : (1) l'enjeu doit être le contrôle des prébendes centrales, (2) la résolution doit produire un nouveau cadre central qui subordonne les oligarques. Si une faction gagne sans nouveau cadre, la guerre sociale n'est pas résolue et la phase oligarchique se poursuit.

- **Acmé oligarchique = saturation de l'exutoire externe**, pas position fixe dans la phase. La fraction de la phase où il se situe varie de 0.13 (Suisse) à 0.71 (Autriche, Léopold Ier). Exutoire court → acmé précoce ; exutoire long → acmé tardif. Ne pas chercher l'acmé à une fraction fixe.

- **Perturbations territoriales — distinction fine** (cf. `perturbations.md`) :
  - **Empire intégré vs union personnelle** : un choc d'hétérogénéité n'opère que si l'acquisition mobilise effectivement les élites du noyau dans un travail de digestion des marges (administration directe, droit imposé, personnel issu du noyau). L'union personnelle ne produit pas de choc structurel — au plus une soupape militaire. Conséquence : le choc d'hétérogénéité se date au moment de l'intégration administrative, pas de l'acquisition dynastique (Bohême autrichienne : 1627, pas 1526).
  - **Correction d'échelle vs fin d'exutoire militaire** : une perte territoriale n'est `correction_echelle` que si le territoire a été **digéré** (administration directe, personnel du noyau) — Crète vénitienne 1669, Silésie autrichienne 1742, empire colonial espagnol 1808-1826. Une perte de territoire en union personnelle (ou d'une possession récemment acquise et non digérée) est `choc_exogene / acceleration` — Normandie 1204, Castillon 1453, Solferino 1859, Sadowa 1866. Les deux produisent une accélération, mais par des mécanismes distincts.

- **Échelle du test discriminant absolutiste = territoire national du Parcours** (noyau + marges), pas toutes les possessions de la couronne. Une marge qui a son propre Parcours (Hongrie pour l'Autriche) ne compte pas ; une marge intégrée (Aragon pour l'Espagne) compte. Piège classique : identifier les Rois Catholiques comme 1er monarque absolu espagnol alors que l'Aragon conserve ses fueros jusqu'à la Nueva Planta — c'est Philippe V (1714) le vrai 1er monarque absolu, les Rois Catholiques sont l'acmé oligarchique.

- **Piège de la codification écrite** : la codification n'est **pas** un test discriminant absolutiste. L'Angleterre n'a jamais codifié son droit (common law) et est canoniquement absolutisée depuis Henri VII. Le test porte sur la substance (préséance de jure de l'administration centrale), pas la forme (code écrit / coutume).

- **Distinction saillant / sous-phase** :
  - `ancien régime` et `révolution initiale` sont des sous-phases **seulement**
  - `Restauration` est à la fois un saillant (le moment) et une sous-phase (la durée)
  - `Émergence de l'IR` est un saillant (avènement de la figure autoritaire) ; `impérialisme revanchard` est la sous-phase (durée)
  - `Éclatement de l'AR`, `Expérience parlementaire`, `Phase aiguë`, `Moment thermidorien` sont les 4 saillants internes à la sous-phase `révolution initiale`

- **Cas particuliers de la RN** (cf. `phase_rn.md`) — à connaître pour ne pas forcer une séquence canonique là où elle ne s'applique pas :
  - **RN avortée** : écrasement par puissance extérieure avant le thermidorien (Israël 70, Venise 1849). Coder comme `choc_exogene / avortement`.
  - **RN contre occupant** : la RN peut éclater contre un occupant étranger si l'homogénéité culturelle du peuple est suffisante (Venise 1848, Milan napoléonien). Deux configurations : AR propre (Sanhédrin sous Rome) ou **AR exogène** (Venise sous l'Autriche) — dérivation canonique documentée.
  - **IR double** : hypothèse structurelle nouvelle (Hitler pour Allemagne ET Autriche simultanément). À signaler explicitement si un cas comparable émerge.
  - **Test discriminant RN avortée vs révolte absolutiste** : une RN commence par une expérience parlementaire avec assemblée élue et factions concurrentes (leadership **construit par l'élection**) ; une révolte absolutiste est portée par un chef à autorité **héritée ou charismatique** (Maccabées, Bar Kokhba).

**Workflow obligatoire** :

1. **Lecture des références méthodologiques** (voir préparation ci-dessus).
2. **Recherche historique** : identifier les grands événements de l'histoire de la nation, en partant du 1er monarque oligarchique si possible, puis remonter et descendre.
3. **Analyse phase par phase** avec **vérification obligatoire après chaque phase** avant de passer à la suivante :
   - Tous les saillants canoniques attendus sont-ils présents ?
   - Si un manque, est-ce mal lu ou structurellement atypique (à justifier comparativement) ?
   - Les durées sont-elles cohérentes (ou écart expliqué par une perturbation identifiée) ?
   - Le test discriminant est-il passé à la bonne échelle (territoire national du Parcours = noyau + marges, pas l'ensemble des possessions de la couronne) ?
   - Les bornes des sous-phases sont-elles correctement identifiées (attention aux 3 pièges) ?
4. **Vérification globale finale** après la dernière phase : lister tous les événements majeurs documentés de l'histoire de la nation et vérifier qu'aucun ne reste inexpliqué historionomiquement. Chaque événement doit être soit un saillant canonique, soit une perturbation, soit une anecdote à mentionner en description, soit un élément nouveau théorique à signaler.
5. **Production des livrables** (voir ci-dessous).

**Livrables attendus** :

1. **`references/nations/[nation]/parcours.md`** : hypothèse structurée selon le format des parcours existants. Métadonnées (nation, territoire, dates, status, subtitle, confidence, highlights), superficie de référence noyau+marges, phases/sous-phases/saillants/perturbations avec champs normalisés (type, phase, start, end, title, summary, description, figure, confidence, alternatives, mechanism, effect, territorial).

2. **`references/nations/[nation]/justification.md`** : raisonnement détaillé, alternatives écartées (comme les *machlokot* du Talmud), points fragiles avec leur confidence explicite, comparaisons structurelles avec au moins deux parcours analogues du corpus.

3. **HTML généré** via `python3 generate_timeline.py references/nations/[nation]/parcours.md -o docs/[nation].html`

4. **Synthèse courte en fin de réponse** : 4-6 points les plus fragiles à discuter, formulés comme questions ouvertes à trancher.

**Honnêteté épistémique (règle cardinale)** :

- Préfère un parcours avec des trous honnêtes à un parcours faussement complet.
- Si un saillant canonique semble absent, justifie structurellement en comparant à un cas du corpus — ne pas forcer une identification par confort narratif.
- Si un événement ne rentre dans aucune des 4 catégories, signale-le comme élément nouveau théorique plutôt que de bricoler.
- Signale explicitement les désaccords avec la méthodologie qui pourraient émerger de l'analyse — c'est potentiellement une découverte, pas un échec.
- `confidence: medium` ou `low` justifié vaut mieux que `confidence: high` forcé.
```

---

## Notes d'usage

- **Remplacer `[NATION]`** par le nom de la nation (ex. : « l'Autriche », « la Russie », « le Japon »).
- **Durée attendue** : une analyse complète prend typiquement 30-60 minutes, entre les recherches web, l'analyse phase par phase, les vérifications et la rédaction des livrables.
- **Si l'utilisateur veut une première passe rapide** plutôt qu'un parcours complet, remplacer la partie livrables par « Synthèse argumentée des grandes lignes, avec saillants identifiés, durées estimées, et points à approfondir » — mais le naming canonique et la catégorisation à 4 niveaux restent obligatoires.
- **Ce prompt n'est pas exhaustif** — il rappelle les règles les plus subtiles et les plus souvent mal appliquées. Les règles générales (les deux moteurs, le test discriminant, les durées typiques) sont supposées être lues dans `references/parcours.md` dès la phase de préparation.

## Historique

- **v1 (2026-04-14)** : première version du prompt canonique.
- **v2 (2026-04-17)** : alignement avec la refonte méthodologique (renommages acmé/éclatement/émergence, 2 critères guerre sociale, territoire national du Parcours, suppression sous_phases.md).
- **v3 (2026-04-18)** : ajouts méthodologiques — critère formel du pacte oligarchique (Coencas), guerre sociale enjeu/forme (économique pure / géographique / mixte), acmé oligarchique = saturation exutoire, empire intégré vs union personnelle, correction_echelle vs choc_exogene fin d'exutoire, échelle du test absolutiste, piège de la codification écrite, cas particuliers RN (avortée, contre occupant, AR exogène, IR double, test RN vs révolte absolutiste).
