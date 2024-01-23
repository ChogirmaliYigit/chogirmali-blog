from django.contrib import admin
from unfold.admin import ModelAdmin

from blog.models import AboutMeSections, Comment, Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
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

    def truncated_content(self, obj):
        max_length = 80
        return (
            (obj.content[:max_length] + "...")
            if len(obj.content) > max_length
            else obj.content
        )

    truncated_content.short_description = "Content"


@admin.register(AboutMeSections)
class AboutMeSectionsAdmin(ModelAdmin):
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

    list_filter_submit = True

    def truncated_content(self, obj):
        max_length = 80
        return (
            (obj.content[:max_length] + "...")
            if len(obj.content) > max_length
            else obj.content
        )

    truncated_content.short_description = "Content"


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
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

    list_filter_submit = True

    def truncated_content(self, obj):
        max_length = 80
        return (
            (obj.content[:max_length] + "...")
            if len(obj.content) > max_length
            else obj.content
        )

    truncated_content.short_description = "Content"
