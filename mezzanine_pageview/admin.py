from django.contrib import admin
from models import PageViewGroup

class PageViewGroupAdmin(admin.ModelAdmin):
    list_display = ("group", "page")

admin.site.register(PageViewGroup, PageViewGroupAdmin)
