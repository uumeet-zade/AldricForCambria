import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove borders from cards and replace with diffuse shadows
css = css.replace('border: 1px solid var(--border-color);', 'border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.02);')

# Increase hover shadows for minimalism
css = css.replace('box-shadow: var(--shadow-hover);', 'box-shadow: 0 15px 40px rgba(0,0,0,0.06);')

# Make candidate-card and featured-candidate card cleaner
css = css.replace('.candidate-card::before {\n      content: \'\';\n      position: absolute;\n      top: 0;\n      left: 0;\n      right: 0;\n      height: 4px;\n      background: var(--border-color);\n      transition: var(--transition);\n    }', '')
css = css.replace('.candidate-card:hover::before {\n      background: var(--primary);\n    }', '')

# Ensure Playfair Display is explicitly used everywhere necessary
css = css.replace("font-family: 'Outfit', sans-serif;", "font-family: 'Playfair Display', serif;")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Card minimalism applied.")
