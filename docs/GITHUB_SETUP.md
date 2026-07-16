# Publishing to GitHub

The project ships as a ready git repository with one clean commit on `main`.

## Option A — from the git bundle (recommended)
A portable bundle (`ai-spanish-platform.bundle`) contains the full history in one file.

```bash
git clone ai-spanish-platform.bundle ai-spanish-platform
cd ai-spanish-platform

# create the empty repo on GitHub first (UI or gh), then:
git remote set-url origin https://github.com/<you>/<repo>.git   # or: git remote add origin ...
git push -u origin main
```

Using the GitHub CLI (creates the repo and pushes in one go):
```bash
git clone ai-spanish-platform.bundle ai-spanish-platform && cd ai-spanish-platform
gh repo create <repo> --private --source . --remote origin --push
```

## Option B — from the source zip
```bash
unzip ai-spanish-platform.zip && cd ai-spanish-platform
git init -b main && git add -A && git commit -m "Initial commit"
gh repo create <repo> --private --source . --remote origin --push
# or add a remote manually and: git push -u origin main
```

## Notes
- Authentication is yours to provide (HTTPS token or SSH key / `gh auth login`); it is not
  bundled for security reasons.
- Secrets are ignored by `.gitignore` — only `.env.example` / `.env.selfhosted.example` are
  tracked. Set real values in a local `.env` after cloning (`make env`).
- Suggested repo name: `ai-spanish-platform`. Add topics: `spanish`, `fastapi`, `react`,
  `telegram-mini-app`, `language-learning`.
