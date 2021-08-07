import re
# import logging

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()
# logger = logging.getLogger(__name__)

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    path = context['request'].path
    # logger.error(path == '/')
    # logger.error(len(pattern_or_urlname))

    if len(pattern_or_urlname) == 0:
        # logger.error('active')
        return 'active' if path == '/' else ''
    else:
        try:
            pattern = '^' + reverse(pattern_or_urlname)
        except NoReverseMatch:
            pattern = pattern_or_urlname

        if re.search(pattern, path):
            return 'active'
        return ''