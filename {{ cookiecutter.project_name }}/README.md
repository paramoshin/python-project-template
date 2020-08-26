

<h1 align='center'>
    {{ cookiecutter.project_name }}
</h1>

<h4 align='center'>
    {{ cookiecutter.description }}
</h4>

<div align="center">

[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.pre-commit-config.yaml)
</div>  

---

## How to use

### Set up

1. Make sure git is initialized in this directory:
```bash
git init
```
2. If you don't have poetry, run:
```bash
make get-poetry
```
3. Install poetry, nox and pre-commit hooks with one command:
```bash
make install
```

### Testing, formatting, linting, etc.
All commands are set up in makefile for easy usage.

1. Run safety checks:
```bash
make safety
```
2. Run tests:
* Unittests: `make pytest`
* Docstring tests: `make xdoctest`
* Both: `make tests`
3. Run pre-commit hooks (include `black`, `isort`, `pyupgrade`, `flakehell` and `mypy`) on all files: `make lint`
4. Create documentation from your code: `make docs`
5. Build your package: `make build`

