# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='ejemplo'),
            preserve_default=False,
        ),
    ]
