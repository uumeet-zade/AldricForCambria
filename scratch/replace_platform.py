with open('platform.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("Cambrian", "National")
content = content.replace("Cambria", "the Republic")
content = content.replace("- Aldric von Reichel", "- The SDA")
content = content.replace("The the Republic Platform", "The Party Platform")
content = content.replace("the Republicn R&D Center", "National R&D Center")

with open('platform.html', 'w', encoding='utf-8') as f:
    f.write(content)
