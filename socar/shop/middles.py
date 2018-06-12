# 自定义中间件
from django.utils.deprecation import MiddlewareMixin

class ShopCar(MiddlewareMixin):

    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     return self.get_response(request)
    
    def process_request(self, request):
        # 读取cookies
        # 获取cookies，并给request添加新的属性
        # print(dir(request.user))
        # 购物车需要和用户绑定
        request.user.car = {}
        shopcar = request.COOKIES.get("goods")
        if shopcar:
            
            request.user.car.update(eval(shopcar))

    
    def process_response(self, request, response):
        # 获取request的car属性，并dump到cookies
        if not hasattr(request.user, "car"):
            request.user.car = {}
        response.set_cookie("goods", request.user.car)
        return response
