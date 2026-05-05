---
description: Stage, commit, branch off dev if needed, push, open PR, and open it in browser
---

Ship the current working changes through to an open PR. Steps:

1. Run `git status` and `git diff` (staged + unstaged) in parallel to see what will be committed.
   Run `git log -5 --oneline` to match commit style.
2. Refuse to proceed if any obviously sensitive file is staged (`.env`, `credentials.json`, anything matching `*secret*`, `*.pem`, `*.key`). Warn and stop.
3. Determine current branch with `git rev-parse --abbrev-ref HEAD`.
   - If the current branch is `dev` (or `main`), pick a branch name from the change:
     - Prefix: `feat/` for new features, `fix/` for bug fixes (match the type of change you see in the diff).
     - Slug: 2–4 kebab-case words summarizing the change.
     - Run `git checkout -b <prefix>/<slug>`.
   - Otherwise stay on the current branch.
4. `git add .` — but only after the secrets check above.
5. Draft a commit message:
   - Subject line: conventional prefix (`feat:`, `fix:`, `refactor:`, `task:`) + concise summary, ≤72 chars, imperative mood, no trailing period.
   - Body only if the change is non-trivial: 1–3 short lines explaining *why*, not *what*.
   - Elegant and concise. No fluff, no emojis.
6. Commit with the standard `Co-Authored-By` trailer (use the HEREDOC pattern from the system prompt).
7. `git push -u origin HEAD`.
8. `gh pr create --base dev --title "<subject>" --body "$(cat <<'EOF' ... EOF)"` with a short body:
   ```
   ## Summary
   <1–3 bullets>

   ## Test plan
   - [ ] <how to verify>
   ```
9. Capture the PR URL from `gh pr create` output and open it: `open <url>` (macOS).
10. Report the PR URL back to the user in one line.

Notes:
- Base branch is **always `dev`**, never `main`.
- If the working tree is clean, stop and say so — don't create empty commits or branches.
- If `gh` is not authenticated, surface the error and stop instead of trying to fix it.
