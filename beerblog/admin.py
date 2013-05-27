from django.contrib import admin
from beerblog.models import Beer, BeerImage, BeerType, Rating, Brewery

admin.site.register(Beer)
admin.site.register(BeerImage)
admin.site.register(BeerType)
admin.site.register(Rating)
admin.site.register(Brewery)