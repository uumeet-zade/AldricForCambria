import os
from bs4 import BeautifulSoup

html_files = ["index.html", "platform.html", "events.html", "candidates.html"]

for filename in html_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    for el in soup.find_all(attrs={"data-i18n": True}):
        # Check if any child also has data-i18n
        for child in el.find_all(attrs={"data-i18n": True}):
            print(f"NESTED FOUND IN {filename}: Parent '{el['data-i18n']}', Child '{child['data-i18n']}'")
