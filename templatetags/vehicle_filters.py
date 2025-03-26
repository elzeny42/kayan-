from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def format_quantity(value):
    """Format quantity with up to 3 decimal places, removing trailing zeros"""
    if value is None:
        return '0'
    formatted = floatformat(value, 3)
    # Remove trailing zeros after decimal point
    if '.' in formatted:
        formatted = formatted.rstrip('0').rstrip('.')
    return formatted

@register.filter
def format_freight(value):
    """Format freight amount with 2 decimal places"""
    if value is None:
        return '0.00'
    return floatformat(value, 2)

@register.filter
def movement_type_class(value):
    """Return Bootstrap class based on movement type"""
    return 'text-primary' if value == 'internal' else 'text-success'

@register.filter
def operation_type_badge(value):
    """Return Bootstrap badge class based on operation type"""
    if value == 'sale':
        return 'badge bg-success'
    elif value == 'purchase':
        return 'badge bg-info'
    return 'badge bg-secondary'