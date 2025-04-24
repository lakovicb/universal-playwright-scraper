# notebook_generator.py

import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from datetime import datetime
import os
from urllib.parse import urlparse


def create_notebook_with_analysis(url: str, output_dir="/home/lakov/projects/llm_engineering/community-contributions/playwright-bojan/notebooks"):
    nb = new_notebook()

    # Cell 1: Markdown intro
    intro_lines = [
        "# ✅ Playwright Scraper Showcase (Auto-Generated)",
        "",
        "This notebook demonstrates asynchronous scraping and",
        "summarization of:",
        "",
        f"**URL:** `{url}`"
    ]
    nb.cells.append(new_markdown_cell("\n".join(intro_lines)))

    # Cell 2: Setup and imports (PEP8 compliant)
    code_imports_lines = [
        "from pathlib import Path",
        "import os",
        "import importlib",
        "import asyncio",
        "import nest_asyncio",
        "",
        "nest_asyncio.apply()",
        "",
        "# Add scraper module path",
        "scraper_path = Path(\"/home/lakov/projects/llm_engineering/\") / \"community-contributions/playwright-bojan\"",
        "if str(scraper_path) not in sys.path:",
        "    import sys",
        "    sys.path.insert(0, str(scraper_path))",
        "",
        "# Clear cache if needed",
        "if 'openai_scraper_playwright' in sys.modules:",
        "    del sys.modules['openai_scraper_playwright']",
        "",
        "from openai_scraper_playwright import analyze_content"
    ]
    nb.cells.append(new_code_cell("\n".join(code_imports_lines)))

    # Cell 3: Run analysis and show markdown output
    analysis_lines = [
        f"result = await analyze_content(url=\"{url}\")",
        "from IPython.display import Markdown, display",
        "display(Markdown(result))"
    ]
    nb.cells.append(new_code_cell("\n".join(analysis_lines)))

    # Determine file name based on domain name
    domain = urlparse(url).netloc.split(".")[0].capitalize()
    filename = f"Playwright_Summary_{domain}.ipynb"

    # Save notebook
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"Notebook saved to: {path}")


if __name__ == "__main__":
    test_url = input("Enter URL to scrape: ")
    create_notebook_with_analysis(test_url)
