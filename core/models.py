from __future__ import absolute_import, unicode_literals

from basic_site import models as basic_site_models
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                PageChooserPanel)
from wagtail.wagtailcore.models import Page

from blog.models import BlogIndexPage, BlogPage
from core.mixin import FeatureMixin, PaginatedListPageMixin
from micro.models import MicroPage


class LindBasePage(Page, basic_site_models.BasePage, FeatureMixin):
    def __init__(self, *args, **kwargs):
        super(LindBasePage, self).__init__(*args, **kwargs)
        for field in self._meta.fields:
            if field.name == 'first_published_at':
                field.editable = True
                field.blank = True

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    promote_panels = Page.promote_panels + FeatureMixin.promote_panels

    settings_panels = [FieldPanel('first_published_at'), ] + Page.settings_panels


class PageList(models.Model):

    class Meta:
        abstract = True

    def pages(self):
        blog_content_type = ContentType.objects.get_for_model(
            BlogPage)
        page_content_type = ContentType.objects.get_for_model(
            LindBasePage)

        pages = Page.objects.live().filter(
            models.Q(content_type=blog_content_type)
            | models.Q(content_type=page_content_type)
        )

        pages = pages.order_by('-first_published_at')
        return pages


class SiteIndexPage(PaginatedListPageMixin, Page, PageList):
    subpage_types = [
        LindBasePage,
        BlogIndexPage,
        MicroPage,
    ]

    posts_per_page = models.IntegerField(default=10)
    counter_field_name = 'posts_per_page'
    counter_context_name = 'posts'

    @property
    def subpages(self):

        all_pages = self.pages()
        page_list = []

        for page in all_pages.all():
            typed_page = page.content_type.get_object_for_this_type(
                id=page.id)
            page_list.append(typed_page)

        return page_list


SiteIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('posts_per_page'),
]


@python_2_unicode_compatible
class HomePage(Page, PageList):
    subpage_types = [
        LindBasePage,
        BlogIndexPage,
        SiteIndexPage,
        MicroPage,
    ]

    featured_item = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    number_homepage_items = models.IntegerField(default=3, verbose_name="Items on Homepage")
    more_link = False

    def latest(self):

        latest = self.pages().exclude(pk=self.featured_item.pk)[:self.number_homepage_items]
        return latest

    def more_link(self):

        if len(self.pages()) > self.number_homepage_items:
            more_link = True

        return more_link

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
