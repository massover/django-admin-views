
from django.conf.urls import url
from django.urls import include, reverse


class AdminView(object):
    def __init__(self, regex, view, name, kwargs, verbose_name):
        self.regex = regex
        self.view = view
        self.name = name
        self.kwargs = kwargs
        self.verbose_name = verbose_name

    def reverse(self):
        return reverse(self.name)


class AdminViewRouter(object):
    def __init__(self):
        self.admin_views = []

    def register(self, regex, view, kwargs=None, name=None):
        if name is None:
            name = view.__name__
        admin_view = AdminView(
            regex=regex,
            view=view,
            name=name,
            kwargs=kwargs,
            verbose_name=view.verbose_name,
        )
        self.admin_views.append(admin_view)

    @property
    def urls(self):
        urls = []
        for admin_view in self.admin_views:
            _url = url(
                admin_view.regex,
                admin_view.view.as_view(),
                kwargs=admin_view.kwargs,
                name=admin_view.name
            )
            urls.append(_url)
        return include(urls)


router = AdminViewRouter()



