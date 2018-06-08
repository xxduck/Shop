from django.shortcuts import render
from rest_framework import viewsets
from shop.models import Commodity
from .models import CSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.urls import path
from rest_framework import status

# Create your views here.

class CommodityView(viewsets.ViewSet):

    queryset = Commodity.objects.all()
    serializer_class = CSerializers


# @api_view(["GET"])
# @permission_classes((permissions.AllowAny,))
# def index(request):
#     if request.method == "GET":
#         result = 
#         ser = CSerializers(result, many=True)
#         return Response(ser.data, 200)


@api_view(["GET", "POST"])
@permission_classes((permissions.AllowAny,))
def goods(request):
    if request.method == "GET":
        result = Commodity.objects.all()
        ser = CSerializers(result, many=True)
        return Response(ser.data, 200)

    if request.method == "POST":
        ser = CSerializers(data=request.data)
        if ser.is_valid():
            print(ser.data)
            ser.create(ser.validated_data)
            # ser.save()

        return Response(ser.data, 200)


@api_view(["GET", "DELETE"])
@permission_classes((permissions.AllowAny,))
def good(request, id):
    try:
        g = Commodity.objects.get(id=id)

        ser = CSerializers(g)
        data = ser.data
        if request.method == "DELETE":
            
            g.delete()
        
        return Response(data, 200)
    except Exception as e:
        return Response([{'error':'notexzit'}], status.HTTP_204_NO_CONTENT)


