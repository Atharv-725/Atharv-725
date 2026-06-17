import urllib.request
import re
import os
import sys
from datetime import datetime, timedelta, timezone

def get_stats(username):
    url = f"https://github-readme-stats-eight-theta.vercel.app/api?username={username}&count_private=true&include_all_commits=true&v={int(datetime.now().timestamp())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        
        texts = re.findall(r'<text[^>]*>([^<]+)</text>', content)
        texts_clean = [t.strip() for t in texts]
        
        stats = {
            "stars": "0",
            "commits": "0",
            "prs": "0",
            "issues": "0",
            "contributions": "0",
            "grade": "A+"
        }
        
        # Parse fields based on text layout
        try:
            if "Total Stars:" in texts_clean:
                idx = texts_clean.index("Total Stars:")
                stats["stars"] = texts_clean[idx + 1]
                if idx > 0:
                    stats["grade"] = texts_clean[idx - 1]
            if "Total Commits:" in texts_clean:
                idx = texts_clean.index("Total Commits:")
                stats["commits"] = texts_clean[idx + 1]
            if "Total PRs:" in texts_clean:
                idx = texts_clean.index("Total PRs:")
                stats["prs"] = texts_clean[idx + 1]
            if "Total Issues:" in texts_clean:
                idx = texts_clean.index("Total Issues:")
                stats["issues"] = texts_clean[idx + 1]
            if "Contributed to:" in texts_clean:
                idx = texts_clean.index("Contributed to:")
                stats["contributions"] = texts_clean[idx + 1]
        except Exception as e:
            print("Warning parsing stats lists:", e)
            
        return stats
    except Exception as e:
        print("Error fetching stats card:", e)
        return None

def get_streaks(username):
    contributions = {}
    # Fetch from 2023 to current year
    current_year = datetime.now().year
    years = list(range(2023, current_year + 1))
    
    for year in years:
        url = f"https://github.com/users/{username}/contributions?from={year}-01-01&to={year}-12-31"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
            
            # Extract id and data-date from class ContributionCalendar-day
            day_tags = re.findall(r'<td\s+[^>]*class="[^"]*ContributionCalendar-day[^"]*"[^>]*>', html)
            id_to_date = {}
            for tag in day_tags:
                date_match = re.search(r'data-date="([^"]+)"', tag)
                id_match = re.search(r'id="([^"]+)"', tag)
                if date_match and id_match:
                    id_to_date[id_match.group(1)] = date_match.group(1)
            
            tooltips = re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]+)</tool-tip>', html)
            for tid, t in tooltips:
                t_clean = t.strip()
                if tid not in id_to_date:
                    continue
                date_str = id_to_date[tid]
                
                count = 0
                if "No contributions" in t_clean:
                    count = 0
                else:
                    match = re.match(r'(\d+)\s+contribution', t_clean)
                    if match:
                        count = int(match.group(1))
                contributions[date_str] = count
        except Exception as e:
            print(f"Error fetching contributions for {year}:", e)
            
    if not contributions:
        return {
            "current_streak": 0,
            "current_start": "-",
            "current_end": "-",
            "longest_streak": 0,
            "longest_start": "-",
            "longest_end": "-"
        }
        
    sorted_dates = sorted(contributions.keys())
    
    # Calculate Longest Streak
    longest_streak = 0
    longest_streak_start = None
    longest_streak_end = None
    
    temp_streak = 0
    temp_start = None
    
    for date_str in sorted_dates:
        count = contributions[date_str]
        if count > 0:
            if temp_streak == 0:
                temp_start = date_str
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
                longest_streak_start = temp_start
                longest_streak_end = date_str
        else:
            temp_streak = 0
            
    # Calculate Current Streak in Asia/Kolkata timezone (UTC + 5.5 hours)
    kolkata_now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
    today_str = kolkata_now.strftime("%Y-%m-%d")
    yesterday_str = (kolkata_now - timedelta(days=1)).strftime("%Y-%m-%d")
    
    current_streak = 0
    current_start = None
    current_end = None
    
    active_dates = [d for d in sorted_dates if contributions.get(d, 0) > 0]
    if active_dates:
        last_active = active_dates[-1]
        last_active_dt = datetime.strptime(last_active, "%Y-%m-%d").date()
        today_dt = datetime.strptime(today_str, "%Y-%m-%d").date()
        
        # Streak remains active if the last active contribution day was today or yesterday
        if today_dt - last_active_dt <= timedelta(days=1):
            idx = sorted_dates.index(last_active)
            current_streak = 0
            current_end = last_active
            for i in range(idx, -1, -1):
                d = sorted_dates[i]
                if contributions.get(d, 0) > 0:
                    current_streak += 1
                    current_start = d
                else:
                    break
                    
    # Format dates
    def format_date(d_str):
        if not d_str or d_str == "-":
            return "-"
        try:
            dt = datetime.strptime(d_str, "%Y-%m-%d")
            return dt.strftime("%b %d")
        except:
            return d_str
            
    return {
        "current_streak": current_streak,
        "current_range": f"{format_date(current_start)} - {format_date(current_end)}" if current_streak > 0 else "No active streak",
        "longest_streak": longest_streak,
        "longest_range": f"{format_date(longest_streak_start)} - {format_date(longest_streak_end)}" if longest_streak > 0 else "No streak recorded"
    }

