from django.conf.urls import url, include
from rest_framework import routers
from .views import CommodityView

router = routers.DefaultRouter()
router.register(r'users', CommodityView)

# 使用URL路由来管理我们的API
# 另外添加登录相关的URL
urlpatterns = [
    url(r'', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]