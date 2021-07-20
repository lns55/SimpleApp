from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your task'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your task'
            }),
        }