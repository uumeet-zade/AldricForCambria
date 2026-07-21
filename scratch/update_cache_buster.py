import os
import re

html_files = ["index.html", "platform.html", "events.html", "candidates.html"]

for filename in html_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace translations.js?v=X.X with translations.js?v=2.2
    content = re.sub(r'translations\.js\?v=\d+\.\d+', 'translations.js?v=2.2', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated cache buster to v=2.2 in all HTML files.")
