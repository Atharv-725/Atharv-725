# GitHub Profile Build Guide

## Overview
This project generates dynamic, animated SVG assets for your GitHub profile README. All assets are created programmatically to keep your profile fresh and engaging.

## Building Assets

### Quick Build
```bash
python build.py
```

This runs all three generators in sequence:
1. Profile icons and visualizations
2. Languages & tools visualization
3. GitHub statistics

### Individual Generators

If you need to run individual scripts:

```bash
# Generate animated icons and visualizations
python scripts/generate_profile_assets.py

# Generate languages & tools SVG (uses icons_cache.json)
python scripts/generate_tools.py

# Generate GitHub statistics
python scripts/generate_stats.py
```

## Environment Setup

### GitHub Token (Optional but Recommended)
For more accurate statistics, set a GitHub personal access token:

```bash
# Windows PowerShell
$env:GITHUB_TOKEN = "your-token-here"

# Windows CMD
set GITHUB_TOKEN=your-token-here

# Linux/Mac
export GITHUB_TOKEN=your-token-here
```

Get a token from: https://github.com/settings/tokens

## Generated Assets

### Icon Files (`assets/icons/`)
- **about_me.svg** - Section header icon
- **focus_areas.svg** - Section header icon
- **current_goals.svg** - Section header icon
- **featured_projects.svg** - Section header icon
- **achievements.svg** - Section header icon
- **bullet_project.svg** - Bullet point for projects
- **bullet_achievement.svg** - Bullet point for achievements

### Visualization SVGs (`assets/`)
- **focus_areas.svg** - Shows your focus areas with floating animations
- **current_goals.svg** - Displays current goals with pulsing indicators
- **languages_tools.svg** - Tech stack visualization with 4 categories:
  - Languages (Java, Python, C++, JavaScript)
  - Frontend (HTML5, CSS3, React, Bootstrap)
  - Backend & Databases (Node.js, Express, MongoDB, MySQL)
  - AI/ML & Tools (TensorFlow, PyTorch, Git, VS Code, Arduino)
- **github_stats.svg** - GitHub statistics card with:
  - Total stars, commits, PRs, issues
  - Current & longest contribution streaks
  - Programming languages breakdown

## Customization

### Update Focus Areas
Edit `generate_profile_assets.py` → `create_focus_areas_svg()` function to modify:
- Focus area titles
- Colors (hex codes)
- Layout

### Update Goals
Edit `generate_profile_assets.py` → `create_current_goals_svg()` function to modify:
- Goal descriptions
- Colors
- Layout

### Update Languages & Tools
Edit `generate_tools.py` → `categories` array to modify:
- Supported tools list
- Category names
- Icon arrangement

## Deployment

After building, commit to your GitHub profile repository:

```bash
# Stage all assets
git add assets/

# Commit
git commit -m "Generate profile assets"

# Push
git push origin main
```

Then reference the SVGs in your README.md:
```markdown
<img src="assets/focus_areas.svg" alt="Focus Areas" width="560" />
<img src="assets/current_goals.svg" alt="Current Goals" width="560" />
<img src="assets/github_stats.svg" alt="GitHub Stats" width="560" />
<img src="assets/languages_tools.svg" alt="Languages & Tools" width="560" />
```

## Troubleshooting

### Missing Icons in languages_tools.svg
Some icons may be missing if not in `icons_cache.json`. The generator will warn but continue.

### GitHub API Rate Limiting
If you get API errors without a token, GitHub has lower rate limits for unauthenticated requests. Set `GITHUB_TOKEN` to increase limits.

### Stats Not Updating
- Ensure you have internet connection
- Check GitHub is not experiencing outages
- Verify username in `generate_stats.py` (line ~170)

## File Structure
```
.
├── build.py                    # Main build script
├── scripts/
│   ├── generate_profile_assets.py  # Icons & visualizations
│   ├── generate_stats.py           # GitHub statistics
│   ├── generate_tools.py           # Languages & tools SVG
│   └── icons_cache.json            # Base64 encoded icons
└── assets/
    ├── icons/                  # Generated icon SVGs
    ├── focus_areas.svg         # Generated
    ├── current_goals.svg       # Generated
    ├── languages_tools.svg     # Generated
    └── github_stats.svg        # Generated
```

## Next Steps

1. ✅ Generated all assets
2. Customize icons/visualizations as needed
3. Commit to GitHub
4. Monitor stats with periodic rebuilds
5. Update focus areas and goals as they evolve

## Performance Tips

- Run build during off-peak hours to avoid GitHub API rate limits
- Cache results locally to reduce API calls
- Use `GITHUB_TOKEN` for increased rate limits

---

*Last updated: 2026-06-24*
