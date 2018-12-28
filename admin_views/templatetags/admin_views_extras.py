from django import template
from admin_views import router

register = template.Library()


@register.simple_tag
def get_admin_views():
    return router.admin_views
