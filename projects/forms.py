from django.forms import ModelForm, widgets
from django import forms

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
    #     widgets = {
    #         'tags': forms.CheckboxSelectMultiple(),
    #     }

    # # def __init__(self, *args, **kwargs):
    # #     super(ProjectForm, self).__init__(*args, **kwargs)