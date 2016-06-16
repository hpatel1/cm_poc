from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField, PPOIField

class Venue(models.Model):
    name = models.CharField(verbose_name=_('Venue name'), max_length=100, help_text=_('Venue name'))
    banner = VersatileImageField(
        'banner',
        upload_to='venue',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'banner Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI')

    created_at = models.DateTimeField(verbose_name=_('Created At'),
        auto_now_add=True, help_text=_("Date when category created."))
    updated_at = models.DateTimeField(verbose_name=_('Updated At'),
        auto_now=True, help_text=_("Date when category updated."))


class Category(models.Model):
    name = models.CharField(verbose_name=_('Category Name'), max_length=100, help_text=_('Cateogry name'))
    venue = models.ForeignKey(Venue)
    banner = VersatileImageField(
        'banner',
        upload_to='category',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'banner Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI')
    
    created_at = models.DateTimeField(verbose_name=_('Created At'),
        auto_now_add=True, help_text=_("Date when category created."))
    updated_at = models.DateTimeField(verbose_name=_('Updated At'),
        auto_now=True, help_text=_("Date when category updated."))
