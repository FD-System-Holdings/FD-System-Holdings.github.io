#!/usr/bin/env python3
"""
FD System Holdings - Zero-Dependency Verification Suite
Validates all HTML semantics, heading hierarchy, internal hyperlinks, asset paths,
and GitHub Pages deployment configuration using only the Python standard library.
"""

import os
import sys
import re
from urllib.parse import urlparse

def find_repo_root():
    """Finds repository root relative to this script."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_html_file(filepath, repo_root):
    """Audits a single HTML file for links, assets, and semantic headings."""
    rel_path = os.path.relpath(filepath, repo_root).replace(os.sep, '/')
    errors = []
    warnings = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. DOCTYPE check
    if not re.match(r'^\s*<!DOCTYPE html>', content, re.IGNORECASE):
        errors.append(f"{rel_path}: Missing <!DOCTYPE html>")

    # 2. Viewport & Charset
    if not re.search(r'<meta\s+charset=[\'"]UTF-8[\'"]', content, re.IGNORECASE):
        warnings.append(f"{rel_path}: Missing standard UTF-8 charset meta tag")
    if not re.search(r'<meta\s+name=[\'"]viewport[\'"]', content, re.IGNORECASE):
        warnings.append(f"{rel_path}: Missing viewport meta tag")

    # 3. Heading hierarchy
    h_tags = re.findall(r'<h([1-6])[^>]*>', content, re.IGNORECASE)
    h_levels = [int(lvl) for lvl in h_tags]

    if 1 not in h_levels:
        errors.append(f"{rel_path}: Missing required <h1> element for document outline")

    last_lvl = 0
    for lvl in h_levels:
        if last_lvl > 0 and lvl > last_lvl + 1:
            warnings.append(f"{rel_path}: Skipped heading level from <h{last_lvl}> directly to <h{lvl}>")
        last_lvl = lvl

    # Collect all IDs in this document for anchor verification
    doc_ids = set(re.findall(r'\bid=[\'"]([^\'"]+)[\'"]', content))

    # 4. Check relative links and asset sources
    # Matches href="..." and src="..."
    matches = re.finditer(r'\b(href|src)=[\'"]([^\'"]+)[\'"]', content)
    base_dir = os.path.dirname(filepath)
    link_count = 0

    for m in matches:
        attr = m.group(1)
        raw_target = m.group(2).strip()

        # Skip external protocols, tel, mailto, javascript
        if raw_target.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:')):
            continue

        link_count += 1
        parsed = urlparse(raw_target)
        target_path = parsed.path
        fragment = parsed.fragment

        # In-page anchor check (e.g. href="#section")
        if not target_path and fragment:
            if fragment not in doc_ids:
                errors.append(f"{rel_path}: Broken internal anchor #{fragment}")
            continue

        # File reference check
        target_fs_path = os.path.normpath(os.path.join(base_dir, target_path))
        if not os.path.exists(target_fs_path):
            errors.append(f"{rel_path}: Broken {attr} target '{raw_target}' (file not found)")
        elif fragment and target_path.endswith('.html'):
            # Cross-file anchor check
            try:
                with open(target_fs_path, "r", encoding="utf-8") as tf:
                    target_content = tf.read()
                target_ids = set(re.findall(r'\bid=[\'"]([^\'"]+)[\'"]', target_content))
                if fragment not in target_ids:
                    errors.append(f"{rel_path}: Target file '{target_path}' lacks anchor #{fragment}")
            except Exception as e:
                warnings.append(f"{rel_path}: Could not inspect target #{fragment}: {e}")

    return {
        "file": rel_path,
        "errors": errors,
        "warnings": warnings,
        "links_checked": link_count,
        "headings": [f"<h{l}>" for l in h_levels]
    }

def main():
    repo_root = find_repo_root()
    print("=" * 65)
    print("FD SYSTEM HOLDINGS - ZERO-DEPENDENCY SITE VERIFICATION")
    print("=" * 65)
    print(f"Repository Root: {repo_root}\n")

    total_errors = 0
    total_warnings = 0
    total_links = 0
    html_files = []

    # Find all HTML files
    for root, _, files in os.walk(repo_root):
        # Skip .git directory
        if os.path.sep + '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    html_files.sort()
    print(f"Found {len(html_files)} HTML documents to verify...\n")

    for f in html_files:
        result = check_html_file(f, repo_root)
        total_links += result["links_checked"]
        rel = result["file"]
        h_str = " -> ".join(result["headings"]) if result["headings"] else "None"

        if result["errors"]:
            print(f"❌ {rel} ({result['links_checked']} links)")
            for err in result["errors"]:
                print(f"   [ERROR] {err}")
                total_errors += 1
        elif result["warnings"]:
            print(f"⚠️  {rel} ({result['links_checked']} links)")
            for w in result["warnings"]:
                print(f"   [WARN] {w}")
                total_warnings += 1
        else:
            print(f"✅ {rel} (Headings: {h_str} | Links: {result['links_checked']})")

    # Deployment configuration checks
    print("\nChecking deployment configuration:")
    nojekyll_path = os.path.join(repo_root, ".nojekyll")
    if os.path.isfile(nojekyll_path):
        print("✅ .nojekyll present (Jekyll bypass enabled)")
    else:
        print("❌ .nojekyll missing in root")
        total_errors += 1

    cname_path = os.path.join(repo_root, "CNAME")
    if os.path.isfile(cname_path):
        with open(cname_path, "r", encoding="utf-8") as f:
            cname_val = f.read().strip()
        print(f"✅ CNAME present: {cname_val}")
    else:
        print("❌ CNAME missing in root")
        total_errors += 1

    pdf_path = os.path.join(repo_root, "assets", "legal", "Privacy-Policy.pdf")
    if os.path.isfile(pdf_path) and os.path.getsize(pdf_path) > 1000:
        print(f"✅ Privacy-Policy.pdf verified ({os.path.getsize(pdf_path)} bytes)")
    else:
        print("❌ assets/legal/Privacy-Policy.pdf missing or empty")
        total_errors += 1

    print("\n" + "=" * 65)
    print(f"VERIFICATION SUMMARY: {len(html_files)} files, {total_links} links verified")
    print(f"Errors: {total_errors} | Warnings: {total_warnings}")
    print("=" * 65)

    if total_errors > 0:
        print("\n❌ Verification FAILED. Please resolve errors above.")
        sys.exit(1)
    else:
        print("\n✅ Verification PASSED. All links, headings, and configs valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
