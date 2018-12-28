from django.conf.urls import url
from django.contrib import admin

from dogs.admin import ExtraAdminView

from admin_views import router


router.register(r'extra-view/', ExtraAdminView, name='extra-admin-view')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/extra-view/', ExtraAdminView.as_view(), name='extra-admin-view'),
    url(r'^admin/', router.urls)
]

