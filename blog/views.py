from typing import Any
from django.views.generic import TemplateView
from django.db.models import Q
from django.shortcuts import redirect, render
from blog.models import Post, AboutMeSections, PRODUCTION
from blog.utils import send_contact_info_to_telegram_chat


class MainView(TemplateView):
    template_name = "blog/index.html"


class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = []
        if self.request.user.is_authenticated and self.request.user.is_staff:
            queryset = Post.objects.all()
        else:
            queryset = Post.objects.filter(status=PRODUCTION)
        context["posts"] = queryset
        return context


class PostDetailView(TemplateView):
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_staff:
            post = Post.objects.filter(pk=context.get("pk")).first()
            context["previous_post"] = post.previous(is_production=False)
            context["next_post"] = post.next(is_production=False)
        else:
            post = Post.objects.filter(pk=context.get("pk"), status=PRODUCTION).first()
            context["previous_post"] = post.previous
            context["next_post"] = post.next
        context["post"] = post
        return context


class ContactView(TemplateView):
    template_name = "sections/contact.html"

    def post(self, request):
        send_contact_info_to_telegram_chat(request.POST)
        return redirect("thanks-for-contacting")


class ThanksForContactingView(TemplateView):
    template_name = "sections/thanks-for-contacting.html"


class AboutView(TemplateView):
    template_name = "sections/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = []
        if self.request.user.is_authenticated and self.request.user.is_staff:
            queryset = AboutMeSections.objects.all()
        else:
            queryset = AboutMeSections.objects.filter(status=PRODUCTION)
        context["sections"] = queryset
        return context


class SearchView(TemplateView):
    template_name = "blog/search.html"

    def get(self, request):
        query = request.GET.get("query")
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        if not request.user.is_authenticated and not request.user.is_staff:
            results = results.filter(status=PRODUCTION)
        return render(request, self.template_name, {"results": results, "query": query})
