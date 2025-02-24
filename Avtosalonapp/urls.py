from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index,name='home' ),
    path('carmodel/<int:model_id>/',carmodel,name='carmodel'),
    path('new_bot/<int:new_id>/',new_bot,name='new_bot'),
]
