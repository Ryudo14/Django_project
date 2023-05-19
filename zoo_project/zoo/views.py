from .serializers import ZooSerializers
from .models import Zoo
from rest_framework import generics
from django.views.generic import ListView


class ListZoo(generics.ListAPIView):
    queryset = Zoo.objects.all()
    serializer_class = ZooSerializers


class DetailZoo(generics.RetrieveAPIView):
    queryset = Zoo.objects.all()
    serializer_class = ZooSerializers


class ZooListView(ListView):
    model = Zoo
    template_name = 'home.html'

