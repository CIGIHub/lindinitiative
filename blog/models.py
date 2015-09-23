from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from core.mixin import FeatureMixin, PaginatedListPageMixin


class BlogPage(Page, FeatureMixin):
    body = RichTextField()
    date = models.DateField("Post date")
    author = models.TextField(max_length=512, blank=True)

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('author'),
    FieldPanel('body', classname="full"),
]

BlogPage.promote_panels = Page.promote_panels + FeatureMixin.promote_panels

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

BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('posts_per_page'),
]

BlogIndexPage.promote_panels = Page.promote_panels
