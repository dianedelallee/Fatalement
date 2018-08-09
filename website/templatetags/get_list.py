from django import template

register = template.Library()


@register.filter(name='get_list')
def get_list(list_of_tags):
    return list_of_tags.split(',')
