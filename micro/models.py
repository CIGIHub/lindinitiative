from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page


class MicroPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('sections', label="Sections"),
    ]


class Section(models.Model):
    heading = models.CharField(max_length=512)
    body = RichTextField()
    button_text = models.CharField(max_length=256, blank=True)
    button_link = models.CharField(max_length=256, blank=True)
    button_external = models.BooleanField(default=False)

    content_panels = [
        FieldPanel('heading'),
        FieldPanel('body', classname="full"),
        FieldPanel('button_text'),
        FieldPanel('button_link'),
        FieldPanel('button_external'),
    ]

    class Meta:
        abstract = True


class MicroSection(Orderable, Section):
    page = ParentalKey(MicroPage, related_name='sections')
