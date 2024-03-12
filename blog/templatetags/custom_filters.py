import markdown as md
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
def google_docs_url(lang, theme):
    return settings.GOOGLE_DOCS_URLS[lang][theme]


@register.simple_tag
def github_repo():
    return settings.GITHUB_REPO


@register.filter
def markdown(value):
    return mark_safe(md.Markdown(extensions=["fenced_code"]).convert(str(value)))


@register.simple_tag
def contact_email():
    return settings.CONTACT_EMAIL
