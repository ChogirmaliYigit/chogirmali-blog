from django.urls import path
from blog.views import (MainView, BlogView, PostDetailView, ContactView, ThanksForContactingView, AboutView, SearchView,
                        bad_request, permission_denied, not_found, server_error)


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("blog", BlogView.as_view(), name="blog"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("contact", ContactView.as_view(), name="contact"),
    path("thanks-for-contacting", ThanksForContactingView.as_view(), name="thanks-for-contacting"),
    path("about", AboutView.as_view(), name="about"),
    path("search", SearchView.as_view(), name="search"),
    path("400", bad_request, name="400-bad-request"),
    path("403", permission_denied, name="403-permission-denied"),
    path("404", not_found, name="404-not-found"),
    path("500", server_error, name="500-server-error"),
]
