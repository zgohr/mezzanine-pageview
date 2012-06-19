#from django.http import Http404
#from mezzanine.pages.page_processors import processor_for
#from mezzanine.pages.models import Page
#from mezzanine.galleries.models import Gallery
from models import PageViewGroup

def can_access(user, page):
    """
    If the page has groups associated with it, the user
    must have access to the group
    """
    page_groups = PageViewGroup.objects.filter(page=page)
    if user.is_anonymous():
        return page_groups.count() == 0
    else:
        groups = page_groups.filter(group__in=user.groups.all())
    return page_groups.count() == 0 or groups.count() > 0

"""
@processor_for(Page)
def page_view(request, page):
"""
