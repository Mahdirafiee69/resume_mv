from django.contrib import admin
from .models import *

# Register your models here.
admin.sites.AdminSite.site_header = "پنل ادمین "
admin.site.register(Articles)
admin.site.register(Books)
admin.site.register(Research)



class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('header',)
    }


