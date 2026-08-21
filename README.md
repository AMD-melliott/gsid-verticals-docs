# GSID Industries & Verticals documentation

Staging repo for the Industries & Verticals content migrated out of
[instinct-docs](https://github.com/ROCm/instinct-docs) (see
[MAT-120](https://linear.app/amd-melliott/issue/MAT-120)). Covers computer vision, data science, life science,
finance, and ISV simulation/modeling applications for AMD Instinct GPUs. For core ROCm software and API
documentation, see [ROCm documentation](https://rocm.docs.amd.com). For deploying and operating AMD Instinct GPUs
at scale, see the [AMD Instinct Systems & Infrastructure documentation](https://instinct.docs.amd.com).

This repo is currently staged under the `AMD-melliott` account pending creation of the permanent `ROCm/gsid-verticals-docs`
repo and its ReadTheDocs project.

## Documentation build guide

This guide provides information for developers who want to contribute to this documentation site. The
documentation uses [rocm-docs-core](https://github.com/ROCm/rocm-docs-core) as the base. The following guide shows
how you can build and access the documentation locally for testing.

### Building and accessing the documentation

- Create a Python Virtual Environment (optional, but recommended).

 ```bash
 python3 -m venv .venv/docs
 ```

- Activate the Virtual Environment.

 ```bash
 source .venv/docs/bin/activate # For Linux

 source .venv/docs/Scripts/activate # For Windows
 ```

- Install the required packages for the documentation.

 ```bash
 pip install -r docs/sphinx/requirements.txt
 ```

- Build the documentation.

 ```bash
 python3 -m sphinx -b html -d _build/doctrees -D language=en ./docs docs/_build/html
 ```

- Serve the documentation locally on port 8000.

 ```bash
 python3 -m http.server -d ./docs/_build/html/
 ```

- You can now view the documentation site by going to http://localhost:8000.

### Auto-building the documentation

- Install Sphinx Autobuild package

 ```bash
 pip install sphinx-autobuild
 ```

- Run the autobuild (will also serve the documentation on port 8000 automatically).

 ```bash
 sphinx-autobuild -b html -d _build/doctrees -D language=en ./docs docs/_build/html --ignore "docs/_build/*" --ignore "docs/sphinx/_toc.yml" --ignore "docs/sphinx/requirements.txt"
 ```
