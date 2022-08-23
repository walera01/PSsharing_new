from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('store/list_game.html')
def get_categories():
    model = GamesModel.objects.all()
    return {"model":model}