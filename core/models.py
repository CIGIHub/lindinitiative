from __future__ import absolute_import, unicode_literals

from basic_site import models as basic_site_models
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                PageChooserPanel)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class FeatureMixin(models.Model):
    short_description = models.CharField(max_length=256, blank=True)
    button_text = models.CharField(max_length=256, blank=True)
    button_link = models.CharField(max_length=256, blank=True)
    button_external = models.BooleanField(default=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    promote_panels = [
        FieldPanel('short_description'),
        ImageChooserPanel('image'),
        MultiFieldPanel(
            [
                FieldPanel('button_text'),
                FieldPanel('button_link'),
                FieldPanel('button_external'),
            ]
        ),
    ]

    class Meta:
        abstract = True


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
        return Page.objects.live().order_by('-first_published_at')[:self.number_homepage_items]

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
