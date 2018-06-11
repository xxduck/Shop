from django.urls import path, include
from rest_framework import routers
from .views import goods, good, CommoditysView, CommodityView

router = routers.DefaultRouter()

# router.register('goods', CommodityView)

# print(router.registry)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path(r'', include(router.urls)),
    # path(r'auth', include('rest_framework.urls', namespace='rest_framework'))
    path("goods/", CommoditysView.as_view()),
    path("", include(router.urls)),
    path("goods/<int:id>", CommodityView.as_view())
]