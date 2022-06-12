from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'date', 'content', 'image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
    }