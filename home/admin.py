from django.contrib import admin
from .models import *


# Register your models here.
class AdminSite(admin.ModelAdmin):
    list_display = ('name', 'phone', 'content', 'timestamp', 'reply')


admin.sites.AdminSite.site_header = "پنل ادمین "
admin.site.register(Articles)
admin.site.register(Books)
admin.site.register(Research)
admin.site.register(Comment,AdminSite)
admin.site.register(Commenta,AdminSite)


