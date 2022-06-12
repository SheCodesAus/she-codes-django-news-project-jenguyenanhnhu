from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    story_fields = forms.ModelChoiceField()

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['story_field'].initial = self.data
    class Meta: 
        model = NewsStory
        fields = ['title', 'author', 'date', 'content', 'image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': self.request.user}),
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
    }