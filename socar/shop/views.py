from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Commodity, Nuser
# from .forms import UserForm, UserRegist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    goods = Commodity.objects.all()
    return render(request, 'index.html', context={
        'goods': goods,
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
        "form": CreationForm})


def user_logout(request):
    print(request.user)
    if request.user.is_authenticated:
        print(request.sessions)
        logout(request)
        return HttpResponse("退出成功")
    else:
        return HttpResponse("您还没有登陆过")


def info(request, id):
    try:
        good = Commodity.objects.filter(id=id)[0]
        
        return render(request, 'info.html', context={
            'good': good.__dict__,
        })
    
    except Exception as e:
        raise Http404(e)


def perinfo(request, nick):
    return render(request, "perinfo.html")