
from django import template

register = template.Library()

@register.filter
def lowers(value):
    return value.lowers()