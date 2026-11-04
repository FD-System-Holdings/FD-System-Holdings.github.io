# Modularization and Code Compacting Plan: FD-System-Holdings.github.io

**Directory:** `D:\Programming\FD-System-Holdings.github.io`  
**Generated Date:** 2026-10-23  
**Project Type:** Static Corporate Website / GitHub Pages  

---

## 1. Project Overview & Current Architecture

`FD-System-Holdings.github.io` is a multi-page corporate static site deployed to GitHub Pages, providing information on annual reports, corporate governance, partner networks, software products, and founders' messages.

### Current File Inventory
- `index.html` (2.8 KB): Homepage layout.
- `css/style.css` (3.0 KB): Global stylesheets.
- `pages/` (6 HTML files): `annual-reports.html`, `founders-message.html`, `governance.html`, `news-releases.html`, `partners.html`, `software.html`.
- `assets/`: Legal PDFs, logos, and images.
- `CNAME`, `README.md`.

### Structural Deficiencies
1. **Severe Markup Duplication**: The `<head>`, navigation bar, logo branding, and `<footer>` are copy-pasted identically across `index.html` and all 6 subpages. Any change to the menu navigation requires manually editing 7 separate files.
2. **Hardcoded Relative Path Management**: Subpages use `../css/style.css` and `../assets/` while `index.html` uses `css/style.css`, causing broken links if files are rearranged.
3. **No Build System / Static Site Generation**: Missing component templating or build pipeline.

---

## 2. Modularization Strategy

Adopt a lightweight component or static site generation (SSG) pipeline (such as 11ty, Astro, or a zero-dependency Python build script) while publishing pre-rendered HTML to GitHub Pages:

```
FD-System-Holdings.github.io/
├── src/                                # Source templates & content
│   ├── includes/                       # Reusable partials
│   │   ├── head.html                   # Meta tags, fonts, CSP, title
│   │   ├── nav.html                    # Shared header & responsive navigation
│   │   └── footer.html                 # Shared footer, copyright, legal links
│   ├── layouts/
│   │   └── base.html                   # Master layout wrapper
│   ├── pages/                          # Pure content pages (Markdown or HTML)
│   │   ├── index.html
│   │   ├── annual-reports.html
│   │   ├── founders-message.html
│   │   ├── governance.html
│   │   ├── news-releases.html
│   │   ├── partners.html
│   │   └── software.html
│   └── css/
│       ├── reset.css
│       ├── typography.css
│       └── components.css
├── build.py                            # Zero-dependency build script (or 11ty config)
├── dist/                               # Output directory (or deployed root)
├── assets/                             # Static images & legal PDFs
├── CNAME
└── README.md
```

### Module Boundary Definitions
- **Header & Navigation (`src/includes/nav.html`)**: Centralized menu. Active link state is computed dynamically via page variable.
- **Footer (`src/includes/footer.html`)**: Centralized legal disclosures, address, and copyright.
- **Layout (`src/layouts/base.html`)**: Defines structural boilerplate once.

---

## 3. Code Compacting Strategy

1. **Eliminate 7x Duplicate Navigation & Footer**:
   - Reduces duplicated HTML lines by over 60% across the site.
2. **CSS Consolidation**:
   - Modernize CSS using CSS custom properties (variables) for branding colors (`--primary`, `--accent`, `--surface`) and spacing.
3. **Automated Link Resolution**:
   - Absolute root links (`/css/style.css`, `/assets/logo.svg`) ensure consistent asset resolution across all pages without fragile `../` traversals.

---

## 4. Implementation Action Plan

- [ ] **Phase 1: Component Extraction**
  - [ ] Create `src/includes/` and extract `nav.html`, `footer.html`, and `head.html`.
  - [ ] Create `src/layouts/base.html`.

- [ ] **Phase 2: Build Automation**
  - [ ] Implement a clean, zero-dependency `build.py` script using Python's built-in `string.Template` or `jinja2` to compile `src/` to root HTML files.
  - [ ] Add npm script or PowerShell build command.

- [ ] **Phase 3: Page Content Clean Up**
  - [ ] Strip duplicated `<head>`, `<nav>`, and `<footer>` from all 7 HTML pages, converting them to pure content body blocks.
  - [ ] Run build script to generate canonical distribution files.

- [ ] **Phase 4: Verification & GitHub Pages Validation**
  - [ ] Check local preview with `python -m http.server 8000`.
  - [ ] Validate HTML semantics and responsive mobile layout.

---

## 5. Risk Assessment & Verification

- **GitHub Pages Compatibility**: Ensure output HTML remains at root or configure GitHub Actions deployment from `dist/`.
- **Verification Command**:
  ```bash
  python build.py
  git status
  ```
