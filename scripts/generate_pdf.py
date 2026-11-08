import os
import subprocess
import shutil
import tempfile

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Privacy Policy - FD System Holdings LLC</title>
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
  }
  html, body {
    margin: 0;
    padding: 0;
    background: #ffffff;
    color: #1e293b;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 9.5pt;
    line-height: 1.5;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page {
    width: 210mm;
    height: 297mm;
    padding: 16mm 20mm 15mm 20mm;
    position: relative;
    page-break-after: always;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  
  /* Top Primary Header */
  .doc-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 12px;
    border-bottom: 2px solid #0f172a;
    margin-bottom: 14px;
  }
  .header-left {
    flex: 1;
  }
  .category-eyebrow {
    font-family: Arial, sans-serif;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #475569;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .doc-title {
    font-family: Arial, sans-serif;
    font-size: 21pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 0.5px;
    margin: 0;
    line-height: 1.1;
  }
  .header-meta {
    border-collapse: collapse;
    font-family: Arial, sans-serif;
    font-size: 8pt;
    margin-left: 20px;
  }
  .header-meta td {
    padding: 2px 6px;
    white-space: nowrap;
  }
  .header-meta td.label {
    font-weight: 700;
    color: #0f172a;
    text-align: right;
  }
  .header-meta td.val {
    color: #334155;
  }
  
  /* Secondary Header for subsequent pages */
  .doc-header-sub {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 8px;
    border-bottom: 1px solid #cbd5e1;
    margin-bottom: 14px;
    font-family: Arial, sans-serif;
    font-size: 8pt;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }
  .doc-header-sub span {
    white-space: nowrap;
  }
  
  /* Overview Callout box */
  .callout-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #0f172a;
    padding: 11px 15px;
    margin-bottom: 14px;
  }
  .callout-title {
    font-family: Arial, sans-serif;
    font-size: 9.5pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }
  .callout-box p {
    margin: 0 0 6px 0;
  }
  .callout-box p:last-child {
    margin-bottom: 0;
  }
  
  /* Sections */
  .section {
    margin-bottom: 13px;
  }
  .section-title {
    font-family: Arial, sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0 0 7px 0;
    padding-bottom: 3px;
    border-bottom: 1px solid #e2e8f0;
  }
  .subsection-title {
    font-family: Arial, sans-serif;
    font-size: 9.5pt;
    font-weight: 700;
    color: #1e293b;
    margin: 9px 0 5px 0;
  }
  p {
    margin: 0 0 7px 0;
    text-align: justify;
  }
  
  /* Bullet lists */
  ul.policy-list {
    margin: 4px 0 8px 0;
    padding-left: 20px;
  }
  ul.policy-list li {
    margin-bottom: 5px;
    line-height: 1.45;
  }
  
  /* Note highlight box */
  .note-box {
    background: #f1f5f9;
    border-left: 3px solid #64748b;
    padding: 6px 12px;
    margin: 6px 0 6px 0;
    font-size: 9pt;
  }
  
  /* Info Card */
  .info-card {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #0f172a;
    padding: 10px 14px;
    margin-top: 6px;
    margin-bottom: 12px;
    font-family: Arial, sans-serif;
    font-size: 9pt;
    line-height: 1.6;
  }
  
  /* Attestation Box at bottom of page 2 */
  .attestation-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #0f172a;
    padding: 10px 14px;
    margin-top: auto;
    margin-bottom: 10px;
    font-family: Arial, sans-serif;
  }
  .attestation-title {
    font-size: 8.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #0f172a;
    margin-bottom: 4px;
  }
  .attestation-desc {
    font-size: 8pt;
    color: #475569;
    line-height: 1.4;
  }
  
  /* Running Document Footer */
  .doc-footer {
    margin-top: auto;
    border-top: 1px solid #cbd5e1;
    padding-top: 6px;
    font-family: Arial, sans-serif;
    font-size: 8pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
  }
  
  a {
    color: #0f172a;
    text-decoration: underline;
  }
