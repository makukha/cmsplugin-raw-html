cmsplugin-raw-html
====================

Django CMS plugins to insert raw HTML as top-level or nested plugin.

This package adds a plugin named "Raw HTML" that can be inserted as a top level plugin directly into the page structure,
or as a nested plugin into the Text plugin.

Requirements
------------

Tested with
* Python 3.4.5
* Django 1.7.7
* django-cms 3.1.0rc1

Installation
------------

Add app to `settings.py`:

    INSTALLED_APPS = (
        ...
        'cmsplugin_raw_html',
        ...
        )

and run migration (Django 1.7):

    python manage.py migrate cmsplugin_raw_html

Credits
-------

The idea was inspired by https://github.com/mrj0/cmsplugin-html.
