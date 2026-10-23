# FD System Holdings Website

Official website for **FD System Holdings**, located at **8 The Green #27082, Dover, DE 19901**.

Modeled strictly on the minimalist, text-first, high-performance design of [Berkshire Hathaway](https://www.berkshirehathaway.com).

## Architecture & Layout

- **Zero Bloat:** Pure HTML5 and vanilla CSS. Zero JavaScript dependencies, zero external tracker scripts, zero web fonts to download.
- **Classic Formatting:**
  - Centered layout with traditional system serif typography (`Times New Roman`, `Times`, `Georgia`).
  - Standard hyperlinks with classic contrast (`#0000ee` blue / `#551a8b` purple).
  - Clean two-column table directories.
  - Authentic horizontal rules (`<hr>`) as section dividers.
  - Retro corporate disclaimers and address styling.
  - Subtle responsive design for modern mobile devices.

## Site Structure

```
├── index.html                  # Official Home Page
├── css/
│   └── style.css               # Minimalist retro stylesheet
├── assets/
│   └── logo.svg                # Vector logo mark
├── pages/
│   ├── founders-message.html   # Founder's Message
│   ├── annual-reports.html     # Annual Reports & interim statements
│   ├── news-releases.html      # News Releases from FD System Holdings
│   ├── software.html           # Links to FD System Holdings Software
│   ├── governance.html         # Corporate Governance & Ethics
│   └── partners.html           # Links to Companies We Work With
└── reports/
    └── README.md               # Guide for PDF report uploads
```

## GitHub Pages Deployment

Because this repository is named `fd-system-holdings.github.io`:
1. Push this codebase to the `main` branch.
2. In GitHub under **Repository Settings > Pages**:
   - Source: **Deploy from a branch**
   - Branch: `main` / Folder: `/(root)`
3. The site will be live at `https://fd-system-holdings.github.io`.
