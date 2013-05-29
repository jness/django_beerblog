from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from beerblog.models import Beer, BeerType, Brewery


def _get_pages(request, object, count=5):
    """Builds a Paginator"""
    pages = Paginator(object, count)
    page = request.GET.get('page')
    try:
        beers = pages.page(page)
    except PageNotAnInteger:
        beers = pages.page(1)
    except EmptyPage:
        beers = pages.page(pages.num_pages)
    return beers


def home(request):
    """Home Page"""
    content = dict()
    content['view'] = 'Home'
    content['settings'] = settings
    return render(request, 'beerblog/home.html', content)


def beers(request):
    """beers Page"""
    content = dict()
    content['view'] = 'Beers'
    content['settings'] = settings

    beers = Beer.objects.all().order_by('-created')

    brewery = request.GET.get('brewery')
    if brewery:
        beers = beers.filter(brewery__id=brewery)

    beer_type = request.GET.get('beer_type')
    if beer_type:
        beers = beers.filter(beer_type__id=beer_type)

    beer = request.GET.get('beer')
    if beer:
        beers = beers.filter(id=beer)

    search = request.GET.get('search')
    if search:
        beers = beers.filter(name__icontains=search)

    content['beers'] = _get_pages(request, beers)
    return render(request, 'beerblog/beers.html', content)

def wines(request):
    """wines Page"""
    content = dict()
    content['view'] = 'Wines'
    content['settings'] = settings
    return render(request, 'beerblog/wines.html', content)