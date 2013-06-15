from django.contrib import admin
from beerblog.models import Beer, BeerType, Brewery


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
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "brewery":
            kwargs["queryset"] = Brewery.objects.order_by('name')
        if db_field.name == "beer_type":
            kwargs["queryset"] = BeerType.objects.order_by('name')
        return super(BeerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Beer, BeerAdmin)

admin.site.register(BeerType)
admin.site.register(Brewery)