from django.contrib import admin
from firstapp.models import Item



class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','cost','quantity','quantity_sold','selling_price','profit_earned','revenue')

admin.site.register(Item,ItemAdmin)
# Register your models here.
