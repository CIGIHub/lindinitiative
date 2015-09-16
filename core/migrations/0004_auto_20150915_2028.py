# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('core', '0003_lindbasepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lindbasepage',
            name='id',
        ),
        migrations.AddField(
            model_name='lindbasepage',
            name='page_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='wagtailcore.Page'),
            preserve_default=False,
        ),
    ]
