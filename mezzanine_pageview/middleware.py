from django.http import Http404
from page_processors import can_access
from mezzanine.pages.models import Page

class PageViewMiddleware(object):
    """
    Mezzanine does not allow page_processors on a generic Page
    so for the time being we're going to use middleware to
    throw a 404 error if the user is not in the necessary group
    """
    def process_request(self, request):
        slug = request.path
        if slug != "/":
            slug = slug.strip("/")
        pages_for_user = Page.objects.published(request.user)
        try:
            page = pages_for_user.get(slug=slug)
            if not can_access(request.user, page):
                raise Http404
        except Page.DoesNotExist:
            pass
        return {}
