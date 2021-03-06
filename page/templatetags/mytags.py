
from django import template
from pytils.translit import slugify

register = template.Library()


@register.filter
def prices(data):
    all_p = data.split('|')
    return_string = ''
    for i in all_p:
        return_string += f'<span itemprop="price" style="display:block">{i}</span>'
    return return_string

@register.filter
def prices_select(data):
    all_p = data.split('|')
    return_string = ''
    for i in all_p:
        print(i.split(' ')[0])
        return_string += f'<option value="{i.split(" ")[0]}">{i}</option>'
    return return_string

@register.filter
def make_slug(data):
    return slugify(data)