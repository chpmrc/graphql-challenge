from django.contrib import admin

from celebrityshop.purchases.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('costume', 'user', 'date_created', 'get_costume_price', 'quantity')
    list_filter = ('costume', 'user')

    def get_costume_price(self, obj):
        return obj.costume.price
    get_costume_price.short_description = 'Price'

admin.site.register(Purchase, PurchaseAdmin)
