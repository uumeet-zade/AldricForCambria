import re
import os

nav_template = """  <nav>
    <a href="index.html" class="nav-brand" style="text-decoration: none; color: inherit;">
      <img class="nav-logo logo-light" src="assets/images/SDAlogo.svg" alt="Social Democratic Alliance Logo" />
      <img class="nav-logo logo-dark" src="assets/images/SDAlogo-dark.svg" alt="Social Democratic Alliance Logo" />
      <span class="nav-name" data-i18n="nav-name">Social Democratic Alliance</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html"{home_active} data-i18n="nav-home">Home</a></li>
      <li><a href="platform.html"{plat_active} data-i18n="nav-platform">Platform</a></li>
      <li><a href="events.html"{ev_active} data-i18n="nav-campaigning">Campaigning</a></li>
      <li><a href="candidates.html"{cand_active} data-i18n="nav-candidates">Candidates</a></li>
      <li class="lang-switcher">
        <button class="lang-toggle" aria-label="Change Language">
          <span class="lang-current">AL</span>
        </button>
        <div class="lang-dropdown">
          <button class="lang-option active" data-lang="al">Alanian</button>
          <button class="lang-option" data-lang="ga">Gallic</button>
          <button class="lang-option" data-lang="ac">Alcamerian</button>
          <button class="lang-option" data-lang="ra">Rälandic</button>
          <button class="lang-option" data-lang="my">Myrati</button>
          <button class="lang-option" data-lang="au">Austrumish</button>
          <button class="lang-option" data-lang="le">Leislandic</button>
        </div>
      </li>
      <li><a href="#" class="theme-toggle" onclick="toggleTheme(event)" title="Toggle Night Mode">🌗</a></li>
    </ul>
  </nav>"""

files = ['index.html', 'platform.html', 'events.html', 'candidates.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    home_a = ' class="active"' if file == 'index.html' else ''
    plat_a = ' class="active"' if file == 'platform.html' else ''
    ev_a = ' class="active"' if file == 'events.html' else ''
    cand_a = ' class="active"' if file == 'candidates.html' else ''

    nav_rendered = nav_template.format(
        home_active=home_a,
        plat_active=plat_a,
        ev_active=ev_a,
        cand_active=cand_a
    )
    
    # replace everything between <nav> and </nav> including the tags
    content = re.sub(r'<nav>.*?</nav>', nav_rendered, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Standardized navigation and language switcher.")
