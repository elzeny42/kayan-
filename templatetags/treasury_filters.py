from django import template
from django.db.models import Sum
from django.forms import BoundField

register = template.Library()

@register.filter
def filter_by(queryset, filter_string):
    """
    Filter a queryset based on a field and value.
    Usage: {{ queryset|filter_by:"field=value" }}
    """
    try:
        field, value = filter_string.split('=')
        kwargs = {field: value}
        return queryset.filter(**kwargs)
    except (ValueError, AttributeError):
        return queryset

@register.filter(name='treasury_sum')
def sum(queryset, field_name):
    """
    Sum the values of a specific field in a queryset
    Usage: {{ queryset|sum:"field_name" }}
    """
    return queryset.aggregate(total=Sum(field_name)).get('total') or 0

@register.filter
def add_class(field, css_class):
    if isinstance(field, BoundField):
        return field.as_widget(attrs={'class': css_class})
    return field

@register.filter
def attr(field, attributes):
    if isinstance(field, BoundField):
        attrs = {}
        for attr_pair in attributes.split(','):
            key, value = attr_pair.split(':')
            attrs[key.strip()] = value.strip().strip('\"').strip("'")
        return field.as_widget(attrs=attrs)
    return field