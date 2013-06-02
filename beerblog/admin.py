from django.contrib import admin
from beerblog.models import Beer, BeerType, Rating, Brewery
from beerblog.models import Wine, WineType, Winery

admin.site.register(Beer)
admin.site.register(BeerType)
admin.site.register(Rating)
admin.site.register(Brewery)

admin.site.register(Wine)
admin.site.register(WineType)
admin.site.register(Winery)