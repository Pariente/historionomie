# Guide de démarrage — Historionomie avec Claude Code

Bienvenue ! Ce guide t'explique tout ce dont tu as besoin pour travailler sur le projet d'historionomie avec Claude Code, **sans aucun prérequis technique**. Tu n'as rien à apprendre par cœur : tu peux revenir lire ce fichier autant de fois que tu veux.

---

## 1. C'est quoi, ce projet ?

Le dossier `historionomie/` contient un cadre théorique pour analyser le **Parcours de construction nationale** des nations (féodale → oligarchique → absolutiste → révolution nationale → parlementaire), ainsi que les parcours déjà cartographiés d'une quinzaine de nations (France, Angleterre, Autriche, Espagne, Florence, Venise, Suisse, etc.).

Tout est rangé dans deux endroits :

- `references/` — le cadre théorique et les parcours nationaux (fichiers texte `.md`)
- `docs/` — les pages web et infographies générées à partir des fichiers texte

Tu n'as **pas besoin de modifier directement les fichiers**. Claude le fera pour toi.

---

## 2. C'est quoi, Claude Code ?

Claude Code est un assistant qui tourne dans le **Terminal** (la fenêtre noire avec du texte). Tu lui parles en français comme à un humain, et il fait le travail à ta place : il lit les fichiers, écrit des analyses, modifie des documents, sauvegarde les changements, etc.

### Démarrer une session

1. Ouvre l'application **Terminal** (cherche-la avec Spotlight : `Cmd + Espace`, tape « Terminal »).
2. Tape cette commande puis appuie sur Entrée :
   ```
   cd ~/Documents/historionomie
   claude
   ```
3. Une interface bleue s'ouvre. **Tu peux maintenant écrire ce que tu veux à Claude.**

Pour quitter : tape `/exit` ou ferme simplement la fenêtre.

---

## 3. Ce que tu peux faire

### A. Poser des questions sur le cadre théorique

Tu peux demander n'importe quoi sur l'historionomie. Claude lira les fichiers de référence et te répondra.

**Exemples** :
- *« Explique-moi ce qu'est un saillant, et donne-moi des exemples. »*
- *« Quelle est la différence entre la phase oligarchique et la phase absolutiste ? »*
- *« C'est quoi, la matrice 2×2 des élites ? »*
- *« Comment on identifie une révolution nationale ? »*

### B. Poser des questions sur une nation déjà cartographiée

**Exemples** :
- *« Résume-moi le parcours de la France. »*
- *« Pourquoi la phase absolutiste autrichienne a-t-elle duré aussi longtemps ? »*
- *« Compare les saillants de l'Angleterre et de la France. »*

### C. Cartographier une nouvelle nation

C'est le plus gros travail du projet. Une commande spéciale, **`/cartographie`**, lance une analyse complète multi-étapes (collecte historique, scoring par phase, vérification, génération du fichier final et de l'infographie).

