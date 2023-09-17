# django-pygwalker
![](https://img.shields.io/pypi/v/django-pygwalker?color=blue) 
[![Downloads](https://static.pepy.tech/badge/django-pygwalker)](https://pepy.tech/project/django-pygwalker)
![](https://img.shields.io/pypi/status/django-pygwalker)

[![Maintainability](https://api.codeclimate.com/v1/badges/23aa8dc3c2e30ac40cb4/maintainability)](https://codeclimate.com/github/djangoaddicts/django-pygwalker/maintainability)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7682/badge)](https://bestpractices.coreinfrastructure.org/projects/7682)

![PyPI - Python](https://img.shields.io/pypi/pyversions/django-pygwalker)
![PyPI - Django](https://img.shields.io/pypi/djversions/django-pygwalker)



This utility creates user interfaces for visual analysis using PyGWalker in your django application. A PyGWalker page can be created from a Django queryset, a static csv file, or an uploaded csv file.

For more information on PyGWalker see the github repo available here: https://github.com/Kanaries/pygwalker 


<br/>

## Code Quality
| Workflow | Description             | Status                                                                       |
|----------|-------------------------|------------------------------------------------------------------------------|
|Bandit|security checks|![Bandit](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/bandit.yaml/badge.svg)|
|Black|code formatting|![Black](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/black.yaml/badge.svg)|
|CodeQL|security analysis|[![CodeQL](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/github-code-scanning/codeql)|
|Coveralls|code coverage status|![Coveralls](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/coveralls.yaml/badge.svg)|
|Isort|python import ordering|![Isort](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/isort.yaml/badge.svg)|
|Mypy|static type checking|![Mypy](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/mypy.yaml/badge.svg)|
|Pytest|unit testing|![Pytest](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/pytest.yaml/badge.svg)|
|Radon|code complexity analysis|![Radon](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/radon.yaml/badge.svg)|
|Ruff|static code analysis|![Ruff](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/ruff.yaml/badge.svg)|
|Safety|dependency scanner|![Saftey](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/safety.yaml/badge.svg)|
|Tox|python/django versions testing|![Tox](https://github.com/djangoaddicts/django-pygwalker/actions/workflows/tox.yaml/badge.svg)|


### Code Coverage 
[![Coverage Status](https://coveralls.io/repos/github/djangoaddicts/django-pygwalker/badge.svg)](https://coveralls.io/github/djangoaddicts/django-pygwalker)

Dashboard:
https://coveralls.io/github/djangoaddicts/django-pygwalker


<br/>

## Documentation
[![Documentation Status](https://readthedocs.org/projects/django-pygwalker/badge/?version=latest)](https://django-pygwalker.readthedocs.io/en/latest/?badge=latest)

Full documentation can be found on http://django-pygwalker.readthedocs.org. 

Documentation source files are available in the docs folder.


<br/>

## License
django-pygwalker is licensed under the GNU-3 license (see the LICENSE file for details).

https://github.com/djangoaddicts/django-pygwalker/blob/main/LICENSE


<br/>

## Installation 
- install via pip:
    ``` 
    pip install django-pygwalker
    ```
- add the following to your INSTALLED_APPS in settings.py:

    ```python 
    djangoaddicts.pygwalker
    ```

    ***NOTE:*** *adding djangoaddicts.pygwalker to INSTALLED_APPS is only required if you intend to use the built-in templates or the 'generic' PyGWalker view.* 

- to include the generic PyGWalker view (creates the PyGWalker page from an upload of a csv file) add the following to your project-level urls.py:

    ```python
    path("pygwalker/", include("djangoaddicts.pygwalker.urls"), ),
    ```


<br/>

## Features

### PygWalkerView
The PygWalkerView renders a page containing PyGWalker html. This view takes a queryset parameter and includes all data in the queryset for visualizations. By default fields defined in the model will be included. To exclude fields or include additional fields (such as related fields), use the field_list parameter to specify exact fields desired for visualizations.  

A Bootstrap 5 template is included, but can be overwritten using the template_name parameter. 

#### Parameters
- **field_list:** list of model fields to include (defaults to fields defined in the model)
- **queryset:** queryset providing data available to visualization
- **theme:** PyGWalker theme to use for pyg html (defaults to "media")
- **title:** title used on html render
- **template_name:** template used when rendering page; (defaults to pygwalker/bs5/pygwalker.html)


<br/>

## Usage Examples

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
```

#### Explicitly Defined Fields

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
    title = "MyModel Data Analysis"
    theme = "light"
    field_list = ["name", "some_field", "some_other__related_field", "id", "created_at", "updated_at"]
```

#### Custom Template
Custom views/templates can be used to override the Bootstrap 5 templates provided by default view. Here is an example:

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
    template_name = "my_custom_template.html"
```
