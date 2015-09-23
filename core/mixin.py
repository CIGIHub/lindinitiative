from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                PageChooserPanel)

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class FeatureMixin(models.Model):
    short_description = models.CharField(max_length=256, blank=False)
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

