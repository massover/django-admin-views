from django.contrib import admin
from django.forms import forms, BooleanField

from admin_views.mixins import AdminViewMixin
from .models import Dog

class ExtraForm(forms.Form):
    foo = BooleanField()


class ExtraAdminView(AdminViewMixin):
    form_class = ExtraForm
    verbose_name = 'Extra View'


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass

