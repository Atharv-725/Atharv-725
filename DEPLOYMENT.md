# Deployment Checklist

## Before Pushing to GitHub

- [ ] All SVG files generated successfully in `assets/`
- [ ] Verified `assets/icons/` contains all icon SVGs
- [ ] Check `github_stats.svg` displays correct stats
- [ ] Reviewed color schemes and animations in preview
- [ ] All links in README.md point to correct asset paths

## Repository Setup

If this is your profile repository:

```bash
# Navigate to your GitHub profile directory
cd Atharv-725

# Check git status
git status

# Stage all generated assets
git add assets/

# Verify the staging
git status
```

## Commit & Push

```bash
# Commit with descriptive message
git commit -m "🎨 Generate animated profile assets

- Create icon SVGs with animations
- Generate focus areas visualization
- Generate current goals visualization  
- Generate languages & tools showcase
- Generate GitHub statistics dashboard"

# Push to main branch
git push origin main
```

## Verify on GitHub

1. Go to https://github.com/Atharv-725
2. Your profile README should now display the generated SVGs
3. If images don't load:
   - Check file paths are correct in README.md
   - Verify assets are committed and visible in the repository
   - Wait a few minutes for GitHub to refresh cache

## Regular Updates

### Weekly Update
```bash
python build.py
git add assets/
git commit -m "📊 Update profile assets" 
git push origin main
```

### When You Want to Change Content
1. Edit `scripts/generate_profile_assets.py` or other generators
2. Run `python build.py`
3. Commit and push

## Troubleshooting

### Assets Not Showing on GitHub
- Wait 5-10 minutes for cache refresh
- Try viewing in incognito/private mode
- Check image URLs are relative paths like `assets/filename.svg`

### Build Fails
- Ensure Python 3.6+
- Check internet connection for API calls
- Verify no special characters in file paths

### Stats Show Old Data
- GitHub caches stats for 1 hour
- Delete local `github_stats.svg` and rebuild
- Set `GITHUB_TOKEN` environment variable

## File Paths for README

Use these relative paths in your README.md:

```markdown
![Icons](assets/icons/about_me.svg)
![Focus Areas](assets/focus_areas.svg)
![Current Goals](assets/current_goals.svg)
![Languages & Tools](assets/languages_tools.svg)
![GitHub Stats](assets/github_stats.svg)
```

## Success Indicators

✅ All SVG files exist in `assets/`
✅ Build completes without errors
✅ GitHub actions (if configured) pass
✅ SVG files display in GitHub's web interface
✅ Links in README work correctly

---

You're all set! Your GitHub profile is now ready to showcase. 🚀
