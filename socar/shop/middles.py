# 自定义中间件
from django.utils.deprecation import MiddlewareMixin

class ShopCar(MiddlewareMixin):

    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     return self.get_response(request)
    
    def process_request(self, request):
        # 读取cookies
        print("hehe")
        print(request.COOKIES)
        # 获取cookies，并给request添加新的属性
        request.car = {}
        shopcar = eval(request.COOKIES.get("goods"))
        if shopcar:
            
            request.car.update(shopcar)

    
    def process_response(self, request, response):
        # 获取request的car属性，并dump到cookies
        response.set_cookie("goods", request.car)
        return response
