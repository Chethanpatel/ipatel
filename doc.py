# Step 1: Generate the folder structure and config for MkDocs
import os

docs_structure = {
    "docs/index.md": "# ipenrich\n\nA fast IP and ASN enrichment tool that works offline after initial database download.\n\n- 🌍 Enrich IPs with ASN, Country, and Owner\n- 📦 Lookup ASN and its IP ranges\n- ⚡ CLI and Python API support\n- 🚀 Works offline after DB download\n- 🔁 Auto-detects stale DB and warns to update",
    "docs/cli.md": "# CLI Usage\n\n```bash\nipenrich -i 8.8.8.8\nipenrich -a 15169\nipenrich --update-db\nipenrich --version\n```",
    "docs/api.md": "# Python API Usage\n\n```python\nfrom ipenrich.enrich import enrich_ip\nfrom ipenrich.asn import get_asn, get_owner\n\nprint(enrich_ip(\"8.8.8.8\"))\nprint(get_owner(\"1.1.1.1\"))\n```",
    "docs/update.md": "# Updating the Database\n\nTo download or refresh the IP to ASN database:\n\n```bash\nipenrich --update-db\n```"
}

mkdocs_config = """site_name: ipenrich
repo_url: https://github.com/chethanpatel/ipenrich
theme:
  name: material
  features:
    - navigation.instant
    - navigation.sections
    - navigation.tabs
    - content.code.copy
markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
"""

# Write files
os.makedirs("docs", exist_ok=True)
for path, content in docs_structure.items():
    with open(path, "w") as f:
        f.write(content)

with open("mkdocs.yml", "w") as f:
    f.write(mkdocs_config)

"✅ MkDocs structure and config created!"
