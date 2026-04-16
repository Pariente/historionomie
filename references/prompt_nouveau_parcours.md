# Prompt canonique de lancement — nouveau Parcours national

Ce fichier contient le prompt standard à utiliser pour lancer l'analyse historionomique d'un nouveau parcours national. Le prompt est conçu pour forcer la lecture de la méthodologie consolidée, rappeler les règles subtiles qui ne sont pas évidentes à la première lecture, et encourager l'honnêteté épistémique.

**Usage** : copier-coller le bloc ci-dessous et remplacer `[NATION]` par le nom de la nation à analyser.

---

## Prompt

```
Produis une proposition de Parcours de construction nationale pour [NATION].

**Préparation obligatoire (avant toute recherche historique)** :
1. Lis `references/parcours.md` (cadre théorique général, tableau des bornes de sous-phases). Pour chaque phase analysée, consulter aussi le fichier `phase_*.md` correspondant.
2. Revois les feedback memories chargées automatiquement (naming canonique, catégorisation des événements, bornes de sous-phases, trois pièges, vérification par phase).
3. Si la nation a un statut particulier (empire multi-national, nation tardivement unifiée, cas de reboot, interférence avec un Parcours voisin), lis aussi au moins deux parcours analogues dans `references/nations/` pour avoir des points de comparaison.

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
  - **Essor oligarchique → polarisation des élites** : basculement de dynamique, pas un saillant. La sous-phase se termine quand la dynamique principale cesse d'être la projection vers l'extérieur et devient la tension entre factions (prébendière vs patrimoniale) pour le contrôle de l'État central.
  - **Absolutisation → impérialisme absolutiste** : borne = fin de la DGRO (consensus absolutiste établi), pas le acmé absolutiste (qui est interne à l'impérialisme absolutiste).
  - **Impérialisme absolutiste → ancien régime** : borne = Remontrance stricte, pas « fin de l'expansion » qui peut coïncider ou précéder.

- **Pacte oligarchique = nécessité structurelle** entre la coagulation/bascule et l'essor oligarchique. Il est généralement très formel (loi salique, Ordonnances, primogéniture, Libell, chartes négociées avec les états dans un contexte de souverain affaibli). Ne jamais conclure « absent, résolution diffuse » sans justification structurelle solide appuyée sur un cas comparable du corpus (ex. : Venise où le pacte est institutionnel et non personnel).

- **Distinction saillant / sous-phase** :
  - `ancien régime` et `révolution initiale` sont des sous-phases **seulement**
  - `Restauration` est à la fois un saillant (le moment) et une sous-phase (la durée)
  - `Émergence de l'IR` est un saillant (avènement de la figure autoritaire) ; `impérialisme revanchard` est la sous-phase (durée)
  - `Éclatement de l'AR`, `Expérience parlementaire`, `Phase aiguë`, `Moment thermidorien` sont les 4 saillants internes à la sous-phase `révolution initiale`

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
