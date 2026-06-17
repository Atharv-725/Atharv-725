import os

def create_icons(assets_dir):
    icons_dir = os.path.join(assets_dir, "icons")
    os.makedirs(icons_dir, exist_ok=True)
    
    # 1. about_me.svg - Bouncing location pin
    about_me_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
    <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }
        .pin {
            fill: #BF91F3;
            animation: bounce 2s ease-in-out infinite;
            transform-origin: center;
        }
        .shadow {
            fill: #2F3147;
            opacity: 0.6;
            animation: pulse-shadow 2s ease-in-out infinite;
            transform-origin: center;
        }
        @keyframes pulse-shadow {
            0%, 100% { transform: scale(1); opacity: 0.6; }
            50% { transform: scale(0.8); opacity: 0.3; }
        }
    </style>
    <ellipse class="shadow" cx="12" cy="20" rx="5" ry="1.5" />
    <path class="pin" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
</svg>
"""
    with open(os.path.join(icons_dir, "about_me.svg"), "w", encoding="utf-8") as f:
        f.write(about_me_svg)

    # 2. focus_areas.svg - Brain with pulsing neural nodes
    focus_areas_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
    <style>
        .brain {
            fill: none;
            stroke: #70A5FD;
            stroke-width: 1.5;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .node {
            fill: #38BDAE;
            animation: pulse-node 1.5s ease-in-out infinite;
        }
        .node-2 {
            fill: #BF91F3;
            animation: pulse-node 1.5s ease-in-out infinite;
            animation-delay: 0.75s;
        }
        @keyframes pulse-node {
            0%, 100% { r: 1.5; opacity: 0.4; }
            50% { r: 2.5; opacity: 1; }
        }
    </style>
    <path class="brain" d="M12 5a3.5 3.5 0 0 0-3.5 3.5c0 .77.25 1.48.67 2.06A3.5 3.5 0 0 0 7 14c0 1.93 1.57 3.5 3.5 3.5.34 0 .67-.05 1-.14V19a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1.64c.33.09.66.14 1 .14 1.93 0 3.5-1.57 3.5-3.5a3.5 3.5 0 0 0-2.17-3.44c.42-.58.67-1.29.67-2.06A3.5 3.5 0 0 0 12 5z"/>
    <path class="brain" d="M12 5v12.5"/>
    <circle class="node" cx="9" cy="8" r="2" />
    <circle class="node-2" cx="15" cy="9" r="2" />
    <circle class="node" cx="8" cy="13" r="2" />
    <circle class="node-2" cx="16" cy="13" r="2" />
</svg>
"""
    with open(os.path.join(icons_dir, "focus_areas.svg"), "w", encoding="utf-8") as f:
        f.write(focus_areas_svg)

    # 3. current_goals.svg - Sonar target
    current_goals_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
    <style>
        .radar-line {
            stroke: #FF9E64;
            stroke-width: 1.5;
            stroke-linecap: round;
            transform-origin: 12px 12px;
            animation: rotate 4s linear infinite;
        }
        .radar-ring {
            fill: none;
            stroke: #2F3147;
            stroke-width: 1;
        }
        .radar-ring-active {
            fill: none;
            stroke: #FF9E64;
            stroke-width: 1;
            opacity: 0.3;
            animation: pulse-ring 2s ease-out infinite;
            transform-origin: 12px 12px;
        }
        .bullseye {
            fill: #FF9E64;
        }
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.5); opacity: 0.8; }
            100% { transform: scale(1.2); opacity: 0; }
        }
    </style>
    <circle class="radar-ring" cx="12" cy="12" r="10" />
    <circle class="radar-ring" cx="12" cy="12" r="6" />
    <circle class="radar-ring-active" cx="12" cy="12" r="8" />
    <line class="radar-line" x1="12" y1="12" x2="12" y2="2" />
    <circle class="bullseye" cx="12" cy="12" r="2" />
