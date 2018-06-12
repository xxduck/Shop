from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Commodity, Nuser
from .forms import BuyForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import MyForm
from django.views.generic import ListView
# Create your views here.


class Index(ListView):
    template_name = "index.html"
    model = Commodity
    paginate_by = 100
    # def get(self, request, *args, **kwargs):
    #     goods = Commodity.objects.all()
    #     return render(request, 'index.html', context={
    #     'goods': goods,
    #     'hello': "hello",
    # })


def index(request):
    goods = Commodity.objects.all()
    return render(request, 'index.html', context={
        'goods': goods,
        'hello': "hello",
    })


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Nuser


def create(request):

    if request.method == "POST":
        user = CreationForm(request.POST)
        if user.is_valid():
            # username = request.POST.get("username")
            # passwd1 = request.POST.get("passwd1")
            # passwd2 = request.POST.get("passwd2")
            # nick = request.POST.get("nick")
            print(user.cleaned_data.items())
            print(user.cleaned_data.keys())
            user.save()
            # if passwd1 == passwd2:
            #     MyUser.objects.create(username=username, passwd1=make_password(passwd1), passwd2=make_password(passwd2), nick=nick)
            return HttpResponse(content="注册成功")

    return render(request, "create.html", context={
        "form": CreationForm()})


def user_logout(request):
    print(request.user)
    if request.user.is_authenticated:
        print(request.sessions)
        logout(request)
        return HttpResponse("退出成功")
    else:
        return HttpResponse("您还没有登陆过")


def info(request, id):
    good = Commodity.objects.filter(id=id)[0]
    
    if request.method == "GET":
        try:
            return render(request, 'info.html', context={
                'good': good.__dict__,
                'form': BuyForm(),
            })
        
        except Exception as e:
            raise Http404(e)
    elif request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            response = HttpResponse(str(good.price * form.cleaned_data.get("num")))
            request.car.update({
                good.id: form.cleaned_data.get("num")
            })
            return response
        else:

            return render(request, 'info.html', context={
                    'good': good.__dict__,
                    'form': form,
                })


def perinfo(request, nick):
    return render(request, "perinfo.html")


def a(request):
    if request.method == "GET":
        
        return render(request, "tmp.html", context={
            "form": MyForm()})

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("success")
        else:
            return render(request, "tmp.html", context={
            "form": form})



# 购物车页面
def carpage(request):
    return render(request, template_name='carinfo.html', context={
        'goods': request.car
    })

@login_required
def buy(request):
    # 购买页面
    price = 0
    print(request.car)
    for k, v in request.car.items():
        good = Commodity.objects.get(id=k)
        price += good.price * v

    return render(request, template_name='buy.html', context={
        'price': price
    })

    
