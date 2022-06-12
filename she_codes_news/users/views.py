from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from news.models import NewsStory
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class MyAccountView(generic.ListView):
    template_name = 'users/myAccount.html'
    context_object_name = 'user_stories'

    def get_queryset(self):
        '''Return user stories.'''
        return NewsStory.objects.all
    
    def get_author_name(self, **kwargs):
        user = self.get_object()
        context = {}
        context['user_stories'] = NewsStory.objects.filter(author=self.username).values()
        return context

    # def get_user_stories(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_stories'] = NewsStory.objects.filter(author=self.user).values()
    #     return context
