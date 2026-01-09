# Quick Start Guide

## For Presenters: View the Presentation

### Option 1: Open in Browser (Simplest)
```bash
# Mac
open planner-premium-deck-improved.html

# Windows - open in file explorer and double-click the file

# Or any browser - drag & drop the file
```

### Option 2: Use Local Server (Better for images)
```bash
python3 -m http.server 8000
# Visit: http://localhost:8000
```

---

## For Developers: Deploy to GitHub Pages

### One-Line Setup (Mac/Linux)
```bash
chmod +x ./scripts/deploy-to-github.sh && ./scripts/deploy-to-github.sh
```

### One-Line Setup (Windows PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-to-github.ps1
```

### Manual Setup (If scripts don't work)
```bash
git init
git add .
git commit -m "Initial Planner Premium presentation"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```
Then: Settings → Pages → Deploy from main branch

---

## Using the Presentation

### Navigation
- **Arrow Keys** or **Prev/Next buttons** - Move between slides
- **Click slide numbers** in sidebar - Jump to specific slide

### Presentation Mode
- Press **F** for fullscreen mode (hides sidebar)
- Press **F** again to exit fullscreen
- Perfect for displaying on projectors or large screens

### Export as PDF
- Press **Ctrl+P** (or Cmd+P on Mac)
- Click "Save as PDF"
- Open PDF in your PDF viewer
- Perfect for sharing or archiving

### Get Help
- Press **?** to see all keyboard shortcuts
- Shortcuts include: Navigation, Fullscreen, PDF export, Help menu

---

## 3 Key Improvements Made

### 1️⃣ Responsive Design
- Works on desktop, tablet, and mobile phones
- Sidebar converts to horizontal nav on small screens
- Properly sized content for all viewport widths

### 2️⃣ Print/PDF Optimization
- Specific print stylesheet removes UI elements
- Proper page breaks between slides
- Optimized image and text sizing for PDF
- Dark text on white background for clarity

### 3️⃣ Enhanced Accessibility
- Full-screen presentation mode (F key)
- Keyboard shortcuts help menu (? key)
- Better focus indicators for keyboard navigation
- ARIA labels for screen readers
- Better visual feedback on interactions

---

## File Naming

The improved version is: **planner-premium-deck-improved.html**

The original is preserved as: **planner-premium-deck.html**

To make the improved version your main file:
```bash
# Rename the improved version to be the primary file
mv planner-premium-deck-improved.html index.html

# Now it will be the default when someone visits your GitHub Pages site
```

---

## Typical Workflow

### Day 1: Initial Setup
```bash
./scripts/deploy-to-github.sh
# Answer prompts with GitHub username and repo name
# Check repository Settings → Pages to enable
```

### Day 2+: Update Content
```bash
# Edit planner-premium-deck-improved.html in your editor
# Test in browser locally
# Push to GitHub
git add .
git commit -m "Update slide content"
git push

# Live site updates in ~1 minute automatically!
```

---

## Support Resources

1. **GITHUB_SETUP.md** - Detailed GitHub Pages setup with troubleshooting
2. **README.md** - Full documentation with examples
3. **Presentation Help** - Press `?` while viewing presentation
4. **GitHub Actions** - Check Settings → Actions for deployment logs

---

## Common Tasks

### Change presentation content
Edit `slidesData` array in `planner-premium-deck-improved.html`

### Change brand colors
Edit `:root` CSS variables at top of `<style>` section

### Add new diagram
1. Add PNG file to project root
2. Add `diagram: "filename.png"` to slide object
3. Push to GitHub

### Fix broken images
1. Verify image files are in repository
2. Check file paths are relative (no `/absolute/path`)
3. Make sure images are pushed to GitHub in same commit as HTML

---

## Next Steps

1. ✅ You have the improved HTML presentation
2. ✅ You have deployment scripts ready
3. → Run `./scripts/deploy-to-github.sh` to deploy
4. → Enable GitHub Pages in repository settings
5. → Share the live URL with stakeholders

Done! 🎉
