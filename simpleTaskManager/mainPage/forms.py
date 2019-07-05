from django.forms import ModelForm
from .models import Task

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
            'developer',
            'project',
        ]
    