from django.db import models
from venue.models import Category
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField, PPOIField

class Images(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )

        
    category = models.ForeignKey(Category, null=True, blank=True, related_name='images')
    created_at = models.DateTimeField(verbose_name=_('Created At'),
        auto_now_add=True, help_text=_("Date when category created."))
    updated_at = models.DateTimeField(verbose_name=_('Updated At'),
        auto_now=True, help_text=_("Date when category updated."))
    ppoi = PPOIField(
        'Image PPOI')
