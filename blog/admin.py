from django.contrib import admin
from django import forms
from blog.models import Post, AboutMeSections
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ("title", "content", "image", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "status", )
    fields = ("title", "slug", "content", "image", "status", )
    search_fields = ("title", "content", )
    form = PostAdminForm


admin.site.register(AboutMeSections)
