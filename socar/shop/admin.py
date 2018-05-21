from django.contrib import admin
from .models import Commodity

# Register your models here.


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'ptime')
    # fields = ('id', 'name', 'price', 'status')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'price',
                'status',
            )
        }),
    )


admin.site.register(Commodity, CommodityAdmin)