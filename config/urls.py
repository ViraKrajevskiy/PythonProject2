
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('cars/',include('Avtomarket.urls')),
    path('avtom/',include('Avtomarket.urls')),
    path('admin/', admin.site.urls),
]
