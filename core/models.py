from __future__ import absolute_import, unicode_literals

from basic_site import models as basic_site_models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                PageChooserPanel)
from wagtail.wagtailcore.models import Page

from core.mixin import FeatureMixin
from blog.models import BlogPage


@python_2_unicode_compatible
class HomePage(Page):

    featured_item = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    number_homepage_items = models.IntegerField(default=3, verbose_name="Items on Homepage")

    def latest(self):

        blog_content_type = ContentType.objects.get_for_model(
            BlogPage)
        page_content_type = ContentType.objects.get_for_model(
            LindBasePage)

        latest = Page.objects.live().filter(
            models.Q(content_type=blog_content_type)
            | models.Q(content_type=page_content_type)
        )
        latest = latest.exclude(pk=self.featured_item.pk)[:self.number_homepage_items]

        return latest

    def __str__(self):
        return self.title

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                PageChooserPanel("featured_item", "wagtailcore.Page"),
            ],
            heading="Main Feature"
        ),
        MultiFieldPanel(
            [
                FieldPanel("number_homepage_items"),
            ],
            heading="Homepage Feed"
        ),
    ]


class LindBasePage(Page, basic_site_models.BasePage, FeatureMixin):
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    promote_panels = Page.promote_panels + FeatureMixin.promote_panels


class SiteIndexPage(Page):

    @property
    def pages(self):

        pages = Page.objects.live().order_by('-first_published_at').exclude(title='Root').exclude(pk=self.pk)
        return pages

SiteIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
]
