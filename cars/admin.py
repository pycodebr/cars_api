from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand__name', 'color', 'factory_year', 'model_year', 'created_at',)
    search_fields = ('model',)
    list_filter = ('brand',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
