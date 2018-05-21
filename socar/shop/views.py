from django.shortcuts import render
from .models import Commodity
# Create your views here.


def index(request):
    goods = Commodity.objects.all()
    return render(request, 'index.html', context={
        'goods': goods,
    })