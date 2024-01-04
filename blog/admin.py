from django.contrib import admin
from blog.models import Post, AboutMeSections


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "truncated_content", "status", "language", )
    fields = ("title", "content", "image", "status", "language", )
    search_fields = ("title", "content", )
    list_filter = ("language", "status", )

    def truncated_content(self, obj):
        max_length = 80
        return (obj.content[:max_length] + '...') if len(obj.content) > max_length else obj.content

    truncated_content.short_description = 'Content'


@admin.register(AboutMeSections)
class AboutMeSectionsAdmin(admin.ModelAdmin):
    list_display = ("meta", "title", "truncated_content", "status", "language", )
    fields = ("meta", "title", "content", "image", "status", "language", )
    search_fields = ("meta", "title", "content", )
    list_filter = ("language", "status", )

    def truncated_content(self, obj):
        max_length = 80
        return (obj.content[:max_length] + '...') if len(obj.content) > max_length else obj.content

    truncated_content.short_description = 'Content'
