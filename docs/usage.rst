=====
Usage
=====

To use Django Admin Views in a project, add it to your `INSTALLED_APPS`:

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
