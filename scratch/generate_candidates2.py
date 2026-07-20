html_top = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Social Democratic Alliance - Candidates</title>
  <link
    href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap"
    rel="stylesheet" />
    <link rel="stylesheet" href="assets/css/style.css?v=1.4">

  <script>
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
      document.documentElement.classList.add('dark-theme');
    }
  </script>
  <script src="assets/js/translations.js?v=1.2" defer></script>
  <link rel="icon" type="image/png" href="assets/images/favicon.png">
  <meta property="og:title" content="Social Democratic Alliance - Candidates">
  <meta property="og:description" content="Meet our candidates. For the Republic. For the People.">
  <meta property="og:image" content="https://uumeet-zade.github.io/sdapage/assets/images/link_preview.png">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Social Democratic Alliance - Candidates">
  <meta name="twitter:description" content="Meet our candidates. For the Republic. For the People.">
  <meta name="twitter:image" content="https://uumeet-zade.github.io/sdapage/assets/images/link_preview.png">
</head>
<body>
  <nav>
    <a href="index.html" class="nav-brand" style="text-decoration: none; color: inherit;">
      <img class="nav-logo logo-light" src="assets/images/SDAlogo.svg" alt="Social Democratic Alliance Logo" />
      <img class="nav-logo logo-dark" src="assets/images/SDAlogo-dark.svg" alt="Social Democratic Alliance Logo" />
      <span class="nav-name" data-i18n="nav-brand-name">Social Democratic Alliance</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="platform.html">Platform</a></li>
      <li><a href="candidates.html" class="active">Candidates</a></li>
      <li><a href="events.html">Events</a></li>
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
  
  <div class="page-header" style="margin-top: 73px;">
    <h1 data-i18n="cand-page-title">The Candidates of SDA</h1>
    <p data-i18n="cand-page-desc" style="margin-bottom: 24px;">Men and women from across the Republic, standing for their communities.</p>
  </div>
  
    <div class="candidate-filters event-filters" style="margin-top: -10px;">
      <button class="filter-btn active" data-filter="all" data-i18n="filter-all-cand">All Candidates</button>
      <button class="filter-btn" data-filter="executive" data-i18n="filter-exec">Executive</button>
      <button class="filter-btn" data-filter="house" data-i18n="filter-house">Constituency Parliament</button>
      <button class="filter-btn" data-filter="list" data-i18n="filter-list">Party List</button>
    </div>
    <div class="candidates-section">
"""

html_exec = """
      <div class="candidates-category" data-category="executive">
        <div class="category-label" data-i18n="cand-cat-exec">Executive Leadership</div>
        <div class="featured-candidates">
          
          <div class="featured-candidate-card">
            <div class="candidate-initials">MT</div>
            <div class="candidate-details">
              <div class="candidate-name">Mandy Trottier</div>
              <div class="candidate-role" data-i18n="role-pres">Presidential Candidate</div>
              <div class="candidate-constituency" data-i18n="const-nat">National</div>
              <div class="candidate-bio" data-i18n="bio-pres">Endorsed (Alternative Labour Party)</div>
            </div>
          </div>

          <div class="featured-candidate-card">
            <img class="candidate-image" src="assets/images/portraits/SafiyaBethune.jpg" alt="Safiyya Bethune" />
            <div class="candidate-details">
              <div class="candidate-name">Safiyya Bethune</div>
              <div class="candidate-role" data-i18n="role-gov">Governor Candidate</div>
              <div class="candidate-constituency" data-i18n="const-gov">State/Regional</div>
              <div class="candidate-bio" data-i18n="bio-gov">Candidate for Governor.</div>
            </div>
          </div>

        </div>
      </div>
"""

constituency = [
    ("Marcus Horvat", "Ambrosia", "MarcusHorvat.jpg"),
    ("Aldric von Reichel", "Cambria", "AldricvonReichel.png"),
    ("William Smith", "Kazana", "WillSmith.png"),
    ("Sherwin Hildebrand", "Mezata", "SherwinHildebrand.png"),
    ("Adam Scholz", "Oplana", "AdamScholz.png"),
    ("Noodles dos Açores", "Reno", "NoodlesDosAcores.jpg"),
]

html_const = """
      <div class="candidates-category" data-category="house">
        <div class="category-label" data-i18n="cand-cat-const">Constituency Parliament</div>
        <div class="masonry-candidates">
"""
for name, region, portrait in constituency:
    html_const += f"""
          <div class="candidate-card">
            <img class="candidate-image" src="assets/images/portraits/{portrait}" alt="{name}" style="object-position: 100% 50%;" />
            <div class="candidate-name">{name}</div>
            <div class="candidate-role">Parliament Candidate</div>
            <div class="candidate-constituency">{region}</div>
            <div class="candidate-bio">Running for Constituency Parliament.</div>
          </div>
"""
html_const += """
        </div>
      </div>
