"""Configuration file for the Sphinx documentation builder."""
import os

html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    os.environ.get("DOCS_BASE_URL", "gsid-verticals-docs.readthedocs.io"),
)
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "gsid-verticals-docs"

version = "1.0.0"
release = version
html_title = "Industries & Verticals"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_copy_source = True
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "instinct-design",
    "link_main_doc": True,
    "repository_url": "https://github.com/AMD-melliott/gsid-verticals-docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "nav_secondary_items": {
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm&#8482 Docs": "https://rocm.docs.amd.com",
        "AMD Instinct Systems & Infrastructure": "https://instinct.docs.amd.com",
    },
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

# Generate llms.txt and llms-full.txt after each build (the llms.txt standard,
# https://llmstxt.org/). See the rocm-docs-core guide:
# https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/llms.html
rocm_docs_generate_llms = True

exclude_patterns = [".venv"]
