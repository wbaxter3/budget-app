from django import template

register = template.Library()

@register.filter(name='gt')
def gt(value, arg):

    return value > arg
