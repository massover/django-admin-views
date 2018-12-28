from django.contrib.admin import helpers
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _


class AdminViewMixin(SuccessMessageMixin, UserPassesTestMixin, FormView):
    form_class = None
    template_name = 'admin_views/admin_view.html'
    success_url = None
    success_message = _('Success')
    _is_admin_view = True

    def __init__(self, *args, **kwargs):
        super(AdminViewMixin, self).__init__(*args, **kwargs)
        self.name = kwargs.get('name')

    def test_func(self):
        return self.request.user.is_staff

    def get_name(self):
        return self.name

    def get_success_url(self):
        if self.success_url is None:
            return self.request.build_absolute_uri()

        return self.success_url

    def get_context_data(self, **kwargs):
        context_data = super(AdminViewMixin, self).get_context_data(**kwargs)
        adminform = helpers.AdminForm(
            context_data['form'],
            list([(None, {'fields': context_data['form'].base_fields})]),
            {},
        )
        context_data['adminform'] = adminform
        context_data['name'] = self.get_name()
        return context_data
