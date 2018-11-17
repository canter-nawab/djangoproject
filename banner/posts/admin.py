from django.contrib import admin

# Register your models here.
from .models import Banners,Entry

admin.site.register(Banners)
admin.site.register(Entry)

