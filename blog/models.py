from django.conf import settings
from django.db import models

PRODUCTION = "production"
STAGING = "staging"

STATUSES = (
    (PRODUCTION, "Production"),
    (STAGING, "Staging"),
)


class Post(models.Model):
    content = models.TextField()
    status = models.CharField(max_length=100, choices=STATUSES, default=STAGING)
    language = models.CharField(
        max_length=10, choices=settings.LANGUAGES, default=settings.EN
    )
    alternative = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def previous(self, is_production: bool = True):
        query = Post.objects.filter(
            created_at__lt=self.created_at,
        )
        if is_production:
            query.filter(status=PRODUCTION)
        previous = query.order_by("-created_at").first()
        if previous != self.alternative:
            return previous
        return

    def next(self, is_production: bool = True):
        query = Post.objects.filter(
            created_at__gt=self.created_at,
        )
        if is_production:
            query.filter(status=PRODUCTION)
        next_post = query.order_by("created_at").first()
        if next_post != self.alternative:
            return next_post
        return

    class Meta:
        db_table = "blog_posts"


class AboutMeSections(models.Model):
    meta = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="about_me/", null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default=STAGING)
    language = models.CharField(
        max_length=10, choices=settings.LANGUAGES, default=settings.EN
    )
    alternative = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "about_me"
        verbose_name_plural = "About Me Sections"


class Comment(models.Model):
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    reply_to = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replied_comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_comments"
