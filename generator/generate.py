import json
import os

BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "docs\p")
# print(OUTPUT_DIR)

with open(os.path.join(BASE_DIR, "template.html"), encoding="utf-8") as f:
    template = f.read()

with open(os.path.join(BASE_DIR, "products.json"), encoding="utf-8") as f:
    products = json.load(f)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for p in products:
    html = template
    html = html.replace("{{TITLE}}", p["title"])
    html = html.replace("{{DESCRIPTION}}", p["description"])
    html = html.replace("{{IMAGE}}", p["image"])
    html = html.replace("{{AFFILIATE_URL}}", p["affiliate_url"])

    output_path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    # print(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Generated: {p['slug']}.html")



