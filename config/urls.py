from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

handler400 = "blog.views.bad_request"
handler403 = "blog.views.permission_denied"
handler404 = "blog.views.not_found"
handler500 = "blog.views.server_error"

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
)
