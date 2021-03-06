from django.contrib import admin
from django.urls import path, include
from homepage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls', namespace='events')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
