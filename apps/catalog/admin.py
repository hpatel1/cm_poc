from django.contrib import admin

from venue.models import Venue, Category
from catalog.models import Images

# Register your models here.
admin.site.register(Venue)
admin.site.register(Category)
admin.site.register(Images)
