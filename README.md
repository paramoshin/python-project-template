<h1 align='center'>
    Cookiecutter Python Project Template • :cookie: • :snake:
</h1>

<h4 align='center'>
<a href=https://cookiecutter.readthedocs.io/en/latest>Cookiecutter</a> template for python projects with modern Python tooling.
</h4>

<div align="center">

[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/paramoshin/python-project-template/pulls/?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/paramoshin/python-project-template/blob/master/.pre-commit-config.yaml)

</div>  

---

## Features

- Supports `python3.7+`
- [`Poetry`](https://github.com/python-poetry/poetry) to manage Python packaging and dependencies
- Unit testing with [`pytest`](https://github.com/pytest-dev/pytest)
- Code coverage with [`Coverage.py`](https://coverage.readthedocs.io/en/coverage-5.2.1/)
- Test automation with [`Nox`](https://nox.thea.codes/en/stable/``)
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks that include:
    - [`Flakehell`](https://flakehell.readthedocs.io/) with linting plugins
    - [`Safety`](https://github.com/pyupio/safety) to check installed dependencies for known security vulnerabilities
    - [`Mypy`](https://mypy.readthedocs.io) for optional static typing
    - Code formatting with [`black`](https://github.com/psf/black), [`isort`](https://github.com/PyCQA/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade)
    - [`Darglint`](https://github.com/terrencepreilly/darglint) to check if docstrings match actual functions/methods
- [`Xdoctest`](https://xdoctest.readthedocs.io/en/latest/) to run tests in docstrings
- [`Pdoc3`](https://github.com/pdoc3/pdoc) for automatic documentation generation
- Always [`up-to-date`](https://github.com/paramoshin/python-project-template/pulls/?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- [`Makefile`](https://github.com/paramoshin/python-project-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile) with commands set up for security checks, linting, code formatting, codestyle checks, testing, building etc. 
---
## How to use:

### Installation:

1. Install cookiecutter with:

    ```bash
    brew install cookiecutter
    ```
    or
    ```bash
    pip install cookiecutter
    ```
2. Create a project with:
    ```bash
    gh:paramoshin/python-project-template
    ```
### Initialization  
You will be asked to fill some information for generating your project.

The input variables, with their default values are:

|     **Parameter**     |      **Default value**      | **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`        | `project_name`            | The name of the project.                 |
| `description` | ` ` | Brief description of your project.                                                                                                                                            |
| `author`        | `author` | Name of the project author                                        |
| `license`             | `No license file`                       | Type of license. One of `No license file`, `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`.                                                                                     |
| `version`             | `0.1.0`                     | An initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification.                                                           |
| `email`               | based on the `author` | Email to specify the ownership of the project in `pyproject.toml`.                                 |

The entered values will be saved in the `cookiecutter-config-file.yml` file and propagated into `pyproject.toml`.

--- 

## Acknowledgements

This template was inspired by:

- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

- [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter)
- [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
- [Audreyr's `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)
- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [TezRomacH's Python Packages Project Generator](https://github.com/TezRomacH/python-package-template)