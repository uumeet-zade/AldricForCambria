import re

files = ['index.html', 'platform.html', 'events.html', 'candidates.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match font-family: 'Outfit', sans-serif; with any spacing/quotes
    content = re.sub(r'font-family:\s*[\'"]?Outfit[\'"]?\s*,\s*sans-serif\s*;?', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Stripped inline Outfit fonts.")
