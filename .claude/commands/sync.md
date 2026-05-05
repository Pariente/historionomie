---
description: Se synchroniser sur master à jour avant de commencer une session de travail
---

Met l'utilisateur sur la branche `master` à jour avec le serveur, en protégeant son travail en cours. Suivre ces étapes dans l'ordre.

## 1. Inspecter l'état (en parallèle)

- `git status`
- `git branch --show-current`
- `git fetch origin` (pour avoir les dernières infos du serveur)

## 2. Vérifier qu'il n'y a pas de travail non sauvegardé

Si `git status` montre des modifications non commitées (staged ou unstaged) ou des fichiers non suivis qui semblent être du travail réel (pas des artefacts) :

- **Stop**. Dire à l'utilisateur en français simple : « Tu as du travail non sauvegardé sur cette branche. Lance `/ship` d'abord pour le sauvegarder, ou dis-moi de le jeter si tu n'en veux plus. »
- Lister brièvement les fichiers concernés.
- Ne pas continuer.

## 3. Aller sur master à jour

- Si la branche actuelle est déjà `master` :
  - `git pull --ff-only origin master`
- Sinon :
  - Vérifier si la branche actuelle a été fusionnée dans `origin/master` :
    - `git log origin/master..HEAD --oneline` — si vide, la branche est fusionnée (ou n'a jamais divergé).
  - `git checkout master`
  - `git pull --ff-only origin master`
  - Si la branche précédente avait été fusionnée dans master, proposer à l'utilisateur de la supprimer localement (`git branch -d <nom>`) — demander avant de le faire.
  - Si elle n'avait pas été fusionnée, ne **rien** supprimer, juste le mentionner : « Ta branche `<nom>` n'a pas encore été fusionnée — je la garde au cas où. »

## 4. Reporter

En une ou deux phrases en français :

- Branche actuelle (`master`).
- Combien de commits ont été récupérés depuis la dernière sync (utiliser le résultat de `git pull`).
- Si rien de nouveau : « Tu étais déjà à jour. »

## Notes

- **Ne jamais utiliser `git pull --rebase`, `git reset --hard`, ou `git push --force`** dans cette commande. Si quelque chose résiste (divergence, conflit), s'arrêter et expliquer le problème à l'utilisateur en mots simples.
- L'utilisateur cible n'est pas technique : éviter le jargon dans les messages, expliquer ce qui se passe.
