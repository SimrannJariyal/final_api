# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # Include the app's URLs for subjects and units
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