</style>
</head>
<body>

  <!-- PAGE 1 -->
  <div class="page">
    <div class="doc-header">
      <div class="header-left">
        <div class="category-eyebrow">Corporate Governance &amp; Privacy Compliance Standard</div>
        <h1 class="doc-title">PRIVACY POLICY</h1>
      </div>
      <table class="header-meta">
        <tr>
          <td class="label">Document ID:</td>
          <td class="val">POL-PRV-001</td>
        </tr>
        <tr>
          <td class="label">Entity:</td>
          <td class="val">FD System Holdings LLC</td>
        </tr>
        <tr>
          <td class="label">Effective Date:</td>
          <td class="val">November 5, 2026</td>
        </tr>
        <tr>
          <td class="label">Website:</td>
          <td class="val">https://fdsystemholdings.com</td>
        </tr>
      </table>
    </div>

    <!-- 1. Overview & Commitment to Privacy -->
    <div class="callout-box">
      <div class="callout-title">1. Overview &amp; Commitment to Privacy</div>
      <p>FD System Holdings LLC ("FD System Holdings," "we," "us," or "our") respects your privacy. Our website (fdsystemholdings.com) is designed as an informational static web property. We do not actively collect, harvest, store, sell, or monetize any personally identifiable information (PII) from visitors to our website.</p>
      <p>While we do not operate databases to track visitors, standard internet infrastructure and web browsers automatically process basic technical and operational metadata to deliver the site securely and reliably.</p>
    </div>

    <!-- 2. Information We Do Not Collect -->
    <div class="section">
      <div class="section-title">2. Information We Do Not Collect</div>
      <p>When you visit fdsystemholdings.com, FD System Holdings LLC does not:</p>
      <ul class="policy-list">
        <li>Require user registration, accounts, or logins.</li>
        <li>Deploy behavioral tracking pixels, third-party advertising cookies, or cross-site analytics trackers.</li>
        <li>Collect personal identifiers such as your name, physical address, phone number, or financial details through the website.</li>
        <li>Sell, rent, or trade visitor data to data brokers or third parties.</li>
      </ul>
    </div>

    <!-- 3. Basic Web Information Automatically Processed -->
    <div class="section">
      <div class="section-title">3. Basic Web Information Automatically Processed</div>
      <p>To render web pages, maintain network security, and ensure site performance, basic technical information is automatically handled in two ways:</p>
      
      <div class="subsection-title">A. Infrastructure &amp; Hosting Logs</div>
      <p>Our static web hosting and DNS infrastructure providers (such as GitHub Pages and Cloudflare) automatically record standard server access logs when your browser requests a page. This basic technical data includes:</p>
      <ul class="policy-list">
        <li><strong>IP Address:</strong> Temporarily logged to route traffic and mitigate DDoS attacks or malicious activity.</li>
        <li><strong>HTTP Request Metadata:</strong> Browser type and version (User-Agent string), operating system, referring URL, requested page path, and the date/time stamp of the request.</li>
      </ul>
      <div class="note-box">
        <strong>Note:</strong> FD System Holdings LLC does not download, aggregate, or link these infrastructure logs to identify individual users.
      </div>
    </div>

    <div class="doc-footer">
      <span>FD System Holdings LLC &mdash; Privacy Policy (POL-PRV-001)</span>
      <span>Page 1 of 2</span>
    </div>
  </div>

  <!-- PAGE 2 -->
  <div class="page">
    <div class="doc-header-sub">
      <span>FD System Holdings LLC &bull; Official Governance &amp; Privacy Compliance Series</span>
      <span>Document ID: POL-PRV-001</span>
    </div>

    <!-- 3B. Local Browser Storage & Caching -->
    <div class="section">
      <div class="subsection-title" style="margin-top: 0;">B. Local Browser Storage &amp; Caching</div>
      <p>Your web browser may automatically save basic site assets locally on your device&mdash;such as HTML, CSS, fonts, images, or basic display preferences (e.g., light/dark mode states)&mdash;via standard HTTP caching or localStorage. This information remains strictly on your device to speed up page load times and is never transmitted back to FD System Holdings LLC.</p>
    </div>

    <!-- 4. Direct Communications -->
    <div class="section">
      <div class="section-title">4. Direct Communications</div>
      <p>If you choose to contact us directly via an email link provided on the website (such as <a href="mailto:web@fdsystemholdings.com">web@fdsystemholdings.com</a>), we will receive your email address and any information you voluntarily include in your message. We use this information solely to respond to your inquiry and conduct standard business correspondence.</p>
    </div>

    <!-- 5. Third-Party Links -->
    <div class="section">
      <div class="section-title">5. Third-Party Links</div>
      <p>Our website may contain links to external websites or repositories (such as GitHub or LinkedIn). FD System Holdings LLC is not responsible for the privacy practices or content of external sites. We encourage you to review the privacy policies of any third-party sites you visit.</p>
    </div>

    <!-- 6. Changes to This Privacy Policy -->
    <div class="section">
      <div class="section-title">6. Changes to This Privacy Policy</div>
      <p>We may update this Privacy Policy periodically to reflect changes in our website operations or legal requirements. Any updates will be posted directly on this page with a revised Effective Date.</p>
    </div>

    <!-- 7. Contact Information -->
    <div class="section">
      <div class="section-title">7. Contact Information</div>
      <p>If you have any questions about this Privacy Policy or our practices, please contact us at:</p>
      <div class="info-card">
        <strong>FD System Holdings LLC</strong><br>
        Email: <a href="mailto:web@fdsystemholdings.com">web@fdsystemholdings.com</a><br>
        Website: <a href="https://fdsystemholdings.com">https://fdsystemholdings.com</a><br>
        Address: 8 The Green #27082, Dover, DE 19901
      </div>
    </div>

    <div class="attestation-box">
      <div class="attestation-title">Corporate Privacy &amp; Data Stewardship Commitment</div>
      <div class="attestation-desc">
        FD System Holdings LLC adheres to absolute data minimization principles. This static digital property operates without surveillance technologies, tracking beacons, third-party advertising cookies, or monetization of visitor telemetry.
      </div>
    </div>

    <div class="doc-footer">
      <span>FD System Holdings LLC &mdash; Privacy Policy (POL-PRV-001)</span>
      <span>Page 2 of 2</span>
    </div>
  </div>

