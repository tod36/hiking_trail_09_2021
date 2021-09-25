from django import template
from django.db.models import Count, F

from mountain.models import Difficulty

register = template.Library()


@register.simple_tag(name='get_list_difficulties')
def get_difficulties():
    return Difficulty.objects.all()


@register.inclusion_tag('list_difficulties.html')
def show_difficulties():
    difficulties = Difficulty.objects.annotate(cnt=Count('trail')).filter(cnt__gt=0)
    return {"difficulties": difficulties}
