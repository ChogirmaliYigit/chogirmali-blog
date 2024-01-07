import markdown

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def google_analytics_id():
    return settings.GOOGLE_ANALYTICS_ID


@register.simple_tag
def google_tag_manager_id():
    return settings.GOOGLE_TAG_MANAGER_ID


@register.simple_tag
def github_repo():
    return settings.GITHUB_REPO


@register.filter
def markdown(value):
    md = markdown.Markdown(extensions=["fenced_code"])
    return mark_safe(md.convert(str(value)))
