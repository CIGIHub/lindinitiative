from __future__ import absolute_import, unicode_literals

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
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


class PaginatedListPageMixin(object):
    '''
    To use this mixing you need to define counter_field_name as the name of the field with
    the items per page and counter_context_name for the template. See jobs/models.py for an example
    '''
    def get_paginator(self, objects=None):
        if objects is None:
            objects = self.subpages
        return Paginator(objects, getattr(self, self.counter_field_name))

    def get_context(self, request):
        # import pdb; pdb.set_trace();

        page = request.GET.get('page')
        paginator = self.get_paginator()

        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        context = super(PaginatedListPageMixin, self).get_context(request)
        context[self.counter_context_name] = objects
        return context

    def get_cached_paths(self):
        yield '/'

        # Yield one URL per page in the paginator to make sure all pages are purged
        for page_number in range(2, self.get_paginator().num_pages + 1):
            yield '/?page=' + str(page_number)
