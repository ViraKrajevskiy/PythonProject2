from django.contrib import admin
from django.urls import path


from Uchebniycentrapp.views import cours

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usrin/',cours),
]
