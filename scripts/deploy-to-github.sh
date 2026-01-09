#!/bin/bash

###############################################################################
# GitHub Pages Deployment Script
# Automates: git init, commit, remote add, and push to GitHub
###############################################################################

set -e  # Exit on error

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  Planner Premium → GitHub Pages Deployment                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Get current directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

# Check if already a git repo
if [ -d ".git" ]; then
    echo "✓ Git repository already initialized"
    echo ""
else
    echo "→ Initializing new Git repository..."
    git init
    echo "✓ Git repository initialized"
    echo ""
fi

# Get user inputs
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: GitHub Repository Details"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
read -p "GitHub username: " USERNAME
read -p "Repository name (e.g., planner-premium): " REPO_NAME

# Validate inputs
if [ -z "$USERNAME" ] || [ -z "$REPO_NAME" ]; then
    echo "✗ Error: Username and repository name are required"
    exit 1
fi

REPO_URL="https://github.com/${USERNAME}/${REPO_NAME}.git"

echo ""
echo "Repository URL: $REPO_URL"
echo ""

# Check if remote already exists
if git remote | grep -q "^origin$"; then
    echo "→ Updating existing remote..."
    git remote remove origin
fi

echo "→ Adding remote origin..."
git remote add origin "$REPO_URL"
echo "✓ Remote added"
echo ""

# Stage and commit
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: Staging & Committing Files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "→ Staging all files..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ No changes to commit"
else
    echo "→ Creating commit..."
    git commit -m "Planner Premium: Initial GitHub Pages setup with improved HTML deck"
    echo "✓ Files committed"
fi

echo ""

# Ensure main branch
echo "→ Ensuring main branch..."
if git rev-parse --quiet --verify main > /dev/null 2>&1; then
    git branch -M main 2>/dev/null || true
else
    echo "Creating main branch..."
fi
echo "✓ On main branch"
echo ""

# Push to GitHub
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 3: Pushing to GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "→ Pushing main branch..."
git push -u origin main
echo "✓ Push successful!"
echo ""

# Setup GitHub Pages workflow
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 4: Setting up GitHub Actions for Auto-Deploy"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

WORKFLOWS_DIR=".github/workflows"
mkdir -p "$WORKFLOWS_DIR"

cat > "$WORKFLOWS_DIR/pages.yml" << 'EOF'
name: Deploy Planner Premium to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Setup Pages
        uses: actions/configure-pages@v3
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: '.'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
EOF

echo "✓ GitHub Actions workflow created"
echo ""

# Commit the workflow file
git add "$WORKFLOWS_DIR/pages.yml"
git commit -m "Add GitHub Actions workflow for automatic Pages deployment" || true
git push origin main

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  ✓ DEPLOYMENT COMPLETE!                                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Enable GitHub Pages in your repository:"
echo "   → Go to: https://github.com/${USERNAME}/${REPO_NAME}/settings/pages"
echo "   → Source: Deploy from a branch"
echo "   → Branch: main / (root)"
echo "   → Click Save"
echo ""
echo "2. Your presentation will be live at:"
echo "   → https://${USERNAME}.github.io/${REPO_NAME}"
echo ""
echo "3. Future updates:"
echo "   → Just push changes to main: git add . && git commit && git push"
echo "   → GitHub Actions will auto-deploy!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
