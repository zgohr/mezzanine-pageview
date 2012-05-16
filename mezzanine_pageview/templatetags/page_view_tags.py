from django import template
from .. page_processors import can_access

register = template.Library()

@register.filter
def can_access_link(user, page):
    return can_access(user, page)
