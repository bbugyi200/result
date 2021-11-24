# result

**A fully type-annotated Rust-like Result type for Python.**

## Badges 📛

project status badges:

[![CI Workflow](https://github.com/bbugyi200/result/actions/workflows/ci.yml/badge.svg)](https://github.com/bbugyi200/result/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/bbugyi200/result/branch/master/graph/badge.svg)](https://codecov.io/gh/bbugyi200/result)
[![Documentation Status](https://readthedocs.org/projects/result/badge/?version=latest)](https://result.readthedocs.io/en/latest/?badge=latest)
[![Package Health](https://snyk.io/advisor/python/python-result/badge.svg)](https://snyk.io/advisor/python/python-result)

version badges:

[![Project Version](https://img.shields.io/pypi/v/python-result)](https://pypi.org/project/python-result/)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-result)](https://pypi.org/project/python-result/)
[![Cookiecutter: cc-python](https://img.shields.io/static/v1?label=cc-python&message=2021.10.03&color=d4aa00&logo=cookiecutter&logoColor=d4aa00)](https://github.com/bbugyi200/cc-python)
[![Docker: bbugyi/python](https://img.shields.io/static/v1?label=bbugyi%20%2F%20python&message=2021.09.25&color=8ec4ad&logo=docker&logoColor=8ec4ad)](https://github.com/bbugyi200/docker-python)

tools / frameworks used by test suite (i.e. used by `make test`):

[![Framework: pytest](https://img.shields.io/badge/framework-pytest-a76465)](https://github.com/pytest-dev/pytest)
[![Framework: doctest](https://img.shields.io/badge/framework-doctest-66a6f6)](https://docs.python.org/3/library/doctest.html)
[![Runner: tox](https://img.shields.io/badge/runner-tox-9da246)](https://github.com/tox-dev/tox)
[![Types: typeguard](https://img.shields.io/badge/types-typeguard-3a7163)](https://github.com/agronholm/typeguard)
[![Mocks: pytest-mock](https://img.shields.io/static/v1?label=mocks&message=pytest-mock&color=9c70d7)](https://github.com/pytest-dev/pytest-mock)
[![Snapshots: syrupy](https://img.shields.io/static/v1?label=snapshots&message=syrupy&color=436fa8)](https://github.com/tophat/syrupy)

linters used to maintain code quality (i.e. used by `make lint`):

[![Linter: pylint](https://img.shields.io/badge/linter-pylint-ffff00)](https://github.com/PyCQA/pylint)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-008080)](https://github.com/PyCQA/flake8)
[![Types: mypy](https://img.shields.io/badge/types-mypy-cd00cd)](https://github.com/python/mypy)
[![Docstrings: pydocstyle](https://img.shields.io/badge/docstrings-pydocstyle-AFD3E6)](https://github.com/PyCQA/pydocstyle)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-ef8336)](https://github.com/PyCQA/isort)

tools / frameworks used to render documentation (i.e used by `make build-docs`):

[![Rendered By: sphinx](https://img.shields.io/badge/rendered%20by-sphinx-9cc676)](https://github.com/sphinx-doc/sphinx)
[![Hosted On: ReadTheDocs](https://img.shields.io/badge/hosted%20on-ReadTheDocs-e08839)](https://docs.readthedocs.io/en/stable/)
[![Types: sphinx-autodoc-typehints](https://img.shields.io/static/v1?label=API&message=sphinx-autodoc-typehints&color=9c70d7)](https://github.com/agronholm/sphinx-autodoc-typehints)
[![Markdown: m2r2](https://img.shields.io/badge/markdown-m2r2-8e1e3d)](https://github.com/CrossNox/m2r2)

miscellaneous tools used to maintain this project:

[![Cookiecutter Updates: cruft](https://img.shields.io/badge/cc%20updates-cruft-6a4aef)](https://github.com/cruft/cruft)
[![Requirements: pip-tools](https://img.shields.io/static/v1?label=requirements&message=pip-tools&color=a77bb5)](https://github.com/jazzband/pip-tools)
[![Releases: bump2version](https://img.shields.io/badge/releases-bump2version-163b1a)](https://github.com/c4urself/bump2version)
[![Versioning: setuptools_scm](https://img.shields.io/static/v1?label=versioning&message=setuptools-scm&color=f61a61)](https://github.com/pypa/setuptools_scm)


## Installation 🗹

To install `python-result` using [pip][9], run the following
commands in your terminal:

``` shell
python3 -m pip install --user python-result  # install result
```

If you don't have pip installed, this [Python installation guide][10] can guide
you through the process.


## Useful Links 🔗

* [API Reference][3]: A developer's reference of the API exposed by this
  project.
* [cc-python][4]: The [cookiecutter][5] that was used to generate this project.
  Changes made to this cookiecutter are periodically synced with this project
  using [cruft][12].
* [CHANGELOG.md][2]: We use this file to document all notable changes made to
  this project.
* [CONTRIBUTING.md][7]: This document contains guidelines for developers
  interested in contributing to this project.
* [Create a New Issue][13]: Create a new GitHub issue for this project.
* [Documentation][1]: This project's full documentation.


[1]: https://result.readthedocs.io/en/latest
[2]: https://github.com/bbugyi200/result/blob/master/CHANGELOG.md
[3]: https://result.readthedocs.io/en/latest/modules.html
[4]: https://github.com/bbugyi200/cc-python
[5]: https://github.com/cookiecutter/cookiecutter
[6]: https://docs.readthedocs.io/en/stable/
[7]: https://github.com/bbugyi200/result/blob/master/CONTRIBUTING.md
[8]: https://github.com/bbugyi200/result
[9]: https://pip.pypa.io
[10]: http://docs.python-guide.org/en/latest/starting/installation/
[11]: https://github.com/pypa/pipx
[12]: https://github.com/cruft/cruft
[13]: https://github.com/bbugyi200/result/issues/new/choose
