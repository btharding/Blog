from django import template

register = template.Library()

@register.filter(name="this_test_filter")
def this_test_filter(value):
    return value[0]

@register.filter(name = "make_headers")
def make_headers(value):
    temp = value.split('*')
    return temp[0]
