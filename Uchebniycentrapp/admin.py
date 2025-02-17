from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('title','start_time','end_time','created_at','updated_at')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['is_bool']

admin.site.register([Course,Student])
