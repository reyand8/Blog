from django import template
from django.db.models import Count
from ..utils import menu
from ..models import Category,TagReview, TypeReview

register = template.Library()


@register.simple_tag
def get_menu():
    return menu

@register.inclusion_tag('../../static/templates/blog/list_types.html')
def show_types():
    types_review =  TypeReview.objects.annotate(total=Count("name")).filter(total__gt=0)
    return {'types_review': types_review}


@register.inclusion_tag('../../static/templates/blog/list_categories.html')
def show_categories(cat_selected=0):
    cats =  Category.objects.annotate(total=Count("name")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('../../static/templates/blog/list_tags.html')
def show_all_tags():
    return {'tags': TagReview.objects.annotate(total=Count("tag")).filter(total__gt=0)}