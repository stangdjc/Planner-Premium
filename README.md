# Planner Premium Presentation

Professional HTML presentation for **Planner Premium Regional Readiness** initiative. Built with Medtronic brand colors, fully responsive, and optimized for web and PDF delivery.

## ✨ Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Full-Screen Presentation Mode**: Press `F` for distraction-free viewing
- **Keyboard Navigation**: Arrow keys to move between slides, `?` for help menu
- **Print/PDF Export**: Optimized styles for printing (Ctrl+P)
- **Accessibility**: ARIA labels, focus indicators, keyboard shortcuts
- **Brand Alignment**: Medtronic color palette and professional styling
- **No Dependencies**: Pure HTML/CSS/JavaScript—no build tools required

---

## 🚀 Quick Start

### View the Presentation Locally
```bash
# Open in your default browser
open planner-premium-deck-improved.html

# Or use a local server (Python)
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

### Deploy to GitHub Pages (Automated)

#### Mac/Linux:
```bash
chmod +x ./scripts/deploy-to-github.sh
./scripts/deploy-to-github.sh
```

#### Windows (PowerShell):
```powershell
.\scripts\deploy-to-github.ps1
```

#### Or use GitHub CLI (fastest):
```bash
gh repo create planner-premium --public --source=. --remote=origin --push
```

Then enable Pages in **Settings → Pages**.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` / `→` | Navigate slides |
| `F` | Toggle fullscreen mode |
| `?` | Show/hide help menu |
| `Ctrl+P` | Print to PDF |
| Click nav items | Jump to specific slide |

---

## 📁 File Structure

```
planner-premium/
├── planner-premium-deck-improved.html    # Main presentation (improved version)
├── planner-premium-deck.html             # Original version
├── README.md                             # This file
├── GITHUB_SETUP.md                       # Detailed GitHub Pages setup
├── diagram_01_npi_lifecycle.png          # NPI lifecycle diagram
├── diagram_02_card_hierarchy.png         # Card hierarchy structure
├── diagram_03_phase_gate_decision.png    # Phase gate flow
├── diagram_04_escalation_tree.png        # Escalation pathways
├── diagram_05_system_integration.png     # System integration map
├── diagram_06_roles_matrix.png           # Roles and RACI matrix
├── resources/
│   └── art-logo-en-rgb-bl.png           # Medtronic logo
└── scripts/
    ├── deploy-to-github.sh              # Mac/Linux deployment script
    └── deploy-to-github.ps1             # Windows PowerShell script
```

---

## 🎨 Customization

### Update Slide Content
Edit the `slidesData` array in `planner-premium-deck-improved.html`:

```javascript
const slidesData = [
  {
    eyebrow: "Section Name",
    title: "Slide Title",
    subtitle: "Optional subtitle",
    bullets: [
      "Bullet point 1",
      "Bullet point 2"
    ],
    tags: ["Tag1", "Tag2"],
    diagram: "image.png"  // Optional
  },
  // ... more slides
];
```

### Change Colors
Modify CSS variables at the top of the `<style>` section:

```css
:root {
  --primary-color: #004b87;      /* Main color */
  --secondary-color: #00a9e0;    /* Accent */
  --accent-color: #78be20;       /* Highlights */
}
```

### Update Logo
Replace the logo path in the HTML:

```html
<img src="your-logo.png" class="slide-logo" />
```

---

## 🌐 GitHub Pages Deployment

### Step 1: Create Repository
Go to [github.com/new](https://github.com/new) and create a **public** repository.

### Step 2: Run Deployment Script
```bash
./scripts/deploy-to-github.sh
```
Or follow manual steps in [GITHUB_SETUP.md](./GITHUB_SETUP.md)

### Step 3: Enable Pages
1. Go to **Settings → Pages**
2. Select **Deploy from a branch**
3. Choose **main** branch and **/ (root)** directory
4. Click **Save**

### Step 4: Access Live Presentation
Your presentation is now live at:
```
https://YOUR_USERNAME.github.io/REPO_NAME
```

---

## 🔄 Continuous Deployment

Once set up, the included GitHub Actions workflow (`.github/workflows/pages.yml`) automatically deploys whenever you push to main:

```bash
git add .
git commit -m "Update presentation content"
git push origin main
```

Your changes go live in ~1 minute. No manual deployment needed!

---

## 📊 19 Slides Included

1. **Title** - Planner Premium for Regional Readiness
2. **Agenda** - Overview of topics
3. **Executive Summary** - Key takeaways
4. **Who This Serves** - Audience & roles
5. **End-to-End Flow** - NPI lifecycle
6. **Phase Gates** - Governance structure
7. **Escalation Path** - Decision routing
8. **Board Architecture** - Card hierarchy
9. **Intake to Pipeline** - First phase details
10. **Global Alignment** - Global coordination
11. **Regional Alignment → Engage** - Regional prep
12. **Kick-off → Execute** - Delivery phase
13. **Close-Out** - Completion & learning
14. **Required Fields** - Data standards
15. **Custom Fields** - Extensible metadata
16. **Timeline & Dependencies** - Scheduling
17. **System Integration** - Tools & connections
18. **File & Link Hygiene** - Organization standards
19. **Roles & RACI** - Responsibilities matrix

---

## 🐛 Troubleshooting

### Site not loading on GitHub Pages
- Check **Settings → Pages** is enabled
- Verify branch is set to `main` (not `master`)
- Ensure publish directory is `/` (root)

### Images not showing
- Verify all image files are in the repo
- Check file paths are relative (e.g., `diagram_01.png` not `/absolute/path`)
- Images must be in the same commit as the HTML

### Keyboard shortcuts not working
- Try reloading the page
- Check browser console (F12) for JavaScript errors
- Some shortcuts may be blocked by browser (e.g., Ctrl+P in some contexts)

### PDF export has wrong formatting
- Use **Chrome/Edge** for best print quality
- Set margins to 0.5" in print dialog
- Uncheck "Background graphics" if you want lighter colors

---

## 📝 License

This presentation is based on the Planner Premium Regional Readiness initiative.

---

## 🤝 Contributing

To make updates:

1. **Edit locally**: Open HTML in your editor
2. **Test locally**: Open in browser to verify changes
3. **Push to GitHub**: `git add . && git commit -m "..." && git push`
4. **Verify deployment**: Check your live site in ~1 minute

---

## 📞 Support

For issues or questions:
- Check [GITHUB_SETUP.md](./GITHUB_SETUP.md) for deployment help
- Review keyboard shortcuts with `?` key in the presentation
- Check GitHub repository **Actions** tab for deployment logs

---

**Last Updated**: January 2026  
**Version**: 2.0 (Improved with responsive design, full-screen mode, and accessibility)
