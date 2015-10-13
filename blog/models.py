from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from core.mixin import FeatureMixin, PaginatedListPageMixin


class BlogPage(Page, FeatureMixin):
    body = RichTextField()
    date = models.DateField("Post date")
    author = models.TextField(max_length=512, blank=True)

    def __init__(self, *args, **kwargs):
        super(BlogPage, self).__init__(*args, **kwargs)
        for field in self._meta.fields:
            if field.name == 'first_published_at':
                field.editable = True
                field.blank = True

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = Page.promote_panels + FeatureMixin.promote_panels
    settings_panels = [FieldPanel('first_published_at'), ] + Page.settings_panels


class BlogIndexPage(PaginatedListPageMixin, Page):
    subpage_types = [
        BlogPage,
    ]

    intro = RichTextField(blank=True)
    posts_per_page = models.IntegerField(default=10)
    counter_field_name = 'posts_per_page'
    counter_context_name = 'posts'

    @property
    def subpages(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by('-date')

        return blogs

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('posts_per_page'),
    ]

    promote_panels = Page.promote_panels
