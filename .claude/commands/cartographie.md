Cartographie complète du Parcours de construction nationale de : **$ARGUMENTS**

Charge `references/methode_cartographie.md` et exécute la procédure complète :

1. **Étape 1** — Lis le cadre théorique (`references/parcours.md`, et tout `phase_*.md` pertinent si la nation a des particularités identifiables d'emblée).
2. **Étape 2** — Spawner Agent 1 (Collecteur) pour produire le dossier historique brut.
3. **Étape 3** — Spawner Agent 2 (Évaluateur) pour produire le scoring tranche × phase.
4. **Étape 4** — Synthèse par fourches d'ambiguïté (identifier les éléments interprétatifs les plus ambigus, construire les scénarios par combinaison de leurs lectures plausibles).
5. **Étape 5** — Vérification de cohérence interne (saillants + marqueurs + test événement par événement).
6. **Étape 6** — Comparaison tardive avec le corpus.
7. **Étape 7** — Scoring final et scénario retenu.
8. **Étape 8** — Produire `references/nations/<slug>/parcours.md` (avec `<slug>` dérivé du nom de la nation : minuscules, sans accents, sans espaces). Sélectionner soigneusement les faits marquants (highlights) selon le critère « qu'est-ce qui, dans ce parcours précis, est intéressant historionomiquement ? ».
9. **Étape 9** — Produire `references/nations/<slug>/justification.md`. Section « Questions ouvertes » réservée aux incertitudes finales réelles, pas une liste à remplir.
10. **Étape 10** — Récupérer **deux types d'images uniquement** : drapeau SVG (téléchargé localement dans `images/<slug>/flag.svg`) et une illustration par highlight (URL Wikimedia, pas de téléchargement). Pour les illustrations, utiliser l'API MediaWiki `pageimages` (`action=query&prop=pageimages&pithumbsize=240`) qui retourne directement une URL de thumbnail à partir du titre d'un article Wikipedia — pas besoin de chercher des noms de fichiers ni de vérifier des URLs après. Pas d'image de popup dédiée ni de portraits de figures-clefs : réutiliser l'URL d'un highlight emblématique pour le champ `image` du popup carte. Régénérer le HTML, puis ajouter un objet JS dans le tableau `nations` de `docs/index.html` (`name`, `lat`/`lng`, `dates`, `href`, `desc`, `flag`, `image`, `badge:{cls,label}`, `offset` optionnel ; valeurs canoniques de `badge` : `complete`/`Complet`, `draft`/`À valider`, `draft`/`Proposition`, `debate`/`Débat`).
11. **Étape 11** — Itérer en dialogue avec moi.

Avant de commencer, confirme :
- Ta compréhension du nom de la nation et du slug que tu vas utiliser pour les fichiers
- Le périmètre temporel et géographique que tu vas étudier (utile en cas d'ambiguïté : « Allemagne » avant 1871 ? « Israël » antique ou moderne ? etc.)

Puis enchaîne les étapes en m'informant à chaque transition.
