import re

files = ['index.html', 'platform.html', 'events.html', 'candidates.html']
allowed_tags = [
    'nav-name', 'nav-brand-name', 'nav-home', 'nav-platform', 'nav-campaigning', 'nav-candidates',
    'footer-name', 'footer-motto', 'footer-copy',
    'filter-all-cand', 'filter-exec', 'filter-house', 'filter-list', 'cand-meet-btn'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        tag = match.group(1)
        if tag in allowed_tags:
            return match.group(0) # keep it
        return '' # strip it

    content = re.sub(r'\s*data-i18n="([^"]+)"', replacer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Stripped unwanted i18n tags.")
