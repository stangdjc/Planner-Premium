# GitHub Pages Deployment Script (Windows PowerShell)
# Automates: git init, commit, remote add, and push to GitHub

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  Planner Premium → GitHub Pages Deployment                  ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Get current directory
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
Set-Location $ProjectDir

# Check if already a git repo
if (Test-Path ".git") {
    Write-Host "✓ Git repository already initialized" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "→ Initializing new Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
    Write-Host ""
}

# Get user inputs
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "STEP 1: GitHub Repository Details" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
$Username = Read-Host "GitHub username"
$RepoName = Read-Host "Repository name (e.g., planner-premium)"

# Validate inputs
if ([string]::IsNullOrWhiteSpace($Username) -or [string]::IsNullOrWhiteSpace($RepoName)) {
    Write-Host "✗ Error: Username and repository name are required" -ForegroundColor Red
    exit 1
}

$RepoUrl = "https://github.com/$Username/$RepoName.git"

Write-Host ""
Write-Host "Repository URL: $RepoUrl" -ForegroundColor Gray
Write-Host ""

# Check if remote already exists
$RemoteExists = git remote | Select-String "^origin$"
if ($RemoteExists) {
    Write-Host "→ Updating existing remote..." -ForegroundColor Yellow
    git remote remove origin
}

Write-Host "→ Adding remote origin..." -ForegroundColor Yellow
git remote add origin $RepoUrl
Write-Host "✓ Remote added" -ForegroundColor Green
Write-Host ""

# Stage and commit
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "STEP 2: Staging & Committing Files" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "→ Staging all files..." -ForegroundColor Yellow
git add .

Write-Host "→ Creating commit..." -ForegroundColor Yellow
git commit -m "Planner Premium: Initial GitHub Pages setup with improved HTML deck"
Write-Host "✓ Files committed" -ForegroundColor Green
Write-Host ""

# Ensure main branch
Write-Host "→ Ensuring main branch..." -ForegroundColor Yellow
git branch -M main 2>$null
Write-Host "✓ On main branch" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "STEP 3: Pushing to GitHub" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "→ Pushing main branch..." -ForegroundColor Yellow
git push -u origin main
Write-Host "✓ Push successful!" -ForegroundColor Green
Write-Host ""

# Setup GitHub Pages workflow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "STEP 4: Setting up GitHub Actions for Auto-Deploy" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""

$WorkflowsDir = ".github\workflows"
if (-not (Test-Path $WorkflowsDir)) {
    New-Item -ItemType Directory -Path $WorkflowsDir | Out-Null
}

$WorkflowContent = @'
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
'@

Set-Content -Path "$WorkflowsDir\pages.yml" -Value $WorkflowContent
Write-Host "✓ GitHub Actions workflow created" -ForegroundColor Green
Write-Host ""

# Commit the workflow file
git add "$WorkflowsDir\pages.yml"
git commit -m "Add GitHub Actions workflow for automatic Pages deployment" -ErrorAction SilentlyContinue
git push origin main

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✓ DEPLOYMENT COMPLETE!                                      ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Next Steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Enable GitHub Pages in your repository:" -ForegroundColor White
Write-Host "   → Go to: https://github.com/$Username/$RepoName/settings/pages" -ForegroundColor Gray
Write-Host "   → Source: Deploy from a branch" -ForegroundColor Gray
Write-Host "   → Branch: main / (root)" -ForegroundColor Gray
Write-Host "   → Click Save" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Your presentation will be live at:" -ForegroundColor White
Write-Host "   → https://$Username.github.io/$RepoName" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Future updates:" -ForegroundColor White
Write-Host "   → Just push changes to main: git add . && git commit && git push" -ForegroundColor Gray
Write-Host "   → GitHub Actions will auto-deploy!" -ForegroundColor Gray
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
