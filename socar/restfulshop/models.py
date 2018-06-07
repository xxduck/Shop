from rest_framework import serializers
from shop.models import Commodity

class CSerializers(serializers.HyperlinkedIdentityField):
    class Meta:
        model = Commodity