from django import template

register = template.Library()

@register.simple_tag
def set_active(menu_item, path):
    if menu_item in path:
        return 'active'
    else:
        return ''
    
