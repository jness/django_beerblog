from django.contrib import admin
from beerblog.models import Beer, BeerType, Brewery
from beerblog.models import Wine, WineType, Winery


class BeerAdmin(admin.ModelAdmin):

    list_display = ['name', 'brewery', 'author']

    def get_form(self, request, obj=None, **kwargs):
            self.exclude = ("author", )
            form = super(BeerAdmin, self).get_form(request, obj, **kwargs)
            return form

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
admin.site.register(Beer, BeerAdmin)

admin.site.register(BeerType)
admin.site.register(Brewery)


class WineAdmin(admin.ModelAdmin):

    list_display = ['name', 'winery', 'author']

    def get_form(self, request, obj=None, **kwargs):
            self.exclude = ("author", )
            form = super(WineAdmin, self).get_form(request, obj, **kwargs)
            return form

    def save_model(self, request, obj, form, change):
        self.exclude = ['author']
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
admin.site.register(Wine, WineAdmin)

admin.site.register(WineType)
admin.site.register(Winery)