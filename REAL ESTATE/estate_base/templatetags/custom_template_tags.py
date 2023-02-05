from django import template
from ..models import *


register = template.Library()


@register.inclusion_tag('estate_base/recent_property.html')
def recent_property(count=7):
    latest_property = HouseDetails.objects.order_by('-date_created')[:count]
    return {'latest_property': latest_property}


@register.inclusion_tag('estate_base/property_single_recents.html')
def property_recents(count=3):
    recents = HouseDetails.objects.order_by('-date_created')[:count]
    return {'recents': recents}


@register.simple_tag
def my_url(value, field_name, url_encode=None):
    url = '?{}-{}'.format(field_name, value)

    if url_encode:
        querystring = url_encode.split('&')
        filtered_querystring = filter(lambda p: p.split('-')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url
