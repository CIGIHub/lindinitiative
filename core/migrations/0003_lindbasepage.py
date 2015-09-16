# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_homepage_number_homepage_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='LindBasePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('short_description', models.CharField(max_length=256, blank=True)),
                ('button_text', models.CharField(max_length=256, blank=True)),
                ('button_link', models.CharField(max_length=256, blank=True)),
                ('button_external', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
