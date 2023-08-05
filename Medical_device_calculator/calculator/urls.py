from django.urls import path

from .views import SearchResultsView, DevicesView, DevicesListView, DevicesDeleteView, DevicesUpdateView, DevicesCreateView
from . import views
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', DevicesView.as_view(), name='home'),
    path('devices/', DevicesListView.as_view(), name='devices_list'),
    path('<int:pk>/delete/', DevicesDeleteView.as_view(), name='devices_delete'),
    path('<int:pk>/edit/', DevicesUpdateView.as_view(), name='devices_edit'),
    path('new/', DevicesCreateView.as_view(), name='devices_new'),

]