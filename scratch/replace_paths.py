import os
import glob

html_files = glob.glob('*.html')

replacements = {
    'href="style.css"': 'href="assets/css/style.css"',
    'src="translations.js': 'src="assets/js/translations.js',
    'href="favicon.png"': 'href="assets/images/favicon.png"',
    'src="SDAlogo.svg"': 'src="assets/images/SDAlogo.svg"',
    'src="SDAlogo-dark.svg"': 'src="assets/images/SDAlogo-dark.svg"',
    'AldricvonReichelPortraitNoBG.png': 'assets/images/AldricvonReichelPortraitNoBG.png',
    '/link_preview.png': '/assets/images/link_preview.png'
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated paths in HTML files.")
