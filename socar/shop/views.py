from django.shortcuts import render
from django.http import Http404
from .models import Commodity
from .forms import UserForm, User
# Create your views here.


def index(request):
    goods = Commodity.objects.all()
    return render(request, 'index.html', context={
        'goods': goods,
    })


def create(request):

    return render(request, "create.html", context={
        "form": UserForm})


def login(request):

    return render(request, "create.html", context={
        "form": User})


def info(request, id):
    try:
        good = Commodity.objects.filter(id=id)[0]
        
        return render(request, 'info.html', context={
            'good': good.__dict__,
        })
    
    except Exception as e:
        raise Http404(e)