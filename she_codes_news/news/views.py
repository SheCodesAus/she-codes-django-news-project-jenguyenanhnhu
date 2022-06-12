from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
# from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/CreateStory.html'
    success_url = reverse_lazy('news:story')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:story')

    def get_queryset(self):
        '''Return submitted form.'''
        return NewsStory.objects.all()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def image_upload_view(request):
    #     """Process images uploaded by users"""
    #     if request.method == 'POST':
    #         form = StoryForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #         # Get the current instance object to display in the template
    #             img_obj = form.instance
    #             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    #     else:
    #         form = StoryForm()
    #     return render(request, 'index.html', {'form': form})