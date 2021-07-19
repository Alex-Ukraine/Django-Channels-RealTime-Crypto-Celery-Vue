from django.contrib import admin
from .models import Coin, Pair


class CoinAdmin(admin.ModelAdmin):
    list_display = ('base', 'target', 'price',)


class PairAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Coin, CoinAdmin)
admin.site.register(Pair, PairAdmin)
