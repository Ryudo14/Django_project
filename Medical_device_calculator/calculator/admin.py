from django.contrib import admin
from .models import Search, Devices


class SearchAdmin(admin.ModelAdmin):
    list_display = ("name",)


class DevicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch', 'date', 'quantity_in_pack', 'quantity_thing', 'packing_price', 'price_for_one')


admin.site.register(Search, SearchAdmin,)
admin.site.register(Devices, DevicesAdmin,)