</svg>
"""
    with open(os.path.join(icons_dir, "current_goals.svg"), "w", encoding="utf-8") as f:
        f.write(current_goals_svg)

    # 4. featured_projects.svg - Rocket ship
    featured_projects_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
    <style>
        .rocket {
            fill: #38BDAE;
        }
        .flame {
            fill: #FF9E64;
            transform-origin: 6px 18px;
            animation: flicker 0.15s ease-in-out infinite alternate;
        }
        @keyframes flicker {
            0% { transform: scale(0.8) translate(0.5px, -0.5px); opacity: 0.7; }
            100% { transform: scale(1.2) translate(-0.5px, 0.5px); opacity: 1; }
        }
    </style>
    <path class="flame" d="M6 18c-1 2-3 3-4 5 2-1 3-3 5-4z"/>
    <path class="rocket" d="M12 2s3 2 3 7c0 2-1 4-2 5l4 4a1 1 0 0 1-1.4 1.4l-4-4c-1 1-3 2-5 2-5 0-7-3-7-3s2-1 2-4V9c0-5 3-7 3-7zm-3 8a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
</svg>
"""
    with open(os.path.join(icons_dir, "featured_projects.svg"), "w", encoding="utf-8") as f:
        f.write(featured_projects_svg)

    # 5. achievements.svg - Trophy
    achievements_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
    <style>
        .trophy {
            fill: #FFD43B;
        }
        .sparkle {
            fill: #ffffff;
            animation: flash 1.2s ease-in-out infinite alternate;
        }
        .sparkle-2 {
            fill: #ffffff;
            animation: flash 1.2s ease-in-out infinite alternate;
            animation-delay: 0.6s;
        }
        @keyframes flash {
            0% { opacity: 0.1; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1.2); }
        }
    </style>
    <path class="trophy" d="M19 5h-2V3H7v2H5c-1.1 0-2 .9-2 2v3c0 2.44 1.72 4.48 4 4.9V17c0 1.1.9 2 2 2h2v2H9v2h6v-2h-3v-2h2c1.1 0 2-.9 2-2v-2.1c2.28-.42 4-2.46 4-4.9V7c0-1.1-.9-2-2-2zM5 10V7h2v3H5zm14 0h-2V7h2v3z"/>
    <path class="sparkle" d="M7 2.5l.8 1.2 1.2.8-1.2.8-.8 1.2-.8-1.2-1.2-.8 1.2-.8zm11 15l.5.8.8.5-.8.5-.5.8-.5-.8-.8-.5.8-.5z" />
    <path class="sparkle-2" d="M17 1.5l.5.8.8.5-.8.5-.5.8-.5-.8-.8-.5.8-.5z" />
