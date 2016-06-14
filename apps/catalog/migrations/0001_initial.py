# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', versatileimagefield.fields.VersatileImageField(height_field=b'height', upload_to=b'images', width_field=b'width', verbose_name=b'Image')),
                ('height', models.PositiveIntegerField(null=True, verbose_name=b'Image Height', blank=True)),
                ('width', models.PositiveIntegerField(null=True, verbose_name=b'Image Width', blank=True)),
                ('created_at', models.DateTimeField(help_text=b'Date when category created.', verbose_name=b'Created At', auto_now_add=True)),
                ('updated_at', models.DateTimeField(help_text=b'Date when category updated.', verbose_name=b'Updated At', auto_now=True)),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', verbose_name=b'Image PPOI', max_length=20, editable=False)),
            ],
        ),
    ]
