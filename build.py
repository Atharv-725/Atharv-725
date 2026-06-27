#!/usr/bin/env python3
"""
GitHub Profile Build Script
Generates all dynamic assets for the profile README
"""

import sys
import os
import importlib.util

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def load_script(script_path):
    """Load a Python script as a module"""
    spec = importlib.util.spec_from_file_location("module", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(script_dir, "scripts")
    
    print("=" * 60)
    print("GitHub Profile Asset Builder")
    print("=" * 60)
    print()
    
    # Step 1: Generate Profile Icons
    print("[1/3] Generating animated icons...")
    try:
        profile_assets = load_script(os.path.join(scripts_dir, "generate_profile_assets.py"))
        profile_assets.main()
        print("✓ Profile icons generated successfully!\n")
    except Exception as e:
        print(f"✗ Error generating profile assets: {e}\n")
        return 1
    
    # Step 2: Generate Languages & Tools SVG
    print("[2/3] Generating languages & tools visualization...")
    try:
        tools = load_script(os.path.join(scripts_dir, "generate_tools.py"))
        tools.generate_svg()
        print("✓ Languages & tools visualization generated!\n")
    except Exception as e:
        print(f"✗ Error generating tools SVG: {e}\n")
        return 1
    
    # Step 3: Generate GitHub Stats SVG
    print("[3/3] Generating GitHub statistics...")
    try:
        stats = load_script(os.path.join(scripts_dir, "generate_stats.py"))
        stats.main()
        print("✓ GitHub statistics SVG generated!\n")
    except Exception as e:
        print(f"⚠ Warning generating stats (may require GitHub token for full data): {e}")
        print("  Note: You can set GITHUB_TOKEN environment variable for better results.\n")
    
    print("=" * 60)
    print("✓ Build Complete!")
    print("=" * 60)
    print("\nGenerated assets:")
    assets_dir = os.path.join(script_dir, "assets")
    if os.path.exists(assets_dir):
        print(f"  📂 {assets_dir}/")
        for item in os.listdir(assets_dir):
            item_path = os.path.join(assets_dir, item)
            if os.path.isdir(item_path):
                print(f"    📁 {item}/")
                for file in os.listdir(item_path):
                    print(f"       ✓ {file}")
            else:
                print(f"    ✓ {item}")
    
    print("\nNext steps:")
    print("  1. Review the generated SVG files in the assets/ folder")
    print("  2. Commit your changes: git add assets/")
    print("  3. Commit: git commit -m 'Generate profile assets'")
    print("  4. Push to main: git push origin main")
    print("\nYour GitHub profile README will now display these dynamic assets!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
