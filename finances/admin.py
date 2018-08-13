from django.contrib import admin

from .models import Currency


class CurrencyModelAdmin(admin.ModelAdmin):
    list_display=['code', 'name', 'type']


admin.site.register(Currency, CurrencyModelAdmin)
