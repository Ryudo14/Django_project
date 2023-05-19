from django.urls import path

from .views import ListZoo, DetailZoo, ZooListView

urlpatterns = [
    path('<int:pk>/', DetailZoo.as_view()),
    path('', ListZoo.as_view()),
    path('home', ZooListView.as_view(), name='home'),
]