</svg>
"""
    with open(os.path.join(icons_dir, "achievements.svg"), "w", encoding="utf-8") as f:
        f.write(achievements_svg)

    # 6. bullet_project.svg - Terminal bracket coding bullet
    bullet_project_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18">
    <style>
        .bracket {
            fill: none;
            stroke: #70A5FD;
            stroke-width: 2.5;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .slash {
            fill: none;
            stroke: #38BDAE;
            stroke-width: 2;
            stroke-linecap: round;
            animation: blink 1.2s step-end infinite;
        }
        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
    <path class="bracket" d="M8 17l-5-5 5-5" />
    <line class="slash" x1="14" y1="5" x2="10" y2="19" />
    <path class="bracket" d="M16 7l5 5-5 5" />
</svg>
"""
    with open(os.path.join(icons_dir, "bullet_project.svg"), "w", encoding="utf-8") as f:
        f.write(bullet_project_svg)

    # 7. bullet_achievement.svg - Pulsing gear/medal
    bullet_achievement_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18">
    <style>
        .outer {
            fill: none;
            stroke: #BF91F3;
            stroke-width: 2;
            transform-origin: center;
            animation: spin 8s linear infinite;
        }
        .inner {
            fill: #38BDAE;
            animation: pulse-inner 1.8s ease-in-out infinite;
            transform-origin: center;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        @keyframes pulse-inner {
            0%, 100% { transform: scale(0.8); opacity: 0.6; }
            50% { transform: scale(1.1); opacity: 1; }
        }
    </style>
    <path class="outer" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z" stroke-dasharray="4,3" />
    <polygon class="inner" points="12,7 15,10 13,10 13,17 11,17 11,10 9,10" transform="translate(0, -1)" />
    <circle class="inner" cx="12" cy="12" r="3" />
</svg>
"""
    with open(os.path.join(icons_dir, "bullet_achievement.svg"), "w", encoding="utf-8") as f:
        f.write(bullet_achievement_svg)

def create_focus_areas_svg(assets_dir):
    output_path = os.path.join(assets_dir, "focus_areas.svg")
    
    width = 560
    height = 135
    
    pills = [
        {"title": "Full Stack Dev", "icon": "M2 4h20v12H2zm10 16h2v-4h-2zm-6 0h12v-1h-12z", "color": "#70A5FD", "col": 0, "row": 0},
        {"title": "Large Language Models", "icon": "M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM9 11H7V9h2v2zm4 0h-2V9h2v2zm4 0h-2V9h2v2z", "color": "#38BDAE", "col": 1, "row": 0},
        {"title": "Advanced Backend", "icon": "M19 12H5V5h14zm0-9H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z", "color": "#FF9E64", "col": 2, "row": 0},
        {"title": "Machine Learning", "icon": "M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 19.4c-.39.39-.39 1.02 0 1.41.39.39 1.02.39 1.41 0l1.9-1.9C9.07 19.58 10.49 20 12 20c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 15c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z", "color": "#BF91F3", "col": 0, "row": 1},
        {"title": "Java Programming", "icon": "M12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10-4.48-10-10-10zm-1 15.5v-3.5H9v-1h2v-3H9v-1h2v-2.5h2V6.5h2v1h-2v3h2v1h-2v3h2v1h-2v3.5h-2z", "color": "#FFD43B", "col": 1, "row": 1},
        {"title": "DSA &amp; Algorithms", "icon": "M19 15c-1.2 0-2.28-.56-3-1.43L9.4 17.5c.37.73.6 1.55.6 2.5 0 2.76-2.24 5-5 5s-5-2.24-5-5 2.24-5 5-5c1.2 0 2.28.56 3 1.43l6.6-3.93c-.37-.73-.6-1.55-.6-2.5 0-2.76 2.24-5 5-5s5 2.24 5 5-2.24 5-5 5z", "color": "#9013FE", "col": 2, "row": 1}
    ]
    
    pills_svg = []
    float_idx = 1
    
    col_w = 166
    gap_x = 18
    start_x = 20
    
    row_h = 36
    gap_y = 12
    start_y = 20
    
    for p in pills:
        x = start_x + p["col"] * (col_w + gap_x)
        y = start_y + p["row"] * (row_h + gap_y)
        
        pills_svg.append(f"""
    <g class="float-{float_idx}">
        <!-- Glassmorphic Card Pill -->
        <rect x="{x}" y="{y}" width="{col_w}" height="{row_h}" class="pill-bg" rx="18" stroke="{p['color']}" stroke-width="1.2" />
        <!-- Tech Icon -->
        <g transform="translate({x + 10}, {y + 8}) scale(0.85)">
            <path d="{p['icon']}" fill="{p['color']}" />
        </g>
        <!-- Title Text -->
        <text x="{x + 36}" y="{y + 22}" class="pill-text" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11px" font-weight="600">{p['title']}</text>
    </g>""")
        float_idx = (float_idx % 6) + 1
        
    svg_body = "\n".join(pills_svg)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}px" height="{height}px" viewBox="0 0 {width} {height}" direction="ltr">
    <style>
        @keyframes float-keyframes-1 {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-3px); }}
            100% {{ transform: translateY(0px); }}
        }}
        @keyframes float-keyframes-2 {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-2px); }}
            100% {{ transform: translateY(0px); }}
        }}
        @keyframes float-keyframes-3 {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-2.5px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .float-1 {{ animation: float-keyframes-1 3s ease-in-out infinite; }}
        .float-2 {{ animation: float-keyframes-2 3.6s ease-in-out infinite; animation-delay: 0.3s; }}
        .float-3 {{ animation: float-keyframes-3 4.2s ease-in-out infinite; animation-delay: 0.6s; }}
        .float-4 {{ animation: float-keyframes-1 3.3s ease-in-out infinite; animation-delay: 0.9s; }}
        .float-5 {{ animation: float-keyframes-2 3.9s ease-in-out infinite; animation-delay: 1.2s; }}
        .float-6 {{ animation: float-keyframes-3 4.5s ease-in-out infinite; animation-delay: 1.5s; }}
        
        .card-border {{
            stroke: #2F3147;
            stroke-width: 1.5;
            fill: #1A1B27;
            rx: 10px;
        }}
        .pill-bg {{
            fill: #1F2335;
            transition: all 0.3s ease;
        }}
        .pill-bg:hover {{
            fill: #24283B;
            filter: drop-shadow(0 0 5px rgba(112, 165, 253, 0.3));
        }}
        .pill-text {{
            fill: #A9B1D6;
        }}
    </style>
    <rect class="card-border" width="{width - 2}" height="{height - 2}" x="1" y="1" />
{svg_body}
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Successfully generated focus_areas SVG at {output_path}")

def create_current_goals_svg(assets_dir):
    output_path = os.path.join(assets_dir, "current_goals.svg")
    
    width = 560
    height = 95
    
    goals = [
        {"title": "Mastering DSA &amp; Algorithms", "desc": "Structured Problem Solving", "color": "#70A5FD", "col": 0, "row": 0},
        {"title": "Production-Level AI Apps", "desc": "LLMs &amp; Smart Agentic Coding", "color": "#38BDAE", "col": 1, "row": 0},
        {"title": "Open Source Contributions", "desc": "Collaborating with Communities", "color": "#BF91F3", "col": 0, "row": 1},
        {"title": "High-Impact Software Eng.", "desc": "Advanced System Architectures", "color": "#FF9E64", "col": 1, "row": 1}
    ]
    
    goals_svg = []
    col_w = 250
    gap_x = 20
    start_x = 20
    
    row_h = 24
    gap_y = 12
    start_y = 18
    
    for g in goals:
        x = start_x + g["col"] * (col_w + gap_x)
        y = start_y + g["row"] * (row_h + gap_y)
        
        goals_svg.append(f"""
    <g>
        <!-- Target Pulsing Radar Dot -->
        <circle cx="{x + 8}" cy="{y + 10}" r="4" fill="{g['color']}" />
        <circle cx="{x + 8}" cy="{y + 10}" r="8" fill="none" stroke="{g['color']}" stroke-width="1.2">
            <animate attributeName="r" values="4;10;4" dur="2.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;0;1" dur="2.5s" repeatCount="indefinite" />
        </circle>
        
        <!-- Goal Text -->
        <text x="{x + 24}" y="{y + 10}" fill="#A9B1D6" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12px" font-weight="700">{g['title']}</text>
        <text x="{x + 24}" y="{y + 22}" fill="#565F89" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5px">{g['desc']}</text>
    </g>""")
        
    svg_body = "\n".join(goals_svg)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}px" height="{height}px" viewBox="0 0 {width} {height}" direction="ltr">
    <style>
        .card-border {{
            stroke: #2F3147;
            stroke-width: 1.5;
            fill: #1A1B27;
            rx: 10px;
        }}
    </style>
    <rect class="card-border" width="{width - 2}" height="{height - 2}" x="1" y="1" />
{svg_body}
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Successfully generated current_goals SVG at {output_path}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(script_dir)
    assets_dir = os.path.join(workspace_dir, "assets")
    
    print("Generating animated icons...")
    create_icons(assets_dir)
    
    print("Generating focus_areas.svg...")
    create_focus_areas_svg(assets_dir)
    
    print("Generating current_goals.svg...")
    create_current_goals_svg(assets_dir)
    
    print("All profile assets generated successfully!")

if __name__ == "__main__":
    main()
