from django.contrib import admin
from unfold.admin import ModelAdmin

from blog.actions import download_file
from blog.models import AboutMeSections, Comment, Post


class BaseModelAdmin(ModelAdmin):
    list_filter_submit = True

    def truncated_content(self, obj):
        max_length = 80
        return (
            (obj.content[:max_length] + "...")
            if len(obj.content) > max_length
            else obj.content
        )

    truncated_content.short_description = "Content"


@admin.register(Post)
class PostAdmin(BaseModelAdmin):
    actions = [download_file]

    list_display = (
        "truncated_content",
        "status",
        "language",
    )
    fields = (
        "content",
        "status",
        "language",
        "alternative",
    )
    search_fields = ("content",)
    list_filter = (
        "language",
        "status",
    )


@admin.register(AboutMeSections)
class AboutMeSectionsAdmin(BaseModelAdmin):
    actions = [download_file]

    list_display = (
        "meta",
        "truncated_content",
        "status",
        "language",
    )
    fields = (
        "meta",
        "content",
        "image",
        "status",
        "language",
        "alternative",
    )
    search_fields = (
        "meta",
        "content",
    )
    list_filter = (
        "language",
        "status",
    )


@admin.register(Comment)
class CommentAdmin(BaseModelAdmin):
    actions = [download_file]

    list_display = (
        "email",
        "truncated_content",
        "post",
        "reply_to",
    )
    fields = (
        "email",
        "content",
        "post",
        "reply_to",
    )
    search_fields = (
        "email",
        "content",
    )
