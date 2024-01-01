# Contributing to django-pygwalker

First off, thank you for considering contributing to django-pygwalker!

The following is a set of guidelines for contributing to this project. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
3. [Development Setup](#development-setup)
4. [Style Guide](#style-guide)
5. [License](#license)

<br/>

## Code of Conduct

This project and everyone participating in it are governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [maintainer email].

<br/>

## How Can I Contribute?

### Reporting Bugs

- Before creating bug reports, please check the [existing issues](https://github.com/djangoaddicts/django-pygwalker/issues) as you might find that the issue has already been reported.
- When creating a bug report, please include a clear and concise description of the problem and steps to reproduce it.

### Suggesting Enhancements

- Before creating enhancement suggestions, please check the [list of open issues](https://github.com/djangoaddicts/django-pygwalker/issues) as you might find that the suggestion has already been made.
- When creating an enhancement suggestion, please provide a detailed description and, if possible, an implementation proposal.

### Pull Requests

- Provide a clear and concise description of your pull request.
- Ensure you have tested your changes thoroughly.
- Add/update unittests as nessessary.
- Make sure code quaility tools run successfully. 

    Merging contributions requires passing the checks configured with the CI. This includes running tests, linters, and other code quaility tools successfully on the currently officially supported Python and Django versions.

<br/>

## Development

You can contribute to this project forking it from GitHub and sending pull requests.

First [fork](https://help.github.com/en/articles/fork-a-repo) the
[repository](https://github.com/djangoaddicts/django-pygwalker) and then clone it:

```shell
git clone git@github.com:<you>/django-pygwalker.git
```

Create a virtual environment and install dependancies:

```shell
cd django-pygwalker
python -m venv venv
source venv/bin/activate
pip install .[dev]
```

Unit tests are located under the tests directory and can be executed via pytest:

```shell
pytest
```


<br/>

## Style Guide

Follow the coding style outlined in [STYLE_GUIDE.md](STYLE_GUIDE.md).

<br/>

## License

By contributing, you agree that your contributions will be licensed under the [GNU-3 license](../LICENSE).
