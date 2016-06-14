from django.db import models
from sorl.thumbnail import ImageField
from django.utils.translation import gettext as _

class Venue(models.Model):
    name = models.CharField(verbose_name=_('Venue name'), max_length=100, help_text=_('Venue name'))
    banner = ImageField(upload_to='venue/')

    created_at = models.DateTimeField(verbose_name=_('Created At'),
        auto_now_add=True, help_text=_("Date when category created."))
    updated_at = models.DateTimeField(verbose_name=_('Updated At'),
        auto_now=True, help_text=_("Date when category updated."))


class Category(models.Model):
    name = models.CharField(verbose_name=_('Category Name'), max_length=100, help_text=_('Cateogry name'))
    venue = models.ForeignKey(Venue)
    banner = ImageField(upload_to='category/')
    
    created_at = models.DateTimeField(verbose_name=_('Created At'),
        auto_now_add=True, help_text=_("Date when category created."))
    updated_at = models.DateTimeField(verbose_name=_('Updated At'),
        auto_now=True, help_text=_("Date when category updated."))
