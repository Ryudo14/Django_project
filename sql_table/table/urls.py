from django.urls import path

from .views import ListTable

urlpatterns = [
    path('', ListTable.as_view(), name='home'),
]