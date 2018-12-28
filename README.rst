=============================
Django Admin Views
=============================

.. image:: https://badge.fury.io/py/django-admin-views.svg
    :target: https://badge.fury.io/py/django-admin-views

.. image:: https://travis-ci.org/massover/django-admin-views.svg?branch=master
    :target: https://travis-ci.org/massover/django-admin-views

.. image:: https://codecov.io/gh/massover/django-admin-views/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/massover/django-admin-views

Admin views

Documentation
-------------

The full documentation is at https://django-admin-views.readthedocs.io.

Quickstart
----------

Install Django Admin Views::

    pip install django-admin-views

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'admin_views.apps.AdminViewsConfig',
        ...
    )

Add Django Admin Views's URL patterns:

.. code-block:: python

    from admin_views import urls as admin_views_urls


    urlpatterns = [
        ...
        url(r'^', include(admin_views_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
