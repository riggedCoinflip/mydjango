from django import template

register = template.Library()

@register.filter
def to_percent(obj, significant_digits):
    return f'{(obj * 100):.{significant_digits}f}'


