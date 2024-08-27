import logging

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

logger = logging.getLogger(__name__)

def trigger_error(request):
    my_dict = {"key": "value"}
    return my_dict["non_existent_key"]  # Esto generará un KeyError

def login_error(request):
    logging.info("Loggin de tipo info")
    return None

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicles.urls')),
    path('media/', include('media.urls')),
    path('users/', include('users.urls')), 
    path('comments/', include('comments.urls')),
    path('sentry-debug/', trigger_error),  # Ruta para verificar Sentry
    path('', HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
