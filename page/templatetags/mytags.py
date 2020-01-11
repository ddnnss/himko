
from django import template

register = template.Library()


@register.filter
def prices(data):
    all_p = data.split('|')
    return_string = ''
    for i in all_p:
        return_string += f'<span style="display:block">{i}</span>'
    return return_string


