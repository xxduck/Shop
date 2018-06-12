from django.urls import path, include
from .views import index, create, info, a, Index, carpage, buy
from django.contrib.auth.views import logout, LoginView

urlpatterns = [
    path('', index, name='index'),
    path("create/", create, name="create"),
    path("accounts/login/", LoginView.as_view(template_name='login.html'), name="login"),
    # 上面这个函数需要设置next  在html中设置
    path("accounts/", include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("<int:id>/", info, name="info"),
    path("logout/", logout, name="logout"),
    path("a/", a),
    path("carinfo/", carpage, name="carinfo"),
    path("buy", buy, name="buy"),
    
]