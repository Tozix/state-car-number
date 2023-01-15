from api.models import CarNumer
from django.contrib import admin


@admin.register(CarNumer)
class CarNumer(admin.ModelAdmin):
    list_display = (
        'pk',
        'plate',
    )
    search_fields = ('plate',)
    empty_value_display = '-пусто-'
