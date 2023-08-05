from django.urls import path
from django.urls import reverse_lazy

from .views import SignUpView, ChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change_form/', ChangeView.as_view(), name='password_change'),
]