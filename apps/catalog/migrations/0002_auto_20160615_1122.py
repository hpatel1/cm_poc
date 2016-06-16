# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(related_name='images', blank=True, to='venue.Category', null=True),
        ),
    ]
