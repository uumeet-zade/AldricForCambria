import re

files = ['index.html', 'platform.html', 'events.html', 'candidates.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match any version of the style.css link and replace it with v=3.0
    content = re.sub(r'href="assets/css/style\.css(\?[^"]+)?"', 'href="assets/css/style.css?v=3.0"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Forced cache bust applied.")
