from django.urls import path
from .views import StudentsListView, StudentsCreateView, StudentsDeleteView, StudentsUpdateView, StudentsDetailView


urlpatterns = [
    path('<int:pk>/delete/', StudentsDeleteView.as_view(), name='students_delete'),
    path('<int:pk>/edit/', StudentsUpdateView.as_view(), name='students_edit'),
    path('<int:pk>/new/', StudentsCreateView.as_view(), name='students_new'),
    path('<int:pk>/list/', StudentsCreateView.as_view(), name='students_list'),
    path('', StudentsListView.as_view(), name='home'),
    path('<int:pk>/detail/', StudentsDetailView.as_view(), name='students_detail'),
]
