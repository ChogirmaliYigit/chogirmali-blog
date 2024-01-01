from django.urls import path
from blog.views import MainView, BlogView, PostDetailView, ContactView, ThanksForContactingView, AboutView, SearchView


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("blog", BlogView.as_view(), name="blog"),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("contact", ContactView.as_view(), name="contact"),
    path("thanks-for-contacting", ThanksForContactingView.as_view(), name="thanks-for-contacting"),
    path("about", AboutView.as_view(), name="about"),
    path("search", SearchView.as_view(), name="search"),
]
