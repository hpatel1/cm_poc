# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Cateogry name', max_length=100, verbose_name=b'Category Name')),
                ('banner', sorl.thumbnail.fields.ImageField(upload_to=b'category/')),
                ('created_at', models.DateTimeField(help_text=b'Date when category created.', verbose_name=b'Created At', auto_now_add=True)),
                ('updated_at', models.DateTimeField(help_text=b'Date when category updated.', verbose_name=b'Updated At', auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Venue name', max_length=100, verbose_name=b'Venue name')),
                ('banner', sorl.thumbnail.fields.ImageField(upload_to=b'venue/')),
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
