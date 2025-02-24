from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('title','birth_date','created_at','updated_at')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['is_bool']

admin.site.register([Car,CarModel])

