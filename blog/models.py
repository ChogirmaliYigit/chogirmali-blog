import markdown

from django.db import models
from django.utils.text import slugify


PRODUCTION = "production"
STAGING = "staging"

STATUSES = (
    (PRODUCTION, "Production"),
    (STAGING, "Staging"),
)


class Post(models.Model):
    title = models.CharField(max_length=1500)
    slug = models.CharField(max_length=1500)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUSES, default=STAGING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def formatted_content(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        return md.convert(str(self.content))

    @property
    def formatted_title(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        return md.convert(str(self.title))

    def previous(self, is_production: bool = True):
        query = Post.objects.filter(
            created_at__lt=self.created_at,
        )
        if is_production:
            query.filter(status=PRODUCTION)
        return query.order_by('-created_at').first()

    def next(self, is_production: bool = True):
        query = Post.objects.filter(
            created_at__gt=self.created_at,
        )
        if is_production:
            query.filter(status=PRODUCTION)
        return query.order_by('created_at').first()

    class Meta:
        db_table = "blog_posts"


class AboutMeSections(models.Model):
    meta = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="about_me/", null=True, blank=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default=STAGING)

    class Meta:
        db_table = "about_me"
        verbose_name_plural = "About Me Sections"

    @property
    def formatted_content(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        return md.convert(str(self.content))

    @property
    def formatted_title(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        return md.convert(str(self.title))
