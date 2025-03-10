from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'complete',
        ]

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2'
        ]