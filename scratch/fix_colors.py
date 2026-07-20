import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the original :root
original_root_pattern = r'(:root\s*\{)([^}]*)(\})'
def root_replacer(match):
    inner = match.group(2)
    # Ensure we keep Rose Red and add the new vars
    new_vars = """
      --primary-glow: rgba(215, 0, 58, 0.2);
      --dark-obsidian: #0B0C10;
      --bg-dark-surface: #1F2833;
      --glass-bg: rgba(255, 255, 255, 0.7);
      --glass-border: rgba(255, 255, 255, 0.8);
      --radius-xl: 24px;
      --hero-text: var(--text-main);
      --bento-gradient: linear-gradient(135deg, rgba(215, 0, 58, 0.05) 0%, rgba(255,255,255,0.5) 100%);
"""
    return match.group(1) + inner.rstrip() + new_vars + match.group(3)

content = re.sub(original_root_pattern, root_replacer, content, count=1)

# 2. Update the original html.dark-theme (around line 1130)
dark_theme_pattern = r'(/\*\s*DARK THEME\s*\*/\s*html\.dark-theme\s*\{)([^}]*)(\})'
def dark_theme_replacer(match):
    new_vars = """
      --text-main: #F3F4F6;
      --text-muted: #9CA3AF;
      --bg-body: var(--dark-obsidian);
      --bg-surface: var(--bg-dark-surface);
      --border-color: rgba(255,255,255,0.08);
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 20px rgba(0,0,0,0.4);
      --shadow-hover: 0 10px 30px rgba(0,0,0,0.5);
      --glass-bg: rgba(255, 255, 255, 0.08);
      --glass-border: rgba(255, 255, 255, 0.15);
      --primary-glow: rgba(215, 0, 58, 0.4);
      --hero-text: #ffffff;
      --bento-gradient: linear-gradient(135deg, rgba(215, 0, 58, 0.1) 0%, rgba(0,0,0,0) 100%);
"""
    return match.group(1) + new_vars + match.group(3)

content = re.sub(dark_theme_pattern, dark_theme_replacer, content, count=1)

# 3. Remove the CAMBRIA PREMIUM OVERRIDES root and html.dark-theme blocks completely
overrides_pattern = r'/\*\s*CAMBRIA PREMIUM OVERRIDES\s*\*/\s*:root\s*\{[^}]*\}\s*html\.dark-theme\s*\{[^}]*\}'
content = re.sub(overrides_pattern, '/* CAMBRIA PREMIUM OVERRIDES STRIPPED FOR COLOR CONSISTENCY */', content, count=1)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors fixed successfully.")
