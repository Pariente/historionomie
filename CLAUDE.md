---
name: historionomie
description: >
  Cadre théorique et boîte à outils pour l'historionomie de Philippe Fabry : analyser le Parcours de construction nationale d'une nation, identifier ses phases (féodale, oligarchique, absolutiste, Révolution Nationale, parlementaire), ses saillants, ses perturbations, et comparer des parcours nationaux entre eux. Utiliser ce skill dès que l'utilisateur mentionne l'historionomie, Philippe Fabry, Antoine Deblonde, le Parcours de construction nationale, ou demande d'analyser l'histoire d'une nation en termes de construction étatique et d'homogénéisation culturelle. Utiliser aussi quand l'utilisateur cherche à identifier des saillants (éveil féodal, premier monarque oligarchique, acmé absolutiste, guerre sociale, Impérialiste Revanchard, Glorieuse Révolution), à comparer des trajectoires nationales, à identifier des perturbations (reboot, prolongement), ou à appliquer la grille du clivage gauche-droite de Fabry & Portal. Ce skill est pertinent même quand l'utilisateur ne mentionne pas explicitement l'historionomie mais pose des questions sur la dynamique de construction nationale d'un pays, les transitions de régime, ou les parallèles structurels entre trajectoires historiques.
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
| `references/phase_pre_feodale.md` | Phase pré-féodale : percolation élitaire (Deblonde), marqueurs, exemples | La question porte sur la percolation ou la pré-féodale |
| `references/phase_feodale.md` | Phase féodale : coagulation, bascule, saillants (éveil féodal, pic féodal, pacte oligarchique), marqueurs | La question porte sur la phase féodale |
| `references/phase_oligarchique.md` | Phase oligarchique : sous-phases (essor, polarisation, guerre sociale), saillants, marqueurs | La question porte sur la phase oligarchique |
| `references/phase_absolutiste.md` | Phase absolutiste : sous-phases (absolutisation, impérialisme, AR), saillants (1er monarque absolu, acmé absolutiste, DGRO), marqueurs | La question porte sur la phase absolutiste |
| `references/phase_rn.md` | Révolution Nationale : sous-phases (révolution initiale, IR, restauration), saillants (éclatement de l'AR, phase aiguë, thermidorien, IR, Glorieuse Révolution), conditions de sortie | La question porte sur la RN |
| `references/phase_parlementaire.md` | Phase parlementaire, technocratique, dominat | La question porte sur les phases post-RN |
| `references/elites.md` | Matrice 2×2 des élites (prébendières/patrimoniales × gouvernementales/non-gouvernementales), mécanismes d'absolutisation, guerre sociale | La question touche à la dynamique des élites |
| `references/perturbations.md` | 3 mécanismes (choc d'hétérogénéité, choc exogène, insuffisance interne) × 4 effets (prolongement, accélération, avortement, reboot) + exutoire (état continu). Rébellion périphérique. Affichage sur la frise (losanges, couleurs, icônes) | La question touche à un choc externe, une déviation des durées typiques, ou un exutoire |
| `references/nations/*/parcours.md` | Parcours nationaux déjà mappés (France, Angleterre, Espagne, Piémont, Milan, Venise, Bavière, Israël, Allemagne, Suisse, Chili, Autriche) — données structurées, hypothèse finale retenue | Pour comparer avec un parcours connu ou générer une infographie |
| `references/nations/*/justification.md` | Justification des choix, hypothèses écartées, questions ouvertes | Pour comprendre le raisonnement derrière le parcours |

## Workflow : analyser le Parcours d'une nation

### Étape 1 : Lire le cadre théorique

Lire `references/parcours.md` pour avoir en tête les phases, les saillants connus, les durées typiques, et les deux moteurs (construction de l'État central + homogénéisation culturelle).

Si la question porte sur une phase ou un mécanisme spécifique, lire aussi le fichier de référence correspondant.

### Étape 2 : Rechercher l'histoire de la nation

Utiliser la recherche web pour rassembler les informations historiques nécessaires — **faits bruts, dates, acteurs, institutions**, sans pré-filtrage par une hypothèse de phase ou de télos. À ce stade, on ne classe rien — on collecte. La classification en phases attend l'Étape 3.

**⚠️ Interdiction de lecture à rebours.** Ne JAMAIS démarrer la recherche depuis un événement final connu (absorption, unification, RN supposée) comme télos. Ce forçage produit systématiquement des cadrages erronés : la fixation implicite sur une date finale transforme le problème en « comment caser les phases dans cette fenêtre » au lieu de « à quel moment les saillants canoniques apparaissent-ils ».

#### Stratégie de recherche web

1. **Commencer large** : chercher « history of [nation] state formation » ou « [nation] medieval centralization » pour identifier les grandes périodes et les figures clés.
2. **Cibler les saillants** : une fois les grandes lignes identifiées, chercher spécifiquement les saillants. Utiliser des requêtes précises : « first permanent army [nation] », « [nation] civil war factions », « [nation] absolute monarchy ».
3. **Chercher des sources académiques** : privilégier les travaux d'historiens (monographies, articles). Wikipédia est un bon point d'entrée mais ne suffit pas — suivre les références citées. Les controverses historiographiques sont souvent révélatrices (cf. débat minimaliste/maximaliste sur Israël).
4. **Remonter depuis le mieux documenté** : la RN et la phase absolutiste sont généralement très bien documentées. Les phases féodale et oligarchique le sont moins. Remonter le fil depuis les événements récents vers les plus anciens.
5. **Attention aux anachronismes** : ne pas projeter les critères d'une phase sur une autre. L'absence de traces archéologiques d'un État central ne réfute pas l'existence d'une société féodale — une société féodale est pauvre et laisse peu de traces (cf. le cas David-Salomon).

#### Checklist de recherche obligatoire (procédure exécutable)

Les listes « à chercher activement » ci-dessous sont des **procédures exécutables, pas des rappels passifs**. Pour chaque nation analysée, lancer une requête web spécifique pour chaque item de la checklist, en remplaçant `[nation]` par le nom. Ne pas se contenter d'extraire autour du hub central le plus connu — chaque item peut révéler un saillant canonique que la narration dominante occulte.

**Requêtes obligatoires pour toute nation :**
- `[nation] popular revolt medieval commoner doge` OU `[nation] plebeian uprising late [phase]`
- `[nation] first permanent army fiscal administration central`
- `[nation] civil war factions [approximate period]`
- `[nation] constitutional reform [century] bicameral lottery sortition`
- `[nation] foreign intervention dynasty imposed [period]`
- `[nation] aristocratic reform noble families closure register`
- `[nation] peasant revolt tax revolt [approximate period]`

**Requêtes supplémentaires pour cités-États :**
- `[nation] rival family dynasties alternance doge lifelong`
- `[nation] private company colonial administration Mahona Banco`
- `[nation] parallel Florence Medici Albizzi faction`

Quand une requête révèle un événement non capturé dans la narration dominante (ex. une révolte populaire courte avec figure roturière), le documenter comme candidat à un saillant canonique et ne pas passer à la suite sans l'avoir exploré.

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
- Qui résout la guerre sociale et concentre le pouvoir ? (1er monarque absolu — tester les deux patterns : tiers populiste neutre ET faction-gagnante qui crée un nouveau cadre, cf. `phase_absolutiste.md`)
- L'administration centrale a-t-elle préséance sur les administrations locales ?
- Y a-t-il un pic d'impérialisme et de prestige ? (acmé absolutiste)
- Y a-t-il sédimentation des élites, sclérose, bloc contestataire ? (Ancien Régime)
- Pour les cités-États : y a-t-il un consortium institutionnalisé de créanciers-actionnaires oligarques qui a progressivement capturé les fonctions d'État (fiscalité, administration territoriale, colonies, coercition), tout en restant propriété collective des élites ? (Absolutisme collectif par consortium — forme 4)

**Événements à chercher activement pour ne pas rater la phase absolutiste :**
- Révolte populaire d'ampleur contre la caste dirigeante (même brève, même écrasée) — peut signaler un début de phase absolutiste par pattern 2 (faction-gagnante)
- Apparition d'une magistrature suprême à vie (ou à longue durée), même si ses titulaires se succèdent rapidement par violence
- Exclusion formelle ou informelle des anciennes élites aristocratiques du pouvoir suprême
- Guerre de projection extérieure soutenue (impérialisme)
- Apparition d'une banque d'État ou d'un office fiscal autonome
- **Pour toute cité-État trop petite à l'époque des États territoriaux : tester activement la forme 4 (absolutisme collectif par consortium oligarchique). Les oligarques se coordonnent collectivement via un consortium institutionnalisé (banco, compagnie, société par actions publique) qui possède l'appareil central sans lutte factionnelle durable pour son contrôle. C'est le pattern attendu, pas une variante rare (cf. `phase_absolutiste.md`, forme 4).**

**Pour identifier la RN :**
- Y a-t-il une éclatement de l'ordre ancien, une expérience parlementaire, une phase aiguë ?
- Y a-t-il une figure d'IR (Impérialiste Revanchard) ?
- Y a-t-il une Glorieuse Révolution qui ancre le parlementarisme ?
- Si la nation est une cité-État ou une nation de taille non-standard : ne pas s'attendre à une RN pleine avec tous les saillants endogènes. Certains saillants (IR endogène, moment thermidorien distinct, Glorieuse Révolution séparée) peuvent être absents ou compressés dans un accord final sous arbitrage extérieur. La RN reste **aboutie** si un nouveau cadre institutionnel stable en émerge (même sous influence étrangère pendant la séquence), **avortée** si l'ordre ancien est restauré à l'identique. La binarité aboutie/avortée ne dépend pas de la présence ou non d'une occupation étrangère (cf. `phase_rn.md`).

**Événements à chercher activement pour ne pas rater la RN :**
- **Révoltes populaires tardives portant une figure roturière au pouvoir, même éphémèrement** — même pour quelques mois, même écrasées par intervention étrangère, ces épisodes peuvent être l'éclatement de l'AR d'une RN. Chercher explicitement dans l'histoire de la nation.
- Conspirations nobiliaires écrasées (signe d'une polarisation dans l'AR tardif)
- Constitutions populaires ou semi-populaires brèves
- Réformes bicamérales avec élargissement significatif du cercle des charges (même si limité à une élite élargie)
- Figure émergeant d'une intervention étrangère pour imposer ou arbitrer un nouveau cadre constitutionnel durable (candidat Glorieuse Révolution compressée / RN aboutie sous arbitrage extérieur)

**Pour identifier les perturbations :**
- Les durées observées s'écartent-elles des ~200 ans typiques ? Si oui, identifier le **mécanisme** (choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire continu) et l'**effet** (prolongement, accélération, avortement, reboot).
- Si choc exogène : les institutions sont-elles détruites (→ reboot) ? Une transition est-elle bloquée (→ avortement) ? Du territoire/exutoire est-il perdu (→ accélération) ? Le Parcours est-il gelé temporairement (→ prolongement) ?
- Y a-t-il un exutoire continu (empire, colonies, expansion) qui prolonge la phase en cours ?
- **La perturbation est-elle territoriale ?** Correspond-elle à un changement de superficie visible ? Si oui, elle doit être reflétée dans les données de superficie ET codée comme saillant avec le bon mécanisme (choc_heterogeneite pour les expansions, correction_echelle pour les contractions). Si la perturbation est culturelle ou institutionnelle sans changement de superficie (ex. : hellénisation d'Israël, occupation napoléonienne de Milan), ajouter `territorial: false`.
- **Le timing de l'exutoire colonial compte** : une expansion coloniale qui arrive pendant une phase active (féodale, oligarchique, absolutiste) prolonge cette phase. Si elle arrive après la RN (phase parlementaire), elle ne perturbe pas le Parcours.

**Pour établir la superficie de référence :**
- Identifier les changements territoriaux majeurs : conquêtes, unions dynastiques, pertes de territoire, traités.
- Pour chaque changement, estimer la superficie en milliers de km² et la décomposer en **noyau** (culturellement homogène) et **marges** (hétérogènes).
- Le noyau est défini par l'homogénéité culturelle (langue, droit), pas par le contrôle politique. Exemple : la France d'oïl est le noyau français ; le Languedoc occitanophone est une marge.
- Un territoire peut transiter de marge à noyau (ex. : pays de Galles en 1536, Écosse en 1707, Languedoc en 1539). Approximer par une date ponctuelle.
- Utiliser la **superficie seule** comme première approximation (pas de pondération par la population).

### Étape 3 : Analyse bottom-up par marqueurs

La classification en phases est un **résultat** du scoring des marqueurs, pas une hypothèse qu'on cherche à valider. La méthode procède strictement **du bas vers le haut** — des marqueurs observables dans chaque tranche d'histoire vers les phases, jamais l'inverse.

**⚠️ Interdiction de toute comparaison avec un parcours connu avant l'Étape 5.** Aucune analogie, aucun rapprochement « cette nation ressemble à X », aucun positionnement paramétrique (taille, projection) au départ. Les erreurs documentées viennent toutes d'un cadrage implicite posé pendant la recherche et jamais contesté — même quand la méthode est exécutée formellement, les scénarios produits restent des variations d'un même cadre tacite. Le bottom-up par marqueurs est la seule méthode qui empêche cet ancrage.

#### 3a : Découpage chronologique neutre

Découper l'histoire de la nation en **10 à 20 tranches**, séparées par des **événements forts** : révolutions, guerres, guerres civiles, changements de régime, traités fondateurs, changements dynastiques majeurs, réformes constitutionnelles. Aucun vocabulaire historionomique à ce stade — juste « tranche N : date1-date2, entre événement A et événement B ».

La sortie est une liste ordonnée de tranches avec dates de début/fin et nom de l'événement frontière.

#### 3b : Scoring des marqueurs par tranche

**Étape préalable anti-ancrage obligatoire** : avant de commencer le scoring, énumérer par écrit les nations du corpus qui pourraient servir d'ancrage silencieux — mêmes critères typologiques de surface (cité-État maritime, monarchie catholique, empire continental, cité commerçante, etc.) — et se déclarer explicitement qu'on ne les consultera pas pendant le scoring. Pendant le travail, si une justification de score fait implicitement référence à une de ces nations (« comme X », « analogue à Y », « moins fort que Z »), retravailler sans la référence. L'ancrage silencieux est la source d'erreur la plus fréquente en analyse historionomique — la détection demande une surveillance active.

Pour **chaque tranche**, évaluer la présence des marqueurs de **chacune des cinq phases** (féodale, oligarchique, absolutiste, RN, parlementaire). Pour chaque couple (tranche × phase), produire :
- **Score de confiance 0-5** fondé sur le nombre et la force des marqueurs présents
- **Justification textuelle courte** listant les marqueurs observés (et éventuellement ceux qui manquent)

La sortie est un tableau tranche × phase, avec scores et justifications. La phase d'une tranche est un **résultat** du scoring — pas une hypothèse. Si une tranche a un score élevé pour plusieurs phases, c'est un signal de transition ou d'ambiguïté à noter.

Marqueurs de chaque phase — cf. `references/phase_*.md` :
- **Féodale** : pouvoir reposant sur des liens personnels d'homme à homme, absence d'administration centrale permanente, stabilité rejouée à chaque succession. Liens de vassalité, chef supra-régional dont l'autorité force les autres à se positionner.
- **Oligarchique** : fisc permanent central, armée permanente, administration institutionnalisée, codification écrite — mais l'exécutif reste structurellement contraint par les grands (frein juridique effectif présent). Pacte oligarchique formel.
- **Absolutiste** : préséance de fait de l'administration centrale sur les administrations locales, exécutif pouvant agir sans frein juridique effectif des oligarques. Cinq formes admises à **énumérer et tester activement** (cf. `phase_absolutiste.md`) : (1) figure personnelle stable — pattern tiers populiste OU pattern faction-gagnante qui crée un nouveau cadre type Omri/Simon Thassi ; (2) institution collective stable ; (3) absolutisme informel factionnel (cité-État, signature empirique = instabilité chronique) ; (4) lignée ancestrale élargie ; (5) tiers exogène imposé. Ne jamais écarter une forme en moins de trois lignes — justifier chaque rejet par l'absence explicite de marqueurs.
- **RN** : **test discriminant fort** — la tranche précédente doit porter les marqueurs d'un Ancien Régime absolutiste (sédimentation des élites, surproduction élitaire, pression fiscale, clivage gauche-droite qui saute avec convergence ED/EG contre le bloc élitaire). **Sans AR préalable avéré, pas de RN.** Ensuite, chercher le pattern des 6 saillants canoniques (éclatement AR / expérience parlementaire / phase aiguë / thermidorien / IR / Glorieuse Révolution). Une révolte populaire suivie d'un dirigeant roturier porté au pouvoir et d'une réforme bicamérale est une signature à tester systématiquement.
- **Parlementaire** : représentation nationale élue, souveraineté de la chambre basse, administration subordonnée au législatif, après RN complète (Glorieuse Révolution qui clôt le cycle).

**Contrainte critique** : les marqueurs se lisent sur la tranche seule, sans comparaison avec aucune autre nation. Même si une configuration « ressemble à » un cas connu, cette ressemblance ne doit pas influencer le scoring. Seuls les marqueurs observables comptent.

#### 3c : Trois scénarios structurellement différents

À partir des scores de marqueurs, construire **trois scénarios** de découpage de l'histoire en phases. Chaque scénario est une proposition de mapping tranches → phases.

**Les trois scénarios doivent être vraiment divergents structurellement** — pas trois variations d'un même découpage, mais trois hypothèses distinctes qui peuvent différer sur :
- La position et le nombre des phases (ex. « RN tardive XIXe » vs « RN précoce XVIe » vs « pas de RN endogène »)
- La présence/absence de phases (ex. « transition absolutiste en X » vs « phase oligarchique prolongée sans transition »)
- Le caractère des transitions (ex. reboot par choc exogène vs prolongement)

Les trois doivent rester **historionomiquement cohérents** : phases dans l'ordre canonique (féodale → oligarchique → absolutiste → RN → parlementaire, avec reboots possibles), durées plausibles ou écarts expliqués par perturbations identifiées, transitions marquées par des saillants canoniques.

Si le scoring de marqueurs (3b) donne une lecture très dominante, les scénarios alternatifs servent quand même de test — ils permettent de vérifier que la lecture dominante tient sous pression. Leur fonction est d'être falsifiés, pas d'être retenus.

### Étape 4 : Vérification de cohérence interne

Pour **chaque scénario** construit à l'étape 3c, appliquer les contrôles suivants. Le scénario qui passe le plus de contrôles avec le moins d'ajustements forcés gagne.

#### 4a : Saillants canoniques et transitions

Pour **chaque phase** du scénario (féodale, oligarchique, absolutiste, RN dans l'ordre), vérifier :

1. **Les saillants canoniques sont-ils tous présents ?**
   - **Féodale** : éveil, pic(s) féodal(aux), crise(s) féodale(s), **pacte oligarchique** (généralement très formel — loi salique, Ordonnances, primogéniture, Libell, etc.)
   - **Oligarchique** : 1er monarque oligarchique, acmé oligarchique, polarisation, **guerre sociale** (deux factions + tiers résolvant)
   - **Absolutiste** : 1er monarque absolu (cf. `phase_absolutiste.md` pour les formes admises — à épuiser avant de conclure à l'absence), acmé absolutiste, fin d'expansion, remontrance, Ancien Régime
   - **RN** : les 7 étapes (éclatement de l'AR, expérience parlementaire, phase aiguë, moment thermidorien, IR, restauration, Glorieuse Révolution)
   
   Si un saillant canonique manque, **c'est un signal d'alarme**. Soit l'histoire a été mal lue (chercher plus fort), soit le cas est structurellement atypique (justifier alors structurellement). **Ne jamais se contenter de dire « absent, résolution diffuse »** sans justification solide.

2. **Le pacte oligarchique en particulier** : c'est une nécessité structurelle. Généralement très formel (acte écrit, diète, codification collective). Chercher activement : actes de type *Libell*, ordonnances, lois de succession, chartes, pactes de primogéniture, compromis avec les états. Un pacte faiblement identifié = analyse à reprendre.

3. **Les durées sont-elles cohérentes ?** La phase est-elle proche de la norme (200 ans pour féodale/oligarchique/absolutiste, 25-80 ans pour RN) ? Si écart, est-il expliqué par une perturbation identifiée ?

4. **Le test discriminant est-il passé à la bonne échelle ?** Pour les monarchies composites, l'absolutisme n'est atteint que quand l'administration centrale a préséance sur TOUTES les administrations locales du territoire national.

5. **L'expansion a-t-elle été attribuée à la bonne phase ?** L'expansion prolonge toujours la phase EN COURS au moment où elle commence.

6. **Les durées atypiques ont-elles été expliquées par des perturbations, pas par des ajustements d'identification ?** Le test discriminant PRIME SUR les durées. Si une identification a été choisie « parce que les durées collent mieux », revérifier le test discriminant.

7. **La guerre sociale se joue-t-elle à l'échelle pertinente ?** Si le Parcours est national, la guerre sociale doit opposer des factions à l'échelle nationale, pas seulement régionale.

#### 4b : Test événement par événement

**Revenir sur chaque événement majeur** de l'histoire de la nation (liste du découpage 3a + tous les événements documentés) et pour chacun, poser explicitement la question :

> *Mon interprétation de cet événement est-elle cohérente avec le scénario ? L'événement pourrait-il être autre chose que ce que j'ai supposé ?*

Exemples de questions-types :
- François Ier a-t-il été interprété (à tort) comme monarque absolu alors qu'il est une acmé oligarchique ?
- Cette réforme bicamérale a-t-elle été lue comme pacte renouvelé alors qu'elle est Glorieuse Révolution ?
- Cette figure a-t-elle été classée comme 1er monarque absolu alors qu'elle est un pic féodal isolé ?
- Cette révolte a-t-elle été classée en anecdote alors qu'elle ouvre une RN ?
- Cette transition dynastique a-t-elle été lue comme bascule oligarchique alors qu'elle est transition absolutiste ?

Documenter les événements où l'interprétation est **non triviale** (plusieurs lectures possibles) et la lecture retenue dans `justification.md`.

**Un événement majeur non expliqué ou mal expliqué = analyse à reprendre.** Soit intégrer l'événement dans le scénario (saillant, perturbation, ou mention contextuelle), soit reconsidérer le cadrage si l'événement ne colle pas du tout.

**Pourquoi c'est critique :** les erreurs documentées viennent systématiquement de l'omission ou de la mauvaise interprétation d'événements structurants. Sur l'Autriche v1, l'oubli de l'Innsbrucker Libell et du Blutgericht masquait le vrai pacte et la DGRO. La vérification événement par événement attrape ces omissions.

### Étape 5 : Comparaison tardive avec les saillants du corpus

**Seulement après l'Étape 4** : comparer les saillants retenus (dates, natures, contextes) avec les saillants équivalents dans le corpus. Cette comparaison est **une validation**, pas un cadrage.

**Règle stricte** : la comparaison se fait saillant par saillant (dates, caractéristiques structurelles), pas par récit global. Jamais « cette nation ressemble à X dans son ensemble ». Toujours « le 1er monarque absolu de cette nation présente les caractéristiques X, Y, Z ; dans le corpus, les cas comparables sont A, B, C ; les différences sont... ».

Ce que la comparaison permet de détecter :
- **Anomalies de datation** : saillant placé très en dehors des fenêtres typiques du corpus
- **Saillants atypiques** : 1er monarque absolu sans les marqueurs habituels, guerre sociale sans tiers résolvant identifiable
- **Configurations nouvelles** : éléments structurels inédits à remonter comme éléments théoriques nouveaux

**Filtrage facultatif du corpus** : on peut utiliser la taille (grande nation / cité-État / petite nation) et la projection (type d'exutoire) pour restreindre le corpus pertinent à la comparaison — mais comme **outil de filtrage**, jamais comme cadrage. Une cité-État avec exutoire maritime est comparée en priorité à d'autres cités-États avec exutoires équivalents, mais le résultat de la comparaison ne doit pas réorienter la lecture ; il doit seulement permettre de vérifier la plausibilité des saillants identifiés indépendamment.

Si la comparaison révèle des tensions fortes (ex. durée absolutiste +200 ans par rapport à toutes les autres nations comparables), c'est un signal de retour à l'Étape 3 ou 4 — pas de réajustement ad hoc.

### Étape 6 : Scoring final et scénario retenu

Pour chaque scénario, scorer sur :
- **Cohérence des scores de marqueurs (3b)** — la succession des phases suit-elle les scores les plus hauts de chaque tranche ?
- **Complétude des saillants canoniques (4a)** — tous les saillants sont-ils présents ou leur absence est-elle structurellement justifiée ?
- **Cohérence événementielle (4b)** — aucun événement majeur mal interprété ou ignoré
- **Durées endogènes** — écarts expliqués par perturbations identifiées
- **Concordance avec le corpus (5)** — saillants plausibles au regard des cas comparables
- **Nombre de singularités** — chaque affirmation « unique dans le corpus » est une **pénalité**. Trois singularités = présomption forte d'erreur de cadrage.

Le scénario avec le meilleur scoring gagne. Les scénarios écartés sont documentés dans `justification.md` avec leurs arguments pour et contre (comme les *machlokot* du Talmud : on conserve la trace du débat).

### Étape 7 : Produire le fichier `parcours.md`

Créer le fichier structuré `references/nations/<nation>/parcours.md` avec :
- La section `## Superficie de référence` avec les données noyau+marges (voir `references/parcours.md` pour le format)
- Les phases, sous-phases, saillants et perturbations identifiés
- Les perturbations territoriales codées avec le bon mécanisme (`choc_heterogeneite` pour les expansions, `correction_echelle` pour les contractions) et un titre spécifique (pas « Choc d'hétérogénéité » ou « Accélérateur » mais le nom de l'événement : « Empire Plantagenêt », « Perte de la Normandie »)
- Le flag `territorial: false` sur les perturbations non territoriales (culturelles ou institutionnelles)
- Les champs normalisés (type, start, end, title, summary, description, figure, confidence)
- Des résumés (summary) en 1-2 phrases et des descriptions (description) en 3-6 phrases construites — pas de style télégraphique

Ce fichier est le **résultat final** — il ne contient que l'hypothèse retenue, pas les débats.

### Étape 8 : Produire le fichier `justification.md`

Créer le fichier `references/nations/<nation>/justification.md` qui documente :

1. **Les hésitations** — pour chaque saillant où la confiance n'est pas « high », expliquer pourquoi on a hésité, quelles alternatives ont été envisagées, et pourquoi l'hypothèse retenue a été préférée
2. **Les hypothèses écartées** — documenter les hypothèses alternatives avec leurs arguments pour et contre (comme les *machlokot* du Talmud : on conserve la trace du débat même quand la décision est prise)
3. **Les questions ouvertes** — ce qui reste à confirmer, les points qui nécessitent davantage de cas comparatifs
4. **Les comparaisons** avec les parcours connus (Israël, France) — les parallèles qui éclairent et renforcent (ou affaiblissent) l'analyse

Le fichier de justification est **séparé** du parcours : le parcours est le résultat, la justification est le raisonnement. On peut modifier l'un sans toucher l'autre.

### Étape 9 : Discuter et itérer

L'historionomie est une discipline en cours de construction. L'utilisateur peut contester une identification, proposer un saillant alternatif, ou demander d'explorer une hypothèse. Claude doit être prêt à réviser son analyse sur la base d'arguments solides, et à mettre à jour le parcours ET la justification.

## Principes importants

### Priorité absolue : fiabilité des durées

L'usage principal du corpus est la **quantification statistique** (régression d'Alyocha Coencas sur les durées de phase). Plus il y a de parcours, plus la régression est robuste. Cela implique que **la fiabilité des dates de bornes** (éveil féodal, pacte, 1er monarque oligarchique, guerre sociale, 1er monarque absolu, éclatement de l'AR, Glorieuse Révolution) est la **première priorité absolue** de toute analyse. Sous-phases, naming, descriptions sont des raffinements secondaires — les durées sont l'enjeu.

Ne jamais forcer une date pour que les durées « collent mieux ». Les écarts atypiques sont toujours le signal d'une perturbation à identifier, pas d'une borne à déplacer.

### Présomption sur les mémoires de sessions précédentes

Si une mémoire de session précédente (dans `project_status.md` ou dossier memory) signale pour une cité-État **« absolutisme jamais atteint endogènement »** ou **« phase oligarchique interrompue avant résolution canonique »**, traiter comme une **présomption forte** que :
- Le test des formes 1 et 2 du 1er MA a déjà été fait et rejeté à raison (figure personnelle stable ou institution collective autonome au-dessus du patriciat).
- La forme 4 (absolutisme collectif par consortium oligarchique) n'a probablement PAS été testée activement.
- Il faut donc **d'abord tester activement la forme 4** avant de se ré-engager dans une lecture alternative.

Ne pas se contenter d'ajouter un paragraphe d'alternative dans justification.md — si la forme 4 colle sur une cité-État où un consortium institutionnalisé (banco, compagnie, société par actions publique) a capturé progressivement les fonctions d'État (cf. `phase_absolutiste.md`), c'est la lecture à retenir, pas une simple alternative à signaler.

### Pièges méthodologiques à éviter

Cinq pièges récurrents documentés :

1. **Lecture à rebours / télos fixé** — démarrer l'analyse depuis un événement final connu (absorption, unification, RN supposée) force mécaniquement les phases à s'ajuster à cette fenêtre. Analyser l'histoire **depuis le début**, sans connaître la fin. La fixation implicite d'un point d'absorption ou d'une date de RN supposée transforme le problème en « comment caser les phases dans cette fenêtre » au lieu de « à quel moment les saillants canoniques apparaissent-ils ».

2. **Noms vs fonction** — un régime formellement républicain avec un clan dominant peut fonctionner en absolutisme de facto. **Appliquer rigoureusement le test fonctionnel** : *l'exécutif peut-il agir sans frein juridique effectif des oligarques ?* Si oui, c'est de l'absolutisme, quelle que soit l'étiquette. Le contrôle des procédures électorales, l'exil d'opposants sans procès, la manipulation des commissions extraordinaires sont autant de marqueurs fonctionnels de l'absolutisme informel de cité-État.

3. **Singularités comme features** — si une analyse conclut qu'une nation est « unique dans le corpus » sur un élément structurel majeur (pas de pic féodal, pas de DGRO, deux acmés absolutistes, pas de remontrance, pas de 1er monarque absolu), c'est presque toujours une erreur de cadrage, pas une découverte. Traiter **chaque singularité comme une hypothèse d'erreur à réfuter**. Trois singularités dans le même parcours = forte présomption de cadrage faux.

4. **Engagement précoce dans un scénario** — une fois qu'un cadrage est choisi, l'analyse tend à forcer les données à s'y conformer (invention ad hoc de concepts non-canoniques pour justifier des durées atypiques ou des saillants manquants). **Obligation de l'Étape 3 : scoring bottom-up des marqueurs par tranche, puis trois scénarios structurellement divergents avant scoring final.**

5. **Ancrage par analogie de surface** — classer la nation par ressemblance culturelle ou géographique avec une nation déjà mappée (« républiques marchandes maritimes », « monarchies catholiques », « empires continentaux ») pendant la recherche ou au début de l'analyse contamine tout le raisonnement. **Toute comparaison avec le corpus est interdite avant l'Étape 5** — elle sert à valider, jamais à cadrer. Le scoring des marqueurs (Étape 3b) se fait sur la tranche seule, sans référence à aucune autre nation.

### Naming canonique — liste fermée obligatoire

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
- **RN** : Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien, Émergence de l'IR, Restauration, Glorieuse Révolution

**Distinction saillant vs sous-phase** :
- `Ancien régime` est une sous-phase **seulement** (pas un saillant). Le « moment » de l'entrée en AR est marqué par la Remontrance, pas par un saillant « Ancien Régime ».
- `Révolution initiale` est une sous-phase **seulement** — elle contient à l'intérieur les 4 saillants : Éclatement de l'AR, Expérience parlementaire, Phase aiguë, Moment thermidorien.
- `Restauration` est à la fois un **saillant** (le moment où l'ancien ordre est restauré — ex. 1815 en France) ET une **sous-phase** (la durée pendant laquelle il dure — ex. 1815-1830).
- `Émergence de l'IR` est un **saillant** — l'avènement de la figure autoritaire (ex. Bonaparte 1er consul, 1799). `impérialisme revanchard` est la **sous-phase** — la durée pendant laquelle la nation est portée par cette dynamique (ex. 1799-1815).

**Tout événement qui n'est pas dans la liste fermée n'est PAS un saillant** — c'est soit une **perturbation** (avec mécanisme + effet, parcimonieusement), soit une **mention dans la description** d'une sous-phase. Ne JAMAIS créer des saillants ad hoc avec des noms inventés (« Victoire de la Contre-Réforme », « Compromis austro-hongrois », « Privilegium Minus »). Les saillants sont des éléments codifiés.

**Événements perturbateurs** : nom historique sec (« Traité de Neuberg », « Innsbrucker Libell »), pas des descriptions narratives.

**Figures historiques** : nom seul. Surnoms UNIQUEMENT s'ils sont historiographiques canoniques et utiles à la désambiguïsation. Jamais d'épithètes ajoutées par goût littéraire (« le Glorieux », « le Fondateur »).

**Règle simple** : un titre de phase, sous-phase ou saillant est une étiquette de catalogage dans un vocabulaire canonique fermé, pas un titre de chapitre.

### Bornes de sous-phases — règles opératoires

Consulter le tableau récapitulatif des bornes dans `references/parcours.md`. Règles fondamentales :

1. **Une borne est toujours un saillant ou un événement identifiable** — jamais une date « arrondie approximative ».
2. **La fin d'une sous-phase et le début de la suivante coïncident** (ou se chevauchent de 1-2 ans maximum).
3. **Les bornes ne doivent pas être forcées** pour obtenir des durées typiques.
4. **Quand une sous-phase optionnelle est absente** (bascule oligarchique comprimée, IR absent, ancien régime écourté), justifier structurellement pourquoi.
5. **DGRO — la Dernière Grande Révolte Oligarchique est un saillant de FIN de phase oligarchique ou de DÉBUT de phase absolutiste** (pendant l'absolutisation), jamais au début de la phase oligarchique. Le mot « dernière » a un sens structurel : c'est le dernier sursaut oligarchique avant l'ancrage absolutiste.

### Catégorisation des événements historiques — 4 catégories

Tout événement historique mentionné dans un parcours relève de l'une de quatre catégories. Pas de « zone grise » — si un événement ne rentre pas clairement dans une catégorie, il faut trancher.

1. **Saillant canonique** — figure dans la liste fermée (cf. section Naming canonique). Affichage : rond de la couleur de la phase.
2. **Perturbation** — événement qui passe le **triple test** :
   - **mécanisme** identifiable parmi : choc d'hétérogénéité, choc exogène, insuffisance interne, correction d'échelle, exutoire
   - **effet** identifiable parmi : prolongement, accélération, avortement, reboot
   - **impact réel** sur la trajectoire du Parcours : la durée, le niveau ou la direction d'une phase aurait été différente sans cet événement
   
   Affichage : losange coloré (« diamant »).
3. **Anecdote de parcours** — événement historique sans impact sur la trajectoire (défaite mineure, scandale politique ordinaire, crise financière ponctuelle, figure mineure). Ne pas marquer dans le parcours structuré ; au plus mentionner en passant dans la description d'une sous-phase.
4. **Élément nouveau théorique** — événement qui semble structurellement important mais ne rentre dans aucune des trois catégories. **À remonter explicitement** pour discussion théorique, plutôt que de forcer artificiellement dans une catégorie existante.

**Règles opératoires** :
- **Les saillants canoniques ont priorité** : si un événement peut être un saillant canonique, le mettre en saillant, pas en perturbation. Exception : les **crises féodales** sont techniquement à la fois canoniques ET perturbations (insuffisance interne / avortement) — seul cas de chevauchement formel documenté.
- **Pas de plafond numérique** : une nation très perturbée peut légitimement avoir 15 perturbations, une nation calme peut n'en avoir que 3. L'important est que chaque perturbation passe le triple test. Le compte est un résultat, pas une contrainte.
- **Distinguer « faible intensité » (anecdote) de « fort impact » (perturbation)** : une défaite militaire ordinaire est une anecdote ; une occupation étrangère qui détruit les institutions est une perturbation.

### Terminologie stricte

- **Parcours** (majuscule) : le Parcours de construction nationale
- **Sous-phases** : découpage mécanique d'une phase (liste canonique fermée, voir ci-dessus)
- **Saillants** : éléments ponctuels facilement identifiables dans le vocabulaire canonique
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

L'historionomie est un cadre en construction. Certains saillants sont bien établis (éveil féodal, 1er monarque oligarchique, guerre sociale), d'autres sont encore en cours de validation (pic féodal, acmé oligarchique). Signaler les incertitudes plutôt que de forcer une identification.

Quand l'analyse d'une nouvelle nation révèle un cas qui ne colle pas au modèle, c'est potentiellement une découverte — pas un échec. Le signaler et en discuter.

### Langue

Ce skill est rédigé en français. Les discussions peuvent se faire en français ou en anglais selon la préférence de l'utilisateur.
