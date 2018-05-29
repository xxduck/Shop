from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Commodity, MyUser
from .forms import UserForm, UserRegist
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
    goods = Commodity.objects.all()
    return render(request, 'index.html', context={
        'goods': goods,
    })


def create(request):
    form = UserRegist

    if request.method == "POST":
        user = UserRegist(request.POST)
        if user.is_valid():
            username = request.POST.get("username")
            passwd1 = request.POST.get("passwd1")
            passwd2 = request.POST.get("passwd2")
            nick = request.POST.get("nick")

            if passwd1 == passwd2:
                MyUser.objects.create(username=username, passwd1=make_password(passwd1), passwd2=make_password(passwd2), nick=nick)
                return HttpResponse(content="注册成功")

    return render(request, "create.html", context={
        "form": form})


def login(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            username = request.POST.get("username")
            passwd = request.POST.get("passwd1")
            tmp = MyUser.objects.filter(username=username)[1]
            if check_password(passwd, tmp.passwd1):
                return HttpResponse("登录成功")

    return render(request, "create.html", context={
        "form": UserForm})


def info(request, id):
    try:
        good = Commodity.objects.filter(id=id)[0]
        
        return render(request, 'info.html', context={
            'good': good.__dict__,
        })
    
    except Exception as e:
        raise Http404(e)