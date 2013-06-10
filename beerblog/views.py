from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from beerblog.models import Beer, Wine, Brewery, Winery, BeerType, WineType


def _get_pages(request, object, count=15):
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
    content['latest_beers'] = Beer.objects.all().order_by('-created')[:4]
    content['latest_wines'] = Wine.objects.all().order_by('-created')[:4]
    return render(request, 'beerblog/home.html', content)


def search(request):
    """Search Page"""
    content = dict()
    content['view'] = 'Search'
    content['settings'] = settings
    search_term = request.GET.get('s')
    if search_term:
        content['view'] = search_term
        content['search_term'] = search_term
        content['beers'] = Beer.objects.filter(
            name__icontains=search_term)
        content['wines'] = Wine.objects.filter(
            name__icontains=search_term)
        content['breweries'] = Brewery.objects.filter(
            name__icontains=search_term)
        content['wineries'] = Winery.objects.filter(
            name__icontains=search_term)
        content['beer_type'] = BeerType.objects.filter(
            name__icontains=search_term)
        content['wine_type'] = WineType.objects.filter(
            name__icontains=search_term)
    return render(request, 'beerblog/search.html', content)


def beers(request):
    """beers Page"""
    content = dict()
    content['view'] = 'Beers'
    content['settings'] = settings

    beers = Beer.objects.all().order_by('name')

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


def beer(request, pk):
    """beer Page"""
    content = dict()
    content['settings'] = settings

    beer = Beer.objects.get(id=pk)
    if not beer:
        raise Http404

    content['view'] = beer.name
    content['beer'] = beer
    return render(request, 'beerblog/beer.html', content)


def wines(request):
    """wines Page"""
    content = dict()
    content['view'] = 'Wines'
    content['settings'] = settings

    wines = Wine.objects.all().order_by('name')

    winery = request.GET.get('winery')
    if winery:
        wines = wines.filter(winery__id=winery)

    wine_type = request.GET.get('wine_type')
    if wine_type:
        wines = wines.filter(wine_type__id=wine_type)

    wine = request.GET.get('wine')
    if wine:
        wines = wines.filter(id=wine)

    region = request.GET.get('region')
    if wine:
        wines = wines.filter(region__id=region)

    search = request.GET.get('search')
    if search:
        wines = wines.filter(name__icontains=search)

    content['wines'] = _get_pages(request, wines)
    return render(request, 'beerblog/wines.html', content)


def wine(request, pk):
    """wine Page"""
    content = dict()
    content['settings'] = settings

    wine = Wine.objects.get(id=pk)
    if not wine:
        raise Http404

    content['view'] = wine.name
    content['wine'] = wine
    return render(request, 'beerblog/wine.html', content)