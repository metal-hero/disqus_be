# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='site_url',
            field=models.CharField(default='youtube.com', max_length=150),
            preserve_default=False,
        ),
    ]
