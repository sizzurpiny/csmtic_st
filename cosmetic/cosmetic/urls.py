from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cosmetic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcomenstat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
