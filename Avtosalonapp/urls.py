from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('carmodel/<int:model_id>/',carmodel,name='carmodel'),
    path('new_bot/<int:new_bot>/',new_bot,name='new_id'),
]
