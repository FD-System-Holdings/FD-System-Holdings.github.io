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
├── .nojekyll                   # Disables Jekyll processing on GitHub Pages
├── CNAME                       # Custom domain routing (fdsystemholdings.com)
├── index.html                  # Official Home Page
├── css/
│   └── style.css               # Minimalist retro stylesheet
├── assets/
│   ├── icon/                   # Corporate icon & header branding
│   └── legal/                  # Official governance & policy PDFs
├── pages/
│   ├── founders-message.html   # Founder's Message
│   ├── governance.html         # Corporate Governance & Ethics
│   ├── partners.html           # Links to Companies We Work With
│   └── privacy-policy.html     # Website Privacy Policy
├── archive/                    # Archived page templates for future use
│   ├── annual-reports.html     # Template: Annual Reports & interim statements
│   ├── news-releases.html      # Template: News Releases from FD System Holdings
│   └── software.html           # Template: Links to FD System Holdings Software
├── reports/
│   └── README.md               # Guide for PDF report uploads
└── scripts/
    ├── generate_pdf.py         # Script for compiling legal PDFs
    └── verify.py               # Zero-dependency site validator and link checker
```

## Local Verification & Utilities

- **Verify all links and headings:**
  ```bash
  python scripts/verify.py
  ```
- **Recompile legal PDF documents:**
  ```bash
  python scripts/generate_pdf.py
  ```

## GitHub Pages Deployment

Because this repository is configured with a custom domain via `CNAME`:
1. Push this codebase to the `main` branch.
2. In GitHub under **Repository Settings > Pages**:
   - Source: **Deploy from a branch**
   - Branch: `main` / Folder: `/(root)`
3. The site is live at `https://fdsystemholdings.com`.
