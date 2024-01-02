from django.contrib import admin
from blog.models import Post, AboutMeSections


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "status", )
    fields = ("title", "content", "image", "status", )
    search_fields = ("title", "content", )


admin.site.register(AboutMeSections)
