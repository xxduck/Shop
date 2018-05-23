from django.shortcuts import render
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
        "form":UserForm})


def login(request):

    return render(request, "create.html", context={
        "form":User})