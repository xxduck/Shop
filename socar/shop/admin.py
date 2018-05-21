from django.contrib import admin
from .models import Commodity

# Register your models here.


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    fieldsets = (
        (None, {
            'fields': (
                'id',
                'name'
            )
        })
    )


admin.register(Commodity, CommodityAdmin)