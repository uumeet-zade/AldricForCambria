import re

files = ['index.html', 'platform.html', 'events.html', 'candidates.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the link tag for style.css and add a query param
    content = re.sub(r'href="assets/css/style\.css"', 'href="assets/css/style.css?v=2.0"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cache bust applied.")
