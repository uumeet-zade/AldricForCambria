import re

with open('scripts/manual_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the lone commas by moving them to the end of the previous line
content = re.sub(r'([^,])\s*\n\s*,\n', r'\1,\n', content)
content = re.sub(r',\s*\n\s*,\n', r',\n', content)

# 2. Fix the broken end of the file
# The broken end looks like:
# print(f"  {code}: {len(d),
#     "idx-leadership-title": "Parteiführung",
# ...
# } translated keys")

# We want to extract the German leadership keys, which start at "idx-leadership-title" and end before } translated keys")
broken_tail_match = re.search(r'print\(f"\s*\{code\}:\s*\{len\(d\),\s*("idx-leadership-title".*?)\}\s*translated keys"\)', content, re.DOTALL)

if broken_tail_match:
    german_keys = broken_tail_match.group(1)
    
    # Remove the broken tail from the content
    content = content[:broken_tail_match.start()] + 'print(f"  {code}: {len(d)} translated keys")\n'
    
    # Insert the German keys into the `de` dictionary
    # Find where the `de` dictionary ends (before `# ===== BUILD FINAL DATA =====`)
    insert_pos = content.find('# ===== BUILD FINAL DATA =====')
    if insert_pos != -1:
        # Find the closing brace of the `de` dictionary just before insert_pos
        brace_pos = content.rfind('}', 0, insert_pos)
        if brace_pos != -1:
            # Check if the line before the brace needs a comma
            before_brace = content[:brace_pos].strip()
            if not before_brace.endswith(','):
                # We need to insert a comma
                content = content[:brace_pos] + ',\n' + german_keys + '\n' + content[brace_pos:]
            else:
                content = content[:brace_pos] + '\n' + german_keys + '\n' + content[brace_pos:]

with open('scripts/manual_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix applied.")
