import re

with open('candidates.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will just remove the specific data-i18n tags on Mandy's card and Isolde's card
# Actually, the constituency parliament and party list cards don't have data-i18n tags in my python script!
# Only the executive section did because I copied it from the html_exec string.

content = content.replace(' data-i18n="role-pres"', '')
content = content.replace(' data-i18n="const-nat"', '')
content = content.replace(' data-i18n="bio-pres"', '')
content = content.replace(' data-i18n="role-gov"', '')
content = content.replace(' data-i18n="const-gov"', '')
content = content.replace(' data-i18n="bio-gov"', '')

with open('candidates.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Stripped i18n tags")
