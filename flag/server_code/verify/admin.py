from django.contrib import admin
from .models import Flag

class FlagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flag, FlagAdmin)

# Register your models here.
