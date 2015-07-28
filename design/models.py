from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Design(models.Model):
    name = models.CharField(max_length=256)
    default = models.BooleanField(default=False)

    logo = models.ImageField(blank=True, null=True)
    logo_mobile = models.ImageField(blank=True, null=True)
    background_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
