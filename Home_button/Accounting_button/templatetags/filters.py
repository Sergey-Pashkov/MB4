from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='add_id')
def add_id(field, element_id):
    return field.as_widget(attrs={"id": element_id})

@register.filter(name='readonly')
def readonly(field, value):
    if value:
        return field.as_widget(attrs={"readonly": "readonly"})
    return field
