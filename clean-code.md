# Clean Code

**Martin Fowler** is a famous person in developing clean code.

Book: Refactoring; improving the design of Existing code
by Martin Fowler, 2018


- readable
- easy to change

[PEP](https://peps.python.org/) (Python Enhancement Proposal)

[PEP8](https://peps.python.org/pep-0008/) - Style Guide For Python Code
- is not completely prescriptive
- there is not a deep discussion

[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

What is Functional Programming?

Resources to become master in Clean Code:

- [Clean code in Python: testdriven.io](https://testdriven.io/blog/clean-code-python/)
- Book: Refactoring; improving the design of Existing code by Martin Fowler, 2018
- Clean Code by Robert C. Martin

## Auto Formatters

### black
 CLI tool written in Python.

 to install black manually:
 - activate the virtual environment
 - pip install black
 - black --help

to format automatically on VS code:
- press command+shift+p
- search for format document
- use black on the opened box


- after that each time you just need to press command+shift_p
- and then search for format document

***Black modifies the file in place!**

How to set length of line?

How to set ruler?
- go to setting
- search for ruler
- add in settings.json in .vscode folder:

"editor.rulers": [
        {
            "color": "lightblue",
            "column": 79
        }
    ]

### linters: Pylint
not only works like black but also give use more qualitative recommendations

manually:
pip install pylint

integrate to VS code:
- go to setting
- search for pylint
- python > linting: pylint enabled

pylint --generate-rcfile > .pylintrc

pylint --disable=missing-function-docstring
or
"pylint.args": ["--disable=missing-function-docstring"]

### linters: flake8
supports a rich plugin system
[flake8 plugins](https://github.com/DmytroLitvinov/awesome-flake8-extensions)

def addition(number_a, number_b,):  # noqa: E302
or
flake8 --exclude=E302 unformatted_file.py
flake8 --ignore=E302 unformatted_file.py

How to install [darglint plugin]()?

### linters: [ruff](https://github.com/astral-sh/ruff)
[ruff website](https://beta.ruff.rs/docs/)

## Bash file
- create a file.sh
- insert at the first line: #!/bin/bash (when you write bash, it seems that you are typing on terminal)
- (if you write: "#!python" it runs the rest of the file as python code)
- then the file can be runned by: ./file.sh
- (if permission is denied just run: chmod +x file.sh)


# Pre-commit

## Git pre-commit hook
- go to .git/hook folder
- rename pre-commit.sample file to pre-commit
- run bash file there ($PWD returns the working directory) like:
  - ./check-code-quality.sh || exit 1

## [pre-commit CLI tool](https://pre-commit.com)
[supported hooks](https://pre-commit.com/hooks.html)
[nbQA for formatting jupyter notebook files](github.com/nbQA-dev/nbQA)

pip install pre-commit

pre-commit --help

to create a config file:

pre-commit sample-config > .pre-commit-config.yaml

to apply changes in .pre-commit-config.yaml file to git/hook.pre-commit:

pre-commit install

pre-commit autoupdate

pre-commit run --all-files

SKIP=black git commit -m "..." // a way to silent one of the hooks

git commit -m "..." --no-verify

# GitHub Action
