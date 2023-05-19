from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Students


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Students
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Students
        fields = UserChangeForm.Meta.fields