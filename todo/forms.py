from django import forms
from django.forms import DateTimeInput, CheckboxSelectMultiple

from todo.models import Todo, Tag


class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "tag"]
        widgets = {
            "created_date": DateTimeInput(attrs={"type": "datetime-local"}),
            "completed": CheckboxSelectMultiple,
        }


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
