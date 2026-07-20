import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Strip the .rose-scatter rules completely
css = re.sub(r'/\*\s*ROSE SCATTER WATERMARKS\s*\*/.*?(?=\/\*\s*Modal Styles)', '', css, flags=re.DOTALL)

# 2. Strip bento-gradient from root and html.dark-theme
css = re.sub(r'--bento-gradient:[^;]+;\n', '', css)
css = css.replace('background: var(--bento-gradient);', 'background: transparent;')

# 3. Fix typography: explicit Playfair Display for headings
css = css.replace("font-family: 'Outfit', 'Playfair Display', sans-serif;", "font-family: 'Playfair Display', serif;")

# 4. Clean up the Crisis Banner (make it a sleek dark surface)
crisis_banner_pattern = r'(\.crisis-banner\s*\{[^}]+background:\s*)linear-gradient\([^)]+\)([^}]+)\}'
def crisis_replacer(m):
    return m.group(1) + 'var(--bg-dark-surface)' + m.group(2) + '}'
css = re.sub(crisis_banner_pattern, crisis_replacer, css)

# Remove the noise filter pseudoelement
css = re.sub(r'\.crisis-banner::after\s*\{[^}]+\}', '', css)

# 5. Simplify the Glassmorphism on cards and pillars to a diffuse shadow
# Remove the white 2px border injection pseudoelement from .pillar::before and .news-card::before
css = re.sub(r'\.pillar::before, \.news-card::before\s*\{[^}]+\}', '', css)
css = re.sub(r'\.pillar:hover::before, \.news-card:hover::before\s*\{[^}]+\}', '', css)

# Adjust shadows on hover
css = css.replace('box-shadow: 0 20px 40px var(--primary-glow);', 'box-shadow: 0 15px 40px rgba(0,0,0,0.08);')

# 6. Simplify the hero section
css = re.sub(r'(\.hero\s*\{[^\}]+)background:\s*linear-gradient[^;]+;', r'\1background: transparent;', css)
css = re.sub(r'(\.hero\s*\{[^\}]+)border:\s*1px solid var\(--glass-border\);', r'\1border: none;', css)
css = re.sub(r'(\.hero\s*\{[^\}]+)box-shadow:[^;]+;', r'\1box-shadow: none;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Minimalist CSS modifications applied.")
