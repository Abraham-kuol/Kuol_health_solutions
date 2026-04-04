from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]

if settings.DEBUG or settings.MEDIA_URL and settings.MEDIA_ROOT:
    # Serve uploaded media in non-debug environments (e.g. Render) for small sites.
    # For production at scale, use a dedicated media storage (S3/Cloudinary).
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
