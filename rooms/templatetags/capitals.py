from django import template

register = template.Library()


@register.filter
def apitals(value):
    return value.capitalize()