</body>
</html>
"""

def find_browser():
    """Finds an installed Chromium-based browser (Edge, Chrome, or Chromium)."""
    # 1. Look in system PATH
    for name in ["msedge", "microsoft-edge", "chrome", "google-chrome", "chromium"]:
        path = shutil.which(name)
        if path:
            return path

    # 2. Known Windows paths
    windows_paths = [
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    ]
    for p in windows_paths:
        if os.path.isfile(p):
            return p

    # 3. Known macOS paths
    macos_paths = [
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for p in macos_paths:
        if os.path.isfile(p):
            return p

    # 4. Known Linux paths
    linux_paths = [
        "/usr/bin/microsoft-edge",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
    ]
    for p in linux_paths:
        if os.path.isfile(p):
            return p

    return None

def generate_pdf():
    browser_path = find_browser()
    if not browser_path:
        raise RuntimeError(
            "Could not find Microsoft Edge, Google Chrome, or Chromium. "
            "Please ensure a Chromium-based browser is installed."
        )
    print(f"Using browser: {browser_path}")

    # Determine paths relative to repository root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    final_pdf = os.path.join(repo_root, "assets", "legal", "Privacy-Policy.pdf")

    temp_dir = tempfile.gettempdir()
    temp_html = os.path.join(temp_dir, "Privacy-Policy-temp.html")
    temp_pdf = os.path.join(temp_dir, "Privacy-Policy-temp.pdf")

    try:
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE)

        cmd = [
            browser_path,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={temp_pdf}",
            f"file:///{temp_html.replace(os.sep, '/')}"
        ]

        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout.strip():
            print("Browser stdout:", result.stdout.strip())
        if result.stderr.strip():
            print("Browser stderr:", result.stderr.strip())

        if not os.path.exists(temp_pdf) or os.path.getsize(temp_pdf) == 0:
            raise RuntimeError(f"Failed to generate PDF via {os.path.basename(browser_path)}")

        file_size = os.path.getsize(temp_pdf)
        print(f"Generated PDF verified: {file_size} bytes")

        # Copy to target destination
        os.makedirs(os.path.dirname(final_pdf), exist_ok=True)
        shutil.copy2(temp_pdf, final_pdf)
        print(f"Successfully wrote {final_pdf} ({file_size} bytes)")

    finally:
        # Clean up temp files
        for temp_file in (temp_html, temp_pdf):
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception as e:
                    print(f"Temp cleanup notice for {temp_file}: {e}")

if __name__ == "__main__":
    generate_pdf()
