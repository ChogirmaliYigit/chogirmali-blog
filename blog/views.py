from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import get_language
from django.views.generic import TemplateView

from blog.models import PRODUCTION, AboutMeSections, Comment, Post
from blog.utils import send_contact_info_to_telegram_chat


class MainView(TemplateView):
    template_name = "blog/index.html"


class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_staff:
            queryset = Post.objects.filter(language=get_language())
        else:
            queryset = Post.objects.filter(status=PRODUCTION, language=get_language())
        context["posts"] = queryset
        return context


class PostDetailView(TemplateView):
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_staff:
            post = Post.objects.filter(
                pk=context.get("pk"), language=get_language()
            ).first()
            if not post:
                post = get_object_or_404(
                    Post, alternative__pk=context.get("pk"), language=get_language()
                )
            context["previous_post"] = post.previous(is_production=False)
            context["next_post"] = post.next(is_production=False)
        else:
            post = Post.objects.filter(
                pk=context.get("pk"), status=PRODUCTION, language=get_language()
            ).first()
            if not post:
                post = get_object_or_404(
                    Post, alternative__pk=context.get("pk"), language=get_language()
                )
            context["previous_post"] = post.previous()
            context["next_post"] = post.next()
        context["post"] = post
        return context

    def post(self, request, pk, *args, **kwargs):
        reply_to = request.POST.get("reply_to", None)
        comment = Comment.objects.create(
            email=request.POST.get("email"),
            content=request.POST.get("message"),
            post_id=pk,
            reply_to_id=reply_to,
        )
        redirect_url = redirect("post-detail", pk=pk).url
        redirect_url += (
            f"#comment-reply-{comment.pk}" if reply_to else f"#comment-{comment.pk}"
        )
        return redirect(redirect_url)


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
        if self.request.user.is_authenticated and self.request.user.is_staff:
            queryset = AboutMeSections.objects.filter(language=get_language())
        else:
            queryset = AboutMeSections.objects.filter(
                status=PRODUCTION, language=get_language()
            )
        context["sections"] = queryset
        return context


class SearchView(TemplateView):
    template_name = "blog/search.html"

    def get(self, request):
        query = request.GET.get("query")
        results = []
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            results.filter(language=get_language())
            if not request.user.is_authenticated and not request.user.is_staff:
                results = results.filter(status=PRODUCTION)
        return render(request, self.template_name, {"results": results, "query": query})


class ResumeView(TemplateView):
    template_name = "sections/resume.html"


def bad_request(request, exception=None):
    return render(request, "errors/400.html")


def permission_denied(request, exception=None):
    return render(request, "errors/403.html")


def not_found(request, exception=None):
    return render(request, "errors/404.html")


def server_error(request, exception=None):
    return render(request, "errors/500.html")
