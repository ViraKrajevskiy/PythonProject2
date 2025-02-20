from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static



from Uchebniycentrapp.views import cours, category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usrin/',cours),
    path('title_ap/<int:id>/',category),

]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
