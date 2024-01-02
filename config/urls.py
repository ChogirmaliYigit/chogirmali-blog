from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler400 = "blog.views.bad_request"
handler403 = "blog.views.permission_denied"
handler404 = "blog.views.not_found"
handler500 = "blog.views.server_error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
