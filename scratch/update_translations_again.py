import re

with open('scripts/manual_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new translations in the order they appear in the file:
# fr, es, da, cy, lv, de

new_roles = [
    # French (fr)
    {"chair": "Présidente", "deputy": "Vice-président", "chief": "Chef de cabinet"},
    # Spanish (es)
    {"chair": "Presidenta", "deputy": "Vicepresidente", "chief": "Jefe de gabinete"},
    # Danish (da)
    {"chair": "Formand", "deputy": "Viceformand", "chief": "Kabinetschef"},
    # Welsh (cy)
    {"chair": "Cadeirydd", "deputy": "Is-gadeirydd", "chief": "Prif Swyddog Staff"},
    # Latvian (lv)
    {"chair": "Priekšsēdētāja", "deputy": "Priekšsēdētāja vietnieks", "chief": "Personāla vadītājs"},
    # German (de)
    {"chair": "Vorsitzende", "deputy": "Stellvertretender Vorsitzender", "chief": "Stabschef"}
]

# We will find all occurrences of the keys and replace them sequentially.
for key in ["ld-role-chair", "ld-role-deputy", "ld-role-chief"]:
    # Find all matches
    pattern = r'("' + key + r'":\s*")[^"]+(")'
    
    matches = list(re.finditer(pattern, content))
    
    if len(matches) != 6:
        print(f"Error: Found {len(matches)} matches for {key}, expected 6.")
        exit(1)
        
    # Replace in reverse order so string indices don't change
    for i in reversed(range(6)):
        match = matches[i]
        
        if key == "ld-role-chair":
            replacement = new_roles[i]["chair"]
        elif key == "ld-role-deputy":
            replacement = new_roles[i]["deputy"]
        elif key == "ld-role-chief":
            replacement = new_roles[i]["chief"]
            
        new_string = match.group(1) + replacement + match.group(2)
        content = content[:match.start()] + new_string + content[match.end():]

with open('scripts/manual_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations updated successfully.")
