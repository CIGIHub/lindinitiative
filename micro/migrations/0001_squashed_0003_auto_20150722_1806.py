# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import modelcluster.fields
import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'micro', '0001_initial'), (b'micro', '0002_auto_20150722_1759'), (b'micro', '0003_auto_20150722_1806')]

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='MircoPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MicroSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('heading', models.CharField(max_length=512)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('button_text', models.CharField(max_length=256, blank=True)),
                ('button_link', models.CharField(max_length=256, blank=True)),
                ('button_external', models.BooleanField(default=False)),
                ('page', modelcluster.fields.ParentalKey(related_name='sections', to='micro.MircoPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='MircoPage',
            new_name='MicroPage',
        ),
    ]
