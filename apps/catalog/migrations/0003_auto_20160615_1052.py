# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_images_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='category',
        ),
        migrations.AlterField(
            model_name='images',
            name='created_at',
            field=models.DateTimeField(help_text=b'Date when image created.', verbose_name=b'Created At', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='updated_at',
            field=models.DateTimeField(help_text=b'Date when image updated.', verbose_name=b'Updated At', auto_now=True),
        ),
    ]