def get_languages(username):
    url = f"https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username={username}&langs_count=8&layout=compact&theme=tokyonight&border_radius=10&count_private=true&v={int(datetime.now().timestamp())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
        texts = re.findall(r'<text[^>]*>([^<]+)</text>', content)
        texts_clean = [t.strip() for t in texts]
        
        # Find all circles with fill attributes
        circles = re.findall(r'<circle[^>]*fill="([^"]+)"[^>]*>', content)
        
        langs = []
        lang_idx = 0
        for t in texts_clean:
            # Match JavaScript (39.21%)
            match = re.match(r'([^)]+) \(([^%]+)%\)', t)
            if match:
                name = match.group(1).strip()
                percentage = float(match.group(2).strip())
                color = "#858585" # fallback gray
                if lang_idx < len(circles):
                    color = circles[lang_idx]
                langs.append({
                    "name": name,
                    "percentage": percentage,
                    "color": color
                })
                lang_idx += 1
        return langs
    except Exception as e:
        print("Error fetching languages card:", e)
        return []

def generate_svg(stats, streak, langs, filepath):
    # Ensure dir exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    width = 560
    height = 550
    
    # Compute grade circle colors
    grade_color = "#70A5FD"
    if stats["grade"] == "A+":
        grade_color = "#BF91F3"
    elif stats["grade"].startswith("A"):
        grade_color = "#38BDAE"
    elif stats["grade"].startswith("B"):
        grade_color = "#FF9E64"
        
    # Build Lang Progress Bar segments
    bar_x = 30
    bar_y = 435
    bar_width = 500
    bar_height = 8
    bar_segments = []
    
    total_percentage = sum(l["percentage"] for l in langs)
    if total_percentage == 0:
        total_percentage = 1
        
    current_x = bar_x
    for i, lang in enumerate(langs):
        seg_w = (lang["percentage"] / total_percentage) * bar_width
        # Rounded corners for the very left and very right segments
        rx = 4 if i == 0 or i == len(langs) - 1 else 0
        bar_segments.append(
            f'<rect x="{current_x}" y="{bar_y}" width="{seg_w}" height="{bar_height}" fill="{lang["color"]}" />'
        )
        current_x += seg_w

    # Build Lang Legend grid
    legend_items = []
    grid_cols = 2
    col_width = 240
    start_x = 35
    start_y = 465
    row_height = 24
    
    for idx, lang in enumerate(langs):
        col = idx % grid_cols
        row = idx // grid_cols
        x = start_x + (col * col_width)
        y = start_y + (row * row_height)
        legend_items.append(f"""
        <g transform="translate({x}, {y})">
            <circle cx="5" cy="5" r="5" fill="{lang["color"]}" />
            <text x="18" y="9" fill="#A9B1D6" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-size="12px" font-weight="500">{lang["name"]}</text>
            <text x="180" y="9" fill="#565F89" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-size="12px" text-anchor="end">{lang["percentage"]}%</text>
        </g>
        """)
        
    legend_svg = "\n".join(legend_items)
    bar_svg = "\n".join(bar_segments)
    
    # Formulate whole SVG content
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}px" height="{height}px" viewBox="0 0 {width} {height}" direction="ltr">
    <style>
        @keyframes currstreak {{
            0% {{ font-size: 3px; opacity: 0.2; }}
            80% {{ font-size: 34px; opacity: 1; }}
            100% {{ font-size: 28px; opacity: 1; }}
        }}
        @keyframes fadein {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        .title {{
            fill: #BF91F3;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
            font-weight: 700;
            font-size: 18px;
        }}
        .stat-label {{
            fill: #70A5FD;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
            font-size: 14px;
            font-weight: 500;
        }}
        .stat-value {{
            fill: #38BDAE;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
            font-size: 14px;
            font-weight: 700;
        }}
        .card-border {{
            stroke: #2F3147;
            stroke-width: 1.5;
            fill: #1A1B27;
            rx: 10px;
        }}
    </style>
    
    <!-- Outer Card Background -->
    <rect class="card-border" width="{width - 2}" height="{height - 2}" x="1" y="1" />
    
    <!-- HEADER -->
    <g transform="translate(30, 45)">
        <!-- GitHub Stats Icon (Simplified Graph Icon) -->
        <path d="M 0 10 L 5 10 L 5 -5 L 0 -5 Z M 8 10 L 13 10 L 13 -15 L 8 -15 Z M 16 10 L 21 10 L 21 0 L 16 0 Z" fill="#BF91F3" stroke="none"/>
        <text x="32" y="8" class="title">My GitHub Statistics</text>
    </g>
    
    <!-- SECTION 1: Key Statistics -->
    <g transform="translate(30, 80)">
        <!-- Stats list -->
        <g transform="translate(0, 0)">
            <!-- Stars -->
            <g transform="translate(0, 10)">
                <text class="stat-label">Total Stars:</text>
                <text x="180" class="stat-value">{stats["stars"]}</text>
            </g>
            <!-- Commits -->
            <g transform="translate(0, 40)">
                <text class="stat-label">Total Commits:</text>
                <text x="180" class="stat-value">{stats["commits"]}</text>
            </g>
            <!-- PRs -->
            <g transform="translate(0, 70)">
                <text class="stat-label">Total PRs:</text>
                <text x="180" class="stat-value">{stats["prs"]}</text>
            </g>
            <!-- Issues -->
            <g transform="translate(0, 100)">
                <text class="stat-label">Total Issues:</text>
                <text x="180" class="stat-value">{stats["issues"]}</text>
            </g>
            <!-- Contributed to -->
            <g transform="translate(0, 130)">
                <text class="stat-label">Contributed to:</text>
                <text x="180" class="stat-value">{stats["contributions"]}</text>
            </g>
        </g>
        
        <!-- Right side: Grade Badge -->
        <g transform="translate(390, 45)">
            <!-- Circle border -->
            <circle cx="45" cy="45" r="45" fill="none" stroke="{grade_color}" stroke-width="4.5" style="opacity: 0.8; animation: fadein 0.5s linear forwards 0.3s" />
            <!-- Grade character -->
            <text x="45" y="56" fill="{grade_color}" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="800" font-size="34px" text-anchor="middle" style="animation: fadein 0.5s linear forwards 0.5s">
                {stats["grade"]}
            </text>
        </g>
    </g>
    
    <!-- Divider Line -->
    <line x1="30" y1="245" x2="530" y2="245" stroke="#2F3147" stroke-width="1.5" />
    
    <!-- SECTION 2: Streaks -->
    <g transform="translate(0, 250)">
        <!-- Current Streak -->
        <g transform="translate(140, 50)">
            <!-- Fire Icon -->
            <g transform="translate(-10, -50)" scale="0.9">
                <path d="M 1.5 0.67 C 1.5 0.67 2.24 3.32 2.24 5.47 C 2.24 7.53 0.89 9.2 -1.17 9.2 C -3.23 9.2 -4.79 7.53 -4.79 5.47 L -4.76 5.11 C -6.78 7.51 -8 10.62 -8 13.99 C -8 18.41 -4.42 22 0 22 C 4.42 22 8 18.41 8 13.99 C 8 8.6 5.41 3.79 1.5 0.67 Z M -0.29 19 C -2.07 19 -3.51 17.6 -3.51 15.86 C -3.51 14.24 -2.46 13.1 -0.7 12.74 C 1.07 12.38 2.9 11.53 3.92 10.16 C 4.31 11.45 4.51 12.81 4.51 14.2 C 4.51 16.85 2.36 19 -0.29 19 Z" fill="#FF9E64"/>
            </g>
            <!-- Number Circle -->
            <circle cx="0" cy="5" r="28" fill="none" stroke="#BF91F3" stroke-width="4.5" />
            <text x="0" y="15" fill="#BF91F3" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="700" font-size="28px" text-anchor="middle" style="animation: currstreak 0.6s linear forwards">
                {streak["current_streak"]}
            </text>
            
            <text x="0" y="55" fill="#BF91F3" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="700" font-size="14px" text-anchor="middle">Current Streak</text>
            <text x="0" y="75" fill="#38BDAE" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="400" font-size="12px" text-anchor="middle">{streak["current_range"]}</text>
        </g>
        
        <!-- Divider -->
        <line x1="280" y1="15" x2="280" y2="105" stroke="#2F3147" stroke-width="1.5" />
        
        <!-- Longest Streak -->
        <g transform="translate(420, 50)">
            <text x="0" y="15" fill="#70A5FD" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="700" font-size="28px" text-anchor="middle">
                {streak["longest_streak"]}
            </text>
            <text x="0" y="55" fill="#70A5FD" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="700" font-size="14px" text-anchor="middle">Longest Streak</text>
            <text x="0" y="75" fill="#38BDAE" stroke="none" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Ubuntu, sans-serif" font-weight="400" font-size="12px" text-anchor="middle">{streak["longest_range"]}</text>
        </g>
    </g>
    
    <!-- Divider Line -->
    <line x1="30" y1="375" x2="530" y2="375" stroke="#2F3147" stroke-width="1.5" />
    
    <!-- SECTION 3: Programming Languages -->
    <g transform="translate(0, 385)">
        <text x="30" y="25" class="title">My Programming Languages</text>
        
        <!-- Progress Bar Background (Rounded Track) -->
        <rect x="{bar_x}" y="{bar_y}" width="{bar_width}" height="{bar_height}" fill="#2F3147" rx="4" />
        
        <!-- Progress Bar Segments -->
        <g clip-path="url(#bar-clip)">
            {bar_svg}
        </g>
        
        <!-- Clip Path to round progress bar edges -->
        <clipPath id="bar-clip">
            <rect x="{bar_x}" y="{bar_y}" width="{bar_width}" height="{bar_height}" rx="4" />
        </clipPath>
        
        <!-- Legend Grid -->
        {legend_svg}
    </g>
</svg>
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"SVG saved to {filepath}")

def main():
    username = "nigampalash"
    print(f"Fetching GitHub stats for user: {username}")
    
    stats = get_stats(username)
    if not stats:
        print("Failed to fetch overall stats.")
        sys.exit(1)
        
    print("Stats fetched:", stats)
    
    print("Fetching streak information...")
    streak = get_streaks(username)
    print("Streaks calculated:", streak)
    
    print("Fetching programming languages...")
    langs = get_languages(username)
    print("Languages fetched:", len(langs))
    
    # Target SVG file
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "github_stats.svg")
    generate_svg(stats, streak, langs, output_path)
    print("Done!")

if __name__ == "__main__":
    main()