"""

party_list = [
    ("Florence Marin", "FlorenceMarin.png"),
    ("William Smith", "WillSmith.png"),
    ("Sherwin Hildebrand", "SherwinHildebrand.png"),
    ("Adam Scholz", "AdamScholz.png"),
    ("Aldric von Reichel", "AldricvonReichel.png"),
    ("Marcus Horvat", "MarcusHorvat.jpg"),
    ("Valentine Magres", "ValentineMagres.png"),
    ("Stephen Bratanovic", "StephenBratanovic.jpg"),
    ("Brezhnev Prigozhn", "BrezhnevPrigozgin.jpeg"),
    ("Dorothy Ardern Roosevelt", "DorothyArdernRoosevelt.png")
]

html_list = """
      <div class="candidates-category" data-category="list">
        <div class="category-label" data-i18n="cand-cat-list">Party List for Parliament</div>
        <div class="masonry-candidates">
"""
for i, (name, portrait) in enumerate(party_list):
    role = f"Party List #{i+1}"
    if name == "Florence Marin":
        role = f"Party Chair • {role}"
    
    html_list += f"""
          <div class="candidate-card">
            <img class="candidate-image" src="assets/images/portraits/{portrait}" alt="{name}" style="object-position: 100% 50%;" />
            <div class="candidate-name">{name}</div>
            <div class="candidate-role">{role}</div>
            <div class="candidate-constituency">National</div>
            <div class="candidate-bio">Standing on the party list.</div>
          </div>
"""
html_list += """
        </div>
      </div>
"""

html_bottom = """
    </div>

  <section class="pillars" style="text-align: center; padding: 60px 5%; background: var(--bg-body); margin-top: 40px;">
    <h2 class="section-title" style="margin-bottom: 24px;" data-i18n="cand-meet-title">Meet them on the ground</h2>
    <p style="font-size: 1.1rem; color: var(--text-muted); max-width: 600px; margin: 0 auto 32px;" data-i18n="cand-meet-desc">Join our candidates at town halls, rallies, and community meetings near you.</p>
    <a href="events.html" class="btn-primary" data-i18n="cand-meet-btn">View Upcoming Events</a>
  </section>

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

  <!-- Candidate Action Modal -->
  <div id="candidate-modal" class="modal-backdrop">
    <div class="modal-content">
      <button class="modal-close" aria-label="Close modal">&times;</button>
      <div class="modal-header">
        <h3 id="modal-candidate-name">Candidate Name</h3>
        <p id="modal-candidate-role" class="candidate-role" style="margin-bottom: 0;">Role</p>
      </div>
      <div class="modal-body">
        <button class="btn-primary modal-action-btn" onclick="alert('Coming soon!')">View Events</button>
        <button class="btn-secondary modal-action-btn" onclick="alert('Coming soon!')">View Media</button>
      </div>
    </div>
  </div>

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

    // Modal Logic
    document.addEventListener('DOMContentLoaded', () => {
      const modal = document.getElementById('candidate-modal');
      const closeBtn = document.querySelector('.modal-close');
      const nameEl = document.getElementById('modal-candidate-name');
      const roleEl = document.getElementById('modal-candidate-role');
      const candidateCards = document.querySelectorAll('.candidate-card, .featured-candidate-card');

      // Open modal on card click
      candidateCards.forEach(card => {
        card.addEventListener('click', () => {
          const name = card.querySelector('.candidate-name').textContent;
          const role = card.querySelector('.candidate-role').textContent;
          
          nameEl.textContent = name;
          roleEl.textContent = role;
          
          modal.classList.add('active');
          document.body.style.overflow = 'hidden'; // Prevent scrolling
        });
      });

      // Close modal functions
      const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
      };

      closeBtn.addEventListener('click', closeModal);

      // Close on backdrop click
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          closeModal();
        }
      });
      
      // Close on Escape key
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
          closeModal();
        }
      });
    });

    // Filter Logic
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.candidate-filters .filter-btn');
      const categories = document.querySelectorAll('.candidates-category');
      
      // Ensure smooth transitions
      categories.forEach(c => {
        c.style.transition = 'opacity 0.4s ease, transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.1)';
      });

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const filterValue = btn.getAttribute('data-filter');

          categories.forEach(category => {
            const catType = category.getAttribute('data-category');
            if (filterValue === 'all' || catType === filterValue) {
              category.style.display = 'block';
              setTimeout(() => {
                category.style.opacity = '1';
                category.style.transform = 'translateY(0) scale(1)';
              }, 10);
            } else {
              category.style.opacity = '0';
              category.style.transform = 'translateY(20px) scale(0.95)';
              setTimeout(() => {
                category.style.display = 'none';
              }, 300);
            }
          });
        });
      });
    });
  </script>
</body>
</html>
"""

with open('candidates.html', 'w', encoding='utf-8') as f:
    f.write(html_top + html_exec + html_const + html_list + html_bottom)
print("Updated candidates.html with the new design!")
