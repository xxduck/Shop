from django.shortcuts import render
from rest_framework import viewsets
from shop.models import Commodity
from .models import CSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.urls import path
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.response import Response

# Create your views here.
#######################
#  基于类
######################
class CommoditysView(generics.ListCreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CSerializers


class CommodityView(generics.ListCreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CSerializers
    
    def get(self, request, *args, **kwargs):
        try:
            kid = kwargs.get("id")
            # result = Commodity.objetcs.get_or_404(id=kid)
            result = self.queryset.get(id=kid)
            ser = CSerializers(result)
            return Response(ser.data, status.HTTP_200_OK)
        except:
            return Response([], status.HTTP_404_NOT_FOUND)

        





#######################
#  基于函数
######################
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


