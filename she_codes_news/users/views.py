from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from news.models import NewsStory
from .forms import CustomUserCreationForm, CustomUser

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class MyAccountView(generic.ListView):
    template_name = 'users/myAccount.html'
    context_object_name = 'user_stories'

    def get_queryset(self):
        '''Return user stories.'''
        return NewsStory.objects.filter(author=self.request.user).values()

