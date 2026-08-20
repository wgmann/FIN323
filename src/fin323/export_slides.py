from pathlib import Path
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

html = Path(sys.argv[1]).resolve()
pdf = html.with_suffix(".pdf")

# Enable Reveal slide numbers
html_text = html.read_text()
html_text = html_text.replace(
    'slideNumber: ""',
    'slideNumber: "c/t"'
)
html.write_text(html_text)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Reveal's PDF mode
    page.goto(html.as_uri() + "?print-pdf", wait_until="networkidle")

    page.pdf(
        path=str(pdf),
        prefer_css_page_size=True,
        print_background=True,
    )

    browser.close()

# Remove the final blank page
reader = PdfReader(pdf)
writer = PdfWriter()
for page in reader.pages[:-1]:
    writer.add_page(page)
with open(pdf, "wb") as f:
    writer.write(f)

print(f"Wrote {pdf}")