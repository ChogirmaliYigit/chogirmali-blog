from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def google_analytics_id():
    return settings.GOOGLE_ANALYTICS_ID


@register.simple_tag
def github_repo():
    return settings.GITHUB_REPO
