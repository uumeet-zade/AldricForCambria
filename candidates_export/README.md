# SDA Candidates Export

Self-contained folder with all candidate data and portrait images, ready to be dropped into another project.

## Folder Structure

```
candidates_export/
├── README.md
├── candidates.json        ← structured data (name, region, role, portrait path)
└── portraits/
    ├── SafiyaBethune.jpg
    ├── FlorenceMarin.png
    ├── StephenBratanovic.jpg
    ├── MarcusHorvat.jpg
    ├── BrezhnevPrigozgin.jpeg
    ├── AldricvonReichel.png
    ├── WillSmith.png
    ├── SherwinHildebrand.png
    ├── AdamScholz.png
    ├── DorothyArdernRoosevelt.png
    ├── NoodlesDosAcores.jpg
    ├── ValentineMagres.png
    └── JeanneValat.jpg
```

## Data Format (`candidates.json`)

Each candidate entry contains:

| Field               | Type   | Description                                      |
|---------------------|--------|--------------------------------------------------|
| `name`              | string | Full name                                        |
| `region`            | string | Constituency or "National"                       |
| `category`          | string | `executive`, `senate`, `house`, or `list`        |
| `role`              | string | Display role / title                             |
| `partyListPosition` | number | *(optional)* Rank on the national party list     |
| `portrait`          | string | Relative path to portrait image within this folder |

## Candidates Summary

| #  | Name                   | Region   | Category  | Portrait File                  |
|----|------------------------|----------|-----------|--------------------------------|
| 1  | Safiya Bethune-Fayyad  | Reno     | Executive | SafiyaBethune.jpg              |
| 2  | Florence Marin         | National | Senate    | FlorenceMarin.png              |
| 3  | Stephen Bratanovic     | National | Senate    | StephenBratanovic.jpg          |
| 4  | Marcus Horvat          | National | Senate    | MarcusHorvat.jpg               |
| 5  | Brezhnev Prigozhn      | National | Senate    | BrezhnevPrigozgin.jpeg         |
| 6  | Aldric von Reichel     | Cambria  | House     | AldricvonReichel.png           |
| 7  | William Smith          | Kazana   | House     | WillSmith.png                  |
| 8  | Sherwin Hildebrand     | Mezata   | House     | SherwinHildebrand.png          |
| 9  | Adam Scholz            | Oplana   | House     | AdamScholz.png                 |
| 10 | Dorothy Roosevelt      | Reno     | House     | DorothyArdernRoosevelt.png     |
| 11 | Noodles dos Açores     | Reno     | House     | NoodlesDosAcores.jpg           |
| 12 | Valentine Magres       | National | List      | ValentineMagres.png            |
| 13 | Jeanne Valat           | National | List      | JeanneValat.jpg                |

## Usage

```javascript
// Example: load candidates in any JS project
import candidates from './candidates.json';

candidates.forEach(c => {
  console.log(`${c.name} — ${c.region} — ${c.portrait}`);
});
```
