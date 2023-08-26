from django import forms
from . import models


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']

    
