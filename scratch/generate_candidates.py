html_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Social Democratic Alliance - Candidates</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css">
  <script>
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme !== 'light') {
      document.documentElement.classList.add('dark-theme');
    }
  </script>
  <script src="assets/js/translations.js?v=1.2" defer></script>
  <link rel="icon" type="image/png" href="assets/images/favicon.png">
</head>
<body>
  <nav>
    <a href="index.html" class="nav-brand" style="text-decoration: none; color: inherit;">
      <img class="nav-logo logo-light" src="assets/images/SDAlogo.svg" alt="Social Democratic Alliance Logo" />
      <img class="nav-logo logo-dark" src="assets/images/SDAlogo-dark.svg" alt="Social Democratic Alliance Logo" />
      <span class="nav-name" data-i18n="nav-name">Social Democratic Alliance</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html" data-i18n="nav-home">Home</a></li>
      <li><a href="platform.html" data-i18n="nav-platform">Platform</a></li>
      <li><a href="events.html" data-i18n="nav-campaigning">Campaigning</a></li>
      <li><a href="candidates.html" class="active" data-i18n="nav-candidates">Candidates</a></li>
      <li class="lang-switcher">
        <button class="lang-toggle" aria-label="Change Language">
          <span class="lang-current">AL</span>
        </button>
        <div class="lang-dropdown">
          <button class="lang-option active" data-lang="al">Alanian</button>
        </div>
      </li>
      <li><a href="#" class="theme-toggle" onclick="toggleTheme(event)" title="Toggle Night Mode">🌗</a></li>
    </ul>
  </nav>

  <section class="page-header" style="margin-top: 80px; text-align: center; animation: fadeUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;">
    <h1 style=" font-size: 4.5rem;">Our Candidates</h1>
    <p style="margin: 0 auto; font-size: 1.25rem; max-width: 600px;">Meet the leaders fighting for the Republic.</p>
  </section>
"""

html_exec = """
  <!-- Executive Section -->
  <section class="page-section" style="padding: 40px 5%; max-width: 1200px; margin: 0 auto;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 2.5rem; margin-bottom: 30px; border-bottom: 2px solid var(--primary); padding-bottom: 10px; display: inline-block;">Executive Leadership</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px;">
      
      <div class="candidate-card" style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); padding: 30px; display: flex; flex-direction: column; align-items: center; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <div class="portrait" style="width: 180px; height: 180px; border-radius: 50%; background: rgba(0,0,0,0.1); border: 3px solid var(--primary); margin-bottom: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            <span style="color: var(--text-muted); font-size: 0.9rem;">No Photo</span>
        </div>
        <h3 style="font-size: 1.8rem; margin-bottom: 5px; font-family: 'Outfit', sans-serif;">Mandy Trottier</h3>
        <p style="color: var(--primary); font-weight: 600; margin-bottom: 5px;">Presidential Candidate</p>
        <p style="color: var(--text-muted); margin-bottom: 25px; font-size: 0.9rem;">Endorsed (Alternative Labour Party)</p>
        <div style="display: flex; gap: 15px; width: 100%; justify-content: center; margin-top: auto;">
          <button class="btn-primary" style="flex: 1; padding: 10px; border: none; border-radius: 4px; font-weight: 600; cursor: pointer;">Events</button>
          <button class="btn-outline" style="flex: 1; padding: 10px; border: 1px solid var(--primary); background: transparent; color: var(--text-main); border-radius: 4px; font-weight: 600; cursor: pointer;">Media</button>
        </div>
      </div>

      <div class="candidate-card" style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); padding: 30px; display: flex; flex-direction: column; align-items: center; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <div class="portrait" style="width: 180px; height: 180px; border-radius: 50%; background: rgba(0,0,0,0.1); border: 3px solid var(--primary); margin-bottom: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            <span style="color: var(--text-muted); font-size: 0.9rem;">No Photo</span>
        </div>
        <h3 style="font-size: 1.8rem; margin-bottom: 5px; font-family: 'Outfit', sans-serif;">Safiyya Bethune</h3>
        <p style="color: var(--primary); font-weight: 600; margin-bottom: 25px;">Candidate for Governor</p>
        <div style="display: flex; gap: 15px; width: 100%; justify-content: center; margin-top: auto;">
          <button class="btn-primary" style="flex: 1; padding: 10px; border: none; border-radius: 4px; font-weight: 600; cursor: pointer;">Events</button>
          <button class="btn-outline" style="flex: 1; padding: 10px; border: 1px solid var(--primary); background: transparent; color: var(--text-main); border-radius: 4px; font-weight: 600; cursor: pointer;">Media</button>
        </div>
      </div>
    </div>
  </section>
"""

constituency = [
    ("Marcus Horvat", "Ambrosia"),
    ("Aldric von Reichel", "Cambria"),
    ("William Smith", "Kazana"),
    ("Sherwin Hildebrand", "Mezata"),
    ("Adam Scholz", "Oplana"),
    ("Noodles dos Açores", "Reno"),
]

html_const = """
  <!-- Constituency Parliament Section -->
  <section class="page-section" style="padding: 40px 5%; max-width: 1200px; margin: 0 auto;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 2.5rem; margin-bottom: 30px; border-bottom: 2px solid var(--primary); padding-bottom: 10px; display: inline-block;">Constituency Parliament</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px;">
