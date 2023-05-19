from rest_framework import serializers
from .models import Zoo


class ZooSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = ('id', 'title', 'name', 'view', 'live', 'age',)