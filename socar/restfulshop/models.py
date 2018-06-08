from rest_framework import serializers
from shop.models import Commodity


class CSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = ('id', 'name', 'price', 'discount', 'status')