"""

for name, region in constituency:
    img_tag = '<span style="color: var(--text-muted); font-size: 0.9rem;">No Photo</span>'
    if name == "Aldric von Reichel":
        img_tag = '<img src="assets/images/AldricvonReichelPortraitNoBG.png" alt="Aldric von Reichel" style="width: 100%; height: 100%; object-fit: cover;">'
        
    html_const += f"""
      <div class="candidate-card" style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); padding: 25px; display: flex; flex-direction: column; align-items: center; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <div class="portrait" style="width: 140px; height: 140px; border-radius: 50%; background: rgba(0,0,0,0.1); border: 3px solid var(--primary); margin-bottom: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            {img_tag}
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 5px; font-family: 'Outfit', sans-serif;">{name}</h3>
        <p style="color: var(--primary); font-weight: 600; margin-bottom: 20px; font-size: 1rem;">Candidate for {region}</p>
        <div style="display: flex; gap: 10px; width: 100%; justify-content: center; margin-top: auto;">
          <button class="btn-primary" style="flex: 1; padding: 8px; font-size: 0.9rem; border: none; border-radius: 4px; font-weight: 600; cursor: pointer;">Events</button>
          <button class="btn-outline" style="flex: 1; padding: 8px; font-size: 0.9rem; border: 1px solid var(--primary); background: transparent; color: var(--text-main); border-radius: 4px; font-weight: 600; cursor: pointer;">Media</button>
        </div>
      </div>
"""

html_const += """
    </div>
  </section>
"""

party_list = [
    "Florence Marin",
    "William Smith",
    "Sherwin Hildebrand",
    "Adam Scholz",
    "Aldric von Reichel",
    "Marcus Horvat",
    "Valentine Magres",
    "Stephen Bratanovic",
    "Brezhnev Prigozhn",
    "Dorothy Ardern Roosevelt"
]

html_party = """
  <!-- Party List Section -->
  <section class="page-section" style="padding: 40px 5%; max-width: 1200px; margin: 0 auto; margin-bottom: 60px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 2.5rem; margin-bottom: 30px; border-bottom: 2px solid var(--primary); padding-bottom: 10px; display: inline-block;">Party List for Parliament</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px;">
"""

for i, name in enumerate(party_list):
    img_tag = '<span style="color: var(--text-muted); font-size: 0.9rem;">No Photo</span>'
    if name == "Aldric von Reichel":
        img_tag = '<img src="assets/images/AldricvonReichelPortraitNoBG.png" alt="Aldric von Reichel" style="width: 100%; height: 100%; object-fit: cover;">'
    
    role = f"List Position #{i+1}"
    if name == "Florence Marin":
        role += " • Party Chair"

    html_party += f"""
      <div class="candidate-card" style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); padding: 25px; display: flex; flex-direction: column; align-items: center; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease;">
        <div class="portrait" style="width: 140px; height: 140px; border-radius: 50%; background: rgba(0,0,0,0.1); border: 3px solid var(--primary); margin-bottom: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            {img_tag}
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 5px; font-family: 'Outfit', sans-serif;">{name}</h3>
        <p style="color: var(--primary); font-weight: 600; margin-bottom: 20px; font-size: 1rem;">{role}</p>
        <div style="display: flex; gap: 10px; width: 100%; justify-content: center; margin-top: auto;">
          <button class="btn-primary" style="flex: 1; padding: 8px; font-size: 0.9rem; border: none; border-radius: 4px; font-weight: 600; cursor: pointer;">Events</button>
          <button class="btn-outline" style="flex: 1; padding: 8px; font-size: 0.9rem; border: 1px solid var(--primary); background: transparent; color: var(--text-main); border-radius: 4px; font-weight: 600; cursor: pointer;">Media</button>
        </div>
      </div>
"""

html_party += """
    </div>
  </section>
"""

html_end = """
  <footer>
    <div class="footer-container">
      <div class="footer-brand">
        <img class="logo-light" src="assets/images/SDAlogo.svg" alt="Social Democratic Alliance" />
        <img class="logo-dark" src="assets/images/SDAlogo-dark.svg" alt="Social Democratic Alliance" />
        <div class="footer-brand-text">
          <div class="footer-name" data-i18n="footer-name">Social Democratic Alliance</div>
          <div class="footer-motto" data-i18n="footer-motto">For the Republic. For the People.</div>
        </div>
      </div>
      <div class="footer-copy" data-i18n="footer-copy">
        Upcoming Elections · Caprica<br />
        Social Democratic Alliance
      </div>
    </div>
  </footer>

  <script>
    function toggleTheme(e) {
      if (e) e.preventDefault();
      const html = document.documentElement;
      if (html.classList.contains('dark-theme')) {
        html.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
      } else {
        html.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
      }
    }
    
    // Add hover effects for candidate cards
    document.querySelectorAll('.candidate-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.boxShadow = '0 15px 40px rgba(0,0,0,0.2)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
        });
    });
  </script>
</body>
</html>
"""

with open('candidates.html', 'w', encoding='utf-8') as f:
    f.write(html_start + html_exec + html_const + html_party + html_end)

print("candidates.html created")
