# GitHub Pages Deployment Guide

## Quick Start (Manual Steps)

### 1. Create a GitHub Repository
```bash
# If you don't have one yet, create it at https://github.com/new
# Name: planner-premium or similar
# Make it Public (required for free GitHub Pages)
```

### 2. Initialize & Push to GitHub
```bash
cd /Users/casild1/Documents/VS_Vault/projects/Planner_Prem

# If not a git repo yet:
git init
git add .
git commit -m "Initial commit: Planner Premium presentation"

# Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages (via Settings)
1. Go to **Settings** → **Pages**
2. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main** / **root** (/)
   - Click **Save**
3. Wait 1-2 minutes for deployment
4. Your site will be live at: `https://YOUR_USERNAME.github.io/REPO_NAME`

---

## Automated Setup (Using Scripts)

### Option A: One-Command Setup (Recommended)
```bash
chmod +x ./scripts/deploy-to-github.sh
./scripts/deploy-to-github.sh
```

Follow the prompts to enter your GitHub username and repository name.

### Option B: Using GitHub CLI (Fastest)
```bash
# Install gh if needed: https://cli.github.com/

# Create repo and push all in one command
gh repo create planner-premium --public --source=. --remote=origin --push
```

---

## Continuous Deployment (GitHub Actions)

### Auto-Deploy on Push
Once your repo is set up, create `.github/workflows/pages.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

This automatically deploys every time you push to main!

---

## File Structure for GitHub Pages
```
planner-premium/
├── planner-premium-deck-improved.html  (main presentation)
├── diagram_*.png                       (all diagrams)
├── resources/
│   └── art-logo-en-rgb-bl.png         (Medtronic logo)
├── .github/
│   └── workflows/
│       └── pages.yml                  (auto-deploy config)
├── README.md
└── GITHUB_SETUP.md
```

---

## Troubleshooting

**Issue:** Site not appearing after 5 minutes
- Check Pages settings in repo → Settings → Pages
- Verify branch is set to `main` and folder is `/root`
- Check "Actions" tab for build failures

**Issue:** Images not loading
- Ensure all image paths are relative (not absolute)
- Verify `resources/` folder is pushed to GitHub

**Issue:** Need to update presentation**
- Edit `planner-premium-deck-improved.html`
- Push to main: `git add . && git commit -m "..." && git push`
- GitHub Actions will auto-deploy in ~1 minute

---

## Next Steps

1. **After initial setup**, rename the file in your repo to `index.html` for cleaner URL
2. **Add a README.md** with usage instructions
3. **Set up custom domain** (optional) in Pages settings

---

## Quick Reference

| Task | Command |
|------|---------|
| Clone repo locally | `git clone <repo-url>` |
| Make changes & push | `git add . && git commit -m "msg" && git push` |
| View live site | `https://YOUR_USERNAME.github.io/REPO_NAME` |
| Check deployment status | Visit **Actions** tab in repo |
