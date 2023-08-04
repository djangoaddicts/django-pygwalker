# Installation

The django-pygwalker package is available on Python Package Index (PyPI) and can be installed via pip with the following command:

```console
pip install django-pygwalker
```

<br/>

To use django-pygwalker in your project, add 'djangoaddicts.pygwalker' to INSTALLED_APPS in your settings.py file.

```python
INSTALLED_APPS = [
    ...
   'djangoaddicts.pygwalker',
]
```

<br/>

***NOTE:*** *adding djangoaddicts.pygwalker to INSTALLED_APPS is only required if you intend to use the built-in templates or the 'generic' PyGWalker view.*


<br/>

To include the generic PyGWalker view (creates the PyGWalker page from an upload of a csv file) add the following to your project-level urls.py:

```python
path("pygwalker/", include("djangoaddicts.pygwalker.urls"), ),
```

<br/>
