from django.contrib import admin
from .models import Commodity, MyUser

# Register your models here.


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'ptime')
    # fields = ('id', 'name', 'price', 'status')
    search_fields = ('name', 'ptime', 'status')
    list_filter = (
        'ptime',
        'status',
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'price',
                'discount',
                'status',
                'img',
                'context'
            )
        }),
    )


admin.site.register(Commodity, CommodityAdmin)
admin.site.register(MyUser)
