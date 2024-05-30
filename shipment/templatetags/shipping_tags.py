from django import template
import datetime

register = template.Library()

@register.filter
def shipment_status(delivery):
    expected_days = (delivery.delivery_date - delivery.order.shipment_date).days
    if expected_days < 0:
        return "early"
    elif expected_days == 0:
        return "fine"
    else:
        return "delay"