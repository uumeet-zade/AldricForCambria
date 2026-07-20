import os

new_context = """# Campaign Website Context: Social Democratic Alliance (National Party)

## Overview
This repository contains the national campaign website for the **Social Democratic Alliance (SDA)**. It was originally built as a localized by-election campaign page for Aldric von Reichel (Chasmia/Cambria) but has since been restructured and rebranded into a general party-wide election platform for the upcoming Caprica national elections.

## File Organization
To manage the growing scope of the project, all files are strictly organized:
*   **`index.html`, `platform.html`, `events.html`, `candidates.html`**: The main pages remain in the root directory.
*   **`assets/images/`**: Contains all SVG logos, favicons, and the `portraits/` subfolder for candidate images.
*   **`assets/css/`**: Contains `style.css`.
*   **`assets/js/`**: Contains the `translations.js` script.
*   **`scripts/`**: Contains all Python utilities for managing translations and index fixing.
*   **`data/`**: Contains `new_source.json`, `new_translations.json`, and `story_source.json`.

## Key Pages & Layouts
1.  **Home (`index.html`)**: Rebranded from "Aldric for Cambria" to a general "For the People. For the Republic" focus. The old highly specific "Letter to Cambria" has been removed.
2.  **Platform (`platform.html`)**: Now generalized as "The Party Platform", modifying old regional promises (like the Cambrian R&D Center) into National initiatives.
3.  **Candidates (`candidates.html`)**: A newly built, frosted-glass masonry grid page that organizes the party roster into three distinct interactive categories (Executive Leadership, Constituency Parliament, Party List for Parliament).
4.  **Campaigning (`events.html`)**: Replaces the template's generic events page. Old Cambria-specific event articles (`event-guildhall`, `event-field`) were entirely deleted to keep the page globally focused.

## Candidate Roster & Mapping
The candidates are officially categorized as follows:

*   **Executive Leadership**
    *   Mandy Trottier (Presidential Candidate) - *Endorsed by Alternative Labour Party. Portrait mapped to `MandyTrottier.png` with an ALP Logo badge.*
    *   Isolde von Dittarsdorf (Vice Presidential Candidate) - *Endorsed.*
    *   Safiyya Bethune (Governor Candidate) - *Reno*
*   **Constituency Parliament**
    *   Ambrosia - Marcus Horvat
    *   Cambria - Aldric von Reichel
    *   Kazana - William Smith
    *   Mezata - Sherwin Hildebrand
    *   Oplana - Adam Scholz 
    *   Reno - Noodles dos Açores
*   **Party List for Parliament**
    1. Florence Marin (Party Chair)
    2. William Smith
    3. Sherwin Hildebrand
    4. Adam Scholz
    5. Aldric von Reichel
    6. Marcus Horvat
    7. Valentine Magres
    8. Stephen Bratanovic
    9. Brezhnev Prigozhn 
    10. Dorothy Ardern Roosevelt

## Strict User Rules
The user has established strict formatting and writing rules that **MUST** be followed at all times. These are also documented in `.agents/AGENTS.md`:
1.  **No Em Dashes**: Never use em dashes (—). Stick strictly to regular hyphens (-).
2.  **Specific Phrasing Ban**: Never use "is not X - but Y" phrasing (or similar variations like "is not X, but Y"). 
3.  **Template Loyalty**: Maintain the general structure and aesthetic of the design template provided, applying sleek dark modes, glassmorphism (`--glass-bg`), and premium responsive layouts.

## Important Note on Translations (`translations.js`)
**CRITICAL:** The website uses a Javascript translation system (`translations.js`) that runs on page load and replaces the text of any HTML element that has a `data-i18n` attribute. 
Because we have heavily customized the English text on these pages (like custom candidate bios for Mandy and Isolde), you **MUST REMOVE** the `data-i18n` attributes from any hardcoded HTML element you manually write. If you leave the `data-i18n` tag intact, the script will overwrite your custom English text with the old placeholder text from the JSON dictionary as soon as the page loads.
"""

with open('context.md', 'w', encoding='utf-8') as f:
    f.write(new_context)
