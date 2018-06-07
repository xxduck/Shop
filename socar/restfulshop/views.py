from django.shortcuts import render
from rest_framework import viewsets
from shop.models import Commodity
from .models import CSerializers

# Create your views here.

class CommodityView(viewsets.ViewSet):

    queryset = Commodity.objects.all()
    serializer_class = CSerializers