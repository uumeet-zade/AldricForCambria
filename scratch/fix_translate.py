import os
import re

html_files = ["index.html", "platform.html", "events.html", "candidates.html"]

for filename in html_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace <html lang="en"> with <html lang="en" translate="no">
    content = re.sub(r'<html\s+lang="en"\s*>', '<html lang="en" translate="no">', content)
    
    # Add meta tag for google translation prevention if it doesn't exist
    if 'content="notranslate"' not in content:
        content = re.sub(r'(<meta charset="utf-8"/>)', r'\1\n<meta name="google" content="notranslate"/>', content)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added translate='no' to html tags and meta tags.")