**Comment faire** :
- Tape simplement : `/cartographie Pologne` (ou n'importe quelle nation).
- Laisse Claude travailler — ça peut prendre **plusieurs dizaines de minutes**, c'est normal. Il lance plusieurs sous-agents en parallèle.
- À la fin, tu auras un nouveau dossier `references/nations/pologne/` avec le parcours, et une infographie dans `docs/pologne.html`.

**Avant de lancer** : si tu n'es pas sûr qu'une nation se prête bien à l'exercice, demande d'abord *« est-ce que la Pologne est un bon candidat pour une cartographie historionomique ? »* — Claude te dira si le cas est intéressant ou problématique.

### D. Apporter une modification ou une correction

Si en lisant un parcours existant tu remarques une erreur, ou si tu veux affiner une formulation :

**Exemples** :
- *« Dans le parcours d'Espagne, je trouve que la datation de la guerre sociale est trop tardive. Peux-tu regarder ? »*
- *« Reformule la justification de l'éveil féodal anglais, je la trouve confuse. »*
- *« Ajoute une perturbation 'Peste noire' au parcours français. »*

Claude lira le fichier concerné, te proposera une modification, et la fera si tu valides.

### E. Discuter le cadre théorique lui-même

L'historionomie est une discipline en construction. Si en lisant tu te dis « tiens, ça ne colle pas », c'est peut-être une vraie découverte. Pose la question :

- *« Le cas de la Suisse semble bizarre — est-ce qu'il y a quelque chose à revoir dans la théorie ? »*
- *« Je ne comprends pas pourquoi on classe X comme perturbation et pas comme saillant. »*

---

## 4. Comment bien parler à Claude

- **Parle-lui normalement, en français.** Pas besoin de mots-clés ni de syntaxe spéciale.
- **Sois concret.** *« Explique-moi la phase féodale »* est mieux que *« phase féodale »*.
- **Si la réponse ne te convient pas, dis-le.** *« Non, je voulais plutôt… »* — Claude ajuste.
- **Tu peux toujours dire « stop » ou changer de sujet.** Aucun engagement, aucune pénalité.
- **Si tu hésites, demande.** *« Est-ce que cette modification a du sens ? »*, *« Avant de faire ça, qu'est-ce que tu en penses ? »*.

---

## 5. Te synchroniser avec `/sync` (à faire au début de chaque session)

Avant de commencer à travailler, il faut **récupérer les dernières modifications** du projet — celles que Thomas (ou toi-même depuis un autre ordinateur) a pu faire entre-temps. Sans ça, tu risques de travailler sur une version périmée.

C'est ce que fait la commande **`/sync`**.

### Ce que `/sync` fait pour toi

1. Vérifie que tu n'as pas de travail non sauvegardé (sinon il s'arrête et te dit de faire `/ship` d'abord).
2. Te remet sur la branche principale (`master`) — celle qui contient la version officielle du projet.
3. Télécharge les dernières modifications depuis le serveur (GitHub).
4. Te dit où tu en es (combien de nouveautés ont été récupérées).

### Comment l'utiliser

Tape simplement, **au tout début de chaque session** :
```
/sync
```

Si tout va bien, tu verras un message du genre « Tu es sur master, à jour. » ou « 3 nouveaux commits récupérés. » Tu peux ensuite travailler normalement.

### À quel moment l'utiliser ?

- **Au début de chaque session de travail.** C'est le réflexe à prendre.
- **Si Thomas te dit « j'ai mergé ta PR »** ou « j'ai poussé des changements ». Tu lances `/sync` pour récupérer la nouvelle version officielle.
- **En cas de doute, lance-le.** Il ne fait jamais rien de risqué — au pire, il te dit qu'il y a un problème et s'arrête.

---

## 6. Sauvegarder ton travail avec `/ship`

Quand tu as fini une session de travail (cartographié une nation, fait des corrections, etc.), il faut **sauvegarder** les changements. Sinon, ils restent uniquement sur ton ordinateur et personne d'autre ne peut les voir.

C'est ce que fait la commande **`/ship`**.

### Ce que `/ship` fait pour toi (en une seule commande)

1. Regroupe tous les fichiers que tu as modifiés.
2. Crée un « point de sauvegarde » (un *commit*, dans le jargon).
3. Crée une « branche » (une copie parallèle du projet) si tu travailles sur le tronc principal.
4. Envoie tout ça sur GitHub (le serveur où le projet est hébergé).
5. Ouvre une **Pull Request** — c'est-à-dire une proposition de fusion de ton travail avec le projet principal, que Thomas pourra relire et accepter.
6. Ouvre la page de la Pull Request dans ton navigateur, pour que tu voies le résultat.

### Comment l'utiliser

Tape simplement :
```
/ship
```

Claude fait tout le reste. Il te montrera ce qu'il s'apprête à faire avant de l'envoyer — tu peux toujours dire « non, attends » si quelque chose te semble bizarre.

### À quel moment l'utiliser ?

- **Quand tu penses qu'un morceau de travail est terminé** (par exemple : tu viens de cartographier la Pologne, ou tu viens de corriger 3 fautes dans le parcours espagnol).
- **Pas besoin de le faire après chaque petite chose.** Une fois par session de travail suffit.
- **En cas de doute, lance-le.** Mieux vaut une sauvegarde de trop qu'un travail perdu.

---

## 7. En cas de problème

- **Claude se trompe ou hallucine** → dis-lui *« non, ce n'est pas ça, vérifie dans le fichier X »*. Il corrigera.
- **Tu as fait une bêtise** → demande *« annule la dernière modification »* ou *« remets le fichier comme il était »*. Tant que tu n'as pas fait `/ship`, rien n'est définitif.
- **Tu ne comprends pas un terme** → demande *« c'est quoi, [le terme] ? »*. Claude expliquera.
- **Une commande ne marche pas** → copie-colle le message d'erreur dans Claude et demande *« qu'est-ce que ça veut dire ? »*.

---

## 8. Quelques règles d'or du projet

Thomas tient beaucoup à ces principes (ils sont aussi écrits dans `CLAUDE.md`, que Claude lit automatiquement) :

1. **L'honnêteté avant la propreté.** Mieux vaut un parcours avec des trous honnêtes qu'un parcours faussement complet. Si quelque chose ne colle pas, on le dit.
2. **Pas d'identification forcée.** Si on n'est pas sûr d'un saillant, on le marque comme incertain.
3. **Les durées atypiques sont des signaux, pas des erreurs.** Une phase de 350 ans n'est pas une faute — c'est une perturbation à comprendre.
4. **Les noms canoniques sont fermés.** On utilise le vocabulaire défini, on n'invente pas de nouvelles catégories sans en discuter.

Tu n'as pas à les retenir : Claude les applique pour toi. Mais c'est utile de savoir qu'ils existent.

---

## 9. Pour aller plus loin

- `CLAUDE.md` — les instructions complètes du projet (Claude les lit automatiquement, mais tu peux y jeter un œil).
- `references/parcours.md` — le cadre théorique général. **Bonne première lecture.**
- `references/nations/france/parcours.md` — un exemple de parcours bien cartographié.
- `docs/index.html` — ouvre ce fichier dans un navigateur pour voir les infographies de toutes les nations.

---

**Bienvenue dans le projet, Martin. Bon courage, et n'hésite jamais à demander.**
