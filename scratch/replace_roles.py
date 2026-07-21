import re

replacements = {
    # French
    r'"ld-role-chair": "Présidente"': r'"ld-role-chair": "Présidente du Parti"',
    r'"ld-role-deputy": "Vice-Président"': r'"ld-role-deputy": "Vice-Président du Parti"',
    r'"ld-role-chief": "Chef de Cabinet"': r'"ld-role-chief": "Chef de Cabinet du Parti"',

    # Spanish
    r'"ld-role-chair": "Presidenta"': r'"ld-role-chair": "Presidenta del Partido"',
    r'"ld-role-deputy": "Vicepresidente"': r'"ld-role-deputy": "Vicepresidente del Partido"',
    r'"ld-role-chief": "Jefe de Gabinete"': r'"ld-role-chief": "Jefe de Gabinete del Partido"',

    # Danish
    r'"ld-role-chair": "Forkvinde"': r'"ld-role-chair": "Partiforkvinde"',
    r'"ld-role-deputy": "Næstformand"': r'"ld-role-deputy": "Næstformand for Partiet"',
    # Danish Stabschef will be handled below to distinguish from German

    # Welsh
    r'"ld-role-chair": "Cadeirydd"': r'"ld-role-chair": "Cadeiryddes y Blaid"',
    r'"ld-role-deputy": "Dirprwy Gadeirydd"': r'"ld-role-deputy": "Dirprwy Gadeirydd y Blaid"',
    r'"ld-role-chief": "Pennaeth Staff"': r'"ld-role-chief": "Pennaeth Staff y Blaid"',

    # Latvian
    r'"ld-role-chair": "Priekšsēdētāja"': r'"ld-role-chair": "Partijas Priekšsēdētāja"',
    r'"ld-role-deputy": "Priekšsēdētāja Vietnieks"': r'"ld-role-deputy": "Partijas Priekšsēdētāja Vietnieks"',
    r'"ld-role-chief": "Personāla Vadītājs"': r'"ld-role-chief": "Partijas Personāla Vadītājs"',

    # German
    r'"ld-role-chair": "Vorsitzende"': r'"ld-role-chair": "Parteivorsitzende"',
    r'"ld-role-deputy": "Stellvertretender Vorsitzender"': r'"ld-role-deputy": "Stellvertretender Parteivorsitzender"',
}

with open('scripts/manual_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = re.sub(old, new, content)

# Danish and German share "Stabschef" as the translation.
# Danish is before German in the file, let's just do a manual replace by counting.
# Or better, we can replace the first occurrence (Danish) and then the second (German)
stabschefs = list(re.finditer(r'"ld-role-chief": "Stabschef"', content))
if len(stabschefs) == 2:
    # Danish
    content = content[:stabschefs[0].start()] + '"ld-role-chief": "Partiets Stabschef"' + content[stabschefs[0].end():]
    # Recalculate second index due to string length change
    stabschefs = list(re.finditer(r'"ld-role-chief": "Stabschef"', content))
    # German
    content = content[:stabschefs[0].start()] + '"ld-role-chief": "Parteistabschef"' + content[stabschefs[0].end():]

with open('scripts/manual_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Roles updated.")
