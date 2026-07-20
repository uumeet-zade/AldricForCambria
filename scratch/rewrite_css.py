css_content = """
/* SOCIAL DEMOCRATIC ALLIANCE - PREMIUM MINIMALIST DESIGN SYSTEM */

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  /* Core Palette */
  --primary: #D7003A; /* Official Rose Red */
  --primary-hover: #B0002F;
  --primary-glow: rgba(215, 0, 58, 0.15);
  
  /* Light Theme */
  --bg-body: #FFFFFF;
  --bg-surface: #F9FAFB;
  --text-main: #111827;
  --text-muted: #6B7280;
  --border-color: rgba(0, 0, 0, 0.04);
  
  /* Shared Elements */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 32px;
  --shadow-diffuse: 0 20px 50px rgba(0,0,0,0.03);
  --shadow-hover: 0 30px 60px rgba(0,0,0,0.06);
  --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

html.dark-theme {
  --bg-body: #0B0C10;
  --bg-surface: #161922;
  --text-main: #F9FAFB;
  --text-muted: #9CA3AF;
  --border-color: rgba(255, 255, 255, 0.04);
  --shadow-diffuse: 0 20px 50px rgba(0,0,0,0.4);
  --shadow-hover: 0 30px 60px rgba(0,0,0,0.6);
  --primary-glow: rgba(215, 0, 58, 0.25);
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
  background: var(--bg-body);
  color: var(--text-main);
  min-height: 100vh;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  transition: background 0.4s ease, color 0.4s ease;
}

h1, h2, h3, .nav-name {
  font-family: 'Playfair Display', serif;
  letter-spacing: -0.02em;
  color: var(--text-main);
}

/* ==========================================================================
   NAVIGATION
   ========================================================================== */
nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  padding: 20px 5%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: var(--transition);
}

html.dark-theme nav {
  background: rgba(11, 12, 16, 0.85);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  text-decoration: none;
}

.nav-logo {
  width: 48px;
  height: 48px;
  object-fit: contain;
}

.logo-dark { display: none !important; }
.dark-theme .logo-light { display: none !important; }
.dark-theme .logo-dark { display: inline-block !important; }

.nav-name {
  font-weight: 700;
  font-size: 1.25rem;
}

.nav-links {
  display: flex;
  gap: 40px;
  list-style: none;
  align-items: center;
}

.nav-links a {
  text-decoration: none;
  color: var(--text-muted);
  font-size: 0.95rem;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  transition: var(--transition);
  position: relative;
}

.nav-links a:hover, .nav-links a.active {
  color: var(--primary);
}

.nav-links a::after {
  content: '';
  position: absolute;
  left: 0; bottom: -6px;
  width: 100%; height: 2px;
  background: var(--primary);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-links a:hover::after, .nav-links a.active::after {
  transform: scaleX(1);
  transform-origin: left;
}

/* LANG SWITCHER */
.lang-switcher {
  position: relative;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.lang-toggle {
  background: none; border: none;
  font-size: 0.95rem; font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  display: flex; align-items: center; gap: 8px;
  transition: var(--transition);
  font-family: inherit;
}

.lang-toggle:hover, .lang-switcher:hover .lang-toggle {
  color: var(--primary);
}

.lang-dropdown {
  position: absolute;
  top: 150%; right: 0;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-diffuse);
  min-width: 200px;
  opacity: 0; visibility: hidden;
  transform: translateY(10px);
  transition: var(--transition);
  z-index: 200;
  overflow: hidden;
}

.lang-switcher:hover .lang-dropdown, .lang-switcher:focus-within .lang-dropdown {
  opacity: 1; visibility: visible;
  transform: translateY(0);
}

.lang-option {
  display: block; width: 100%;
  padding: 16px 24px;
  background: none; border: none;
  text-align: left; font-size: 0.95rem;
  font-weight: 500; color: var(--text-main);
  cursor: pointer; transition: var(--transition);
  font-family: inherit;
}

.lang-option:hover {
  background: var(--bg-body);
  color: var(--primary);
}

.lang-option.active {
  color: var(--primary);
  font-weight: 700;
}

.theme-toggle {
  font-size: 1.25rem; cursor: pointer; text-decoration: none;
  transition: transform 0.3s ease;
}
.theme-toggle:hover { transform: scale(1.1); }

/* ==========================================================================
   BUTTONS
   ========================================================================== */
.btn-primary, .btn-outline {
  padding: 18px 36px;
  font-size: 1.05rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
  border-radius: 50px;
  cursor: pointer;
  transition: var(--transition);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.btn-primary {
  background: var(--primary);
  color: #FFFFFF;
  border: 1px solid var(--primary);
  box-shadow: 0 10px 25px var(--primary-glow);
}

.btn-primary:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 35px var(--primary-glow);
  background: var(--primary-hover);
}

.btn-outline {
  background: transparent;
  color: var(--text-main);
  border: 1px solid var(--border-color);
}

.btn-outline:hover {
  border-color: var(--text-main);
  transform: translateY(-4px);
}

/* ==========================================================================
   HERO SECTION
   ========================================================================== */
.page-section { padding-top: 160px; }

.hero {
  display: flex;
  align-items: center;
  gap: 80px;
  padding: 0 5%;
  max-width: 1400px;
  margin: 0 auto;
}

.hero-eyebrow {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 0.2em;
  margin-bottom: 24px;
}

.hero-title {
  font-size: clamp(4rem, 7vw, 7rem);
  line-height: 1;
  margin-bottom: 32px;
}

.hero-title span {
  color: var(--primary);
  font-style: italic;
}

.hero-subtitle {
  font-size: 1.35rem;
  color: var(--text-muted);
  max-width: 600px;
  margin-bottom: 48px;
  font-weight: 300;
}

.hero-buttons {
  display: flex; gap: 24px;
}

.hero-visual img {
  width: 100%;
  max-width: 500px;
  opacity: 0.9;
}
html.dark-theme .hero-visual img { opacity: 0.7; }

/* ==========================================================================
   SHARED SECTIONS & BENTO
   ========================================================================== */
.bento-grid {
  padding: 120px 5%;
  max-width: 1200px;
  margin: 0 auto;
}

.bento-full {
  text-align: center;
  padding: 80px 20px;
}

.bento-full h2 {
  font-size: 3.5rem;
  margin-bottom: 24px;
}

.bento-full p {
  font-size: 1.25rem;
  max-width: 800px;
  margin: 0 auto;
  color: var(--text-muted);
  font-weight: 300;
}

/* ==========================================================================
   CANDIDATES
   ========================================================================== */
.candidates-section {
  padding: 80px 5% 160px;
  max-width: 1300px;
  margin: 0 auto;
}

.candidates-category { margin-bottom: 120px; }

.category-label {
  font-size: 2rem;
  margin-bottom: 60px;
  color: var(--text-main);
  text-align: center;
}

.candidates-grid, .masonry-candidates {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 40px;
}

/* Feature Candidates (Executive) */
.featured-candidates {
  display: flex; flex-direction: column; gap: 40px; margin-bottom: 40px;
}

/* Universal Card Style for Candidates */
.candidate-card, .featured-candidate-card {
  background: var(--bg-surface);
  border-radius: var(--radius-lg);
  padding: 48px;
  border: none;
  box-shadow: var(--shadow-diffuse);
  transition: var(--transition);
  cursor: pointer;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.featured-candidate-card {
  flex-direction: row;
  text-align: left;
  align-items: center;
  gap: 48px;
}

.candidate-card:hover, .featured-candidate-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-hover);
}

.candidate-image, .candidate-initials {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 32px;
  box-shadow: var(--shadow-diffuse);
  background: var(--bg-body);
  display: flex; align-items: center; justify-content: center;
  font-size: 2.5rem;
  font-family: 'Playfair Display', serif;
  color: var(--text-main);
}

.featured-candidate-card .candidate-image,
.featured-candidate-card .candidate-initials {
  width: 180px; height: 180px; margin-bottom: 0;
}

.candidate-name {
  font-size: 2rem;
  margin-bottom: 8px;
}

.candidate-role {
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 16px;
}

.candidate-constituency {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-bottom: 24px;
}

.candidate-bio {
  font-size: 1.05rem;
  color: var(--text-muted);
  line-height: 1.7;
}

/* ==========================================================================
   EVENTS
   ========================================================================== */
.events-section {
  padding: 80px 5% 160px;
  max-width: 1100px;
  margin: 0 auto;
}

.event-filters {
  display: flex; justify-content: center; gap: 16px; margin-bottom: 80px; flex-wrap: wrap;
}

.filter-btn {
  background: transparent;
  border: none;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  border-radius: 50px;
  transition: var(--transition);
}

.filter-btn:hover { color: var(--text-main); }
.filter-btn.active { background: var(--bg-surface); color: var(--text-main); box-shadow: var(--shadow-diffuse); }

.events-list {
  display: flex; flex-direction: column; gap: 40px;
}

.event-card {
  background: var(--bg-surface);
  border-radius: var(--radius-lg);
  border: none;
  box-shadow: var(--shadow-diffuse);
  display: flex;
  transition: var(--transition);
  overflow: hidden;
}

.event-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-hover);
}

.event-date {
  padding: 48px;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  background: var(--bg-body);
  min-width: 160px;
}

.event-date-month {
  font-size: 0.9rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 8px;
}
.event-date-day {
  font-size: 4rem; font-weight: 300; font-family: 'Playfair Display', serif; line-height: 1;
}

.event-details { padding: 48px; flex-grow: 1; }
.event-title { font-size: 2rem; margin-bottom: 16px; }
.event-location, .event-time { font-size: 1rem; color: var(--text-muted); margin-bottom: 12px; font-weight: 300;}
.event-desc { margin-top: 24px; font-size: 1.1rem; color: var(--text-muted); }
.event-action { padding: 48px; display: flex; align-items: center; }

/* ==========================================================================
   PLATFORM ZIGZAG
   ========================================================================== */
.platform-zigzag {
  display: flex; flex-direction: column; gap: 120px;
  padding: 80px 5% 160px;
  max-width: 1200px; margin: 0 auto;
}

.zigzag-row {
  display: flex; align-items: center; gap: 80px;
}
.zigzag-row:nth-child(even) { flex-direction: row-reverse; }

.zigzag-image-placeholder {
  flex: 0 0 auto;
  width: 100%; max-width: 440px; aspect-ratio: 4/3;
  background: var(--bg-surface);
  border-radius: var(--radius-lg);
  display: flex; align-items: center; justify-content: center;
  color: var(--text-muted);
  box-shadow: var(--shadow-diffuse);
}

.zigzag-content { flex: 1; }
.zigzag-title { font-size: 2.5rem; margin-bottom: 24px; }
.zigzag-desc { font-size: 1.15rem; color: var(--text-muted); font-weight: 300; }

/* ==========================================================================
   PAGE HEADERS
   ========================================================================== */
.page-header {
  padding: 160px 5% 80px;
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}
.page-header h1 { font-size: 4.5rem; margin-bottom: 24px; }
.page-header p { font-size: 1.35rem; color: var(--text-muted); font-weight: 300; }

/* ==========================================================================
   FOOTER
   ========================================================================== */
footer {
  padding: 120px 5%;
  background: var(--bg-surface);
}

.footer-container {
  max-width: 1400px; margin: 0 auto;
  display: flex; justify-content: space-between; align-items: center;
}
.footer-brand { display: flex; align-items: center; gap: 24px; }
.footer-brand img { width: 64px; height: 64px; }
.footer-name { font-size: 1.5rem; margin-bottom: 4px; }
.footer-motto { font-size: 1rem; color: var(--primary); font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }
.footer-copy { text-align: right; font-size: 1rem; color: var(--text-muted); }

/* ==========================================================================
   MODALS
   ========================================================================== */
.modal-backdrop {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.4); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  z-index: 1000; display: flex; justify-content: center; align-items: center;
  opacity: 0; visibility: hidden; transition: all 0.4s ease;
}
.modal-backdrop.active { opacity: 1; visibility: visible; }

.modal-content {
  background: var(--bg-body); padding: 48px; border-radius: var(--radius-xl);
  width: 90%; max-width: 480px; position: relative;
  transform: translateY(40px) scale(0.95); opacity: 0;
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: var(--shadow-hover);
}
.modal-backdrop.active .modal-content { transform: translateY(0) scale(1); opacity: 1; }

.modal-close {
  position: absolute; top: 24px; right: 24px; background: none; border: none;
  font-size: 24px; cursor: pointer; color: var(--text-muted);
}
.modal-close:hover { color: var(--text-main); }
.modal-header { text-align: center; margin-bottom: 40px; }
.modal-header h3 { font-size: 2rem; }
.modal-body { display: flex; flex-direction: column; gap: 20px; }
.modal-action-btn {
  width: 100%; padding: 18px; border-radius: 50px; font-size: 1.05rem; font-weight: 500;
  cursor: pointer; border: none; font-family: 'Inter', sans-serif; transition: var(--transition);
}
.modal-action-btn.btn-primary { background: var(--primary); color: white; }
.modal-action-btn.btn-primary:hover { background: var(--primary-hover); transform: translateY(-2px); }
.modal-action-btn.btn-secondary { background: var(--bg-surface); color: var(--text-main); }
.modal-action-btn.btn-secondary:hover { background: var(--bg-body); box-shadow: var(--shadow-diffuse); transform: translateY(-2px); }

/* ==========================================================================
   MOBILE RESPONSIVENESS
   ========================================================================== */
@media (max-width: 1024px) {
  .hero { flex-direction: column; text-align: center; padding-top: 40px; }
  .hero-buttons { justify-content: center; }
  .featured-candidate-card { flex-direction: column; text-align: center; }
  .zigzag-row, .zigzag-row:nth-child(even) { flex-direction: column; text-align: center; }
  .event-card { flex-direction: column; }
  .event-date { flex-direction: row; gap: 16px; padding: 24px; border-bottom: 1px solid var(--border-color); }
  .event-action { padding: 24px; justify-content: center; }
  .footer-container { flex-direction: column; text-align: center; gap: 40px; }
  .footer-copy { text-align: center; }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero-title { font-size: 3.5rem; }
  .bento-full h2 { font-size: 2.5rem; }
  .page-header h1 { font-size: 3.5rem; }
}
"""

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Ground-up minimal style.css deployed.")
