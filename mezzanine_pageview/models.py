from django.db import models
from django.contrib.auth.models import Group
from mezzanine.pages.models import Page

class PageViewGroup(models.Model):
    class Meta:
        verbose_name = "Page View Group"
        verbose_name_plural = "Page View Groups"

    group = models.ForeignKey(Group, related_name="viewablepages")
    page = models.ForeignKey(Page, related_name="viewgroup")
