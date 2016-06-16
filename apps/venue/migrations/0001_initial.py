# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Cateogry name', max_length=100, verbose_name=b'Category Name')),
                ('banner', versatileimagefield.fields.VersatileImageField(height_field=b'height', upload_to=b'category', width_field=b'width', verbose_name=b'banner')),
                ('height', models.PositiveIntegerField(null=True, verbose_name=b'banner Height', blank=True)),
                ('width', models.PositiveIntegerField(null=True, verbose_name=b'Image Width', blank=True)),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', verbose_name=b'Image PPOI', max_length=20, editable=False)),
                ('created_at', models.DateTimeField(help_text=b'Date when category created.', verbose_name=b'Created At', auto_now_add=True)),
                ('updated_at', models.DateTimeField(help_text=b'Date when category updated.', verbose_name=b'Updated At', auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Venue name', max_length=100, verbose_name=b'Venue name')),
                ('banner', versatileimagefield.fields.VersatileImageField(height_field=b'height', upload_to=b'venue', width_field=b'width', verbose_name=b'banner')),
                ('height', models.PositiveIntegerField(null=True, verbose_name=b'banner Height', blank=True)),
                ('width', models.PositiveIntegerField(null=True, verbose_name=b'Image Width', blank=True)),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', verbose_name=b'Image PPOI', max_length=20, editable=False)),
                ('created_at', models.DateTimeField(help_text=b'Date when category created.', verbose_name=b'Created At', auto_now_add=True)),
                ('updated_at', models.DateTimeField(help_text=b'Date when category updated.', verbose_name=b'Updated At', auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='venue',
            field=models.ForeignKey(to='venue.Venue'),
        ),
    ]
