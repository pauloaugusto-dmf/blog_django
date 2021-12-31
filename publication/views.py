from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.list import ListView

from .models import Topic

class PublicationHomeView(View):
    template_name = 'publication/home.html'
    topic = Topic

    
    def get(self, request):
        context = {
            'topics': self.topic.objects.all()
        }
        
        return render(request, self.template_name, context)

class TopicListView(ListView):
    model = Topic
    paginate_by = 15

class TopicCreateView(CreateView):
    model = Topic
    fields = ['name']
    success_url = '/topic/list/'

class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = '/topic/list/'

class TopicDeleteView(DeleteView):
    model = Topic
    template_name_suffix = '_confirm_delete'
    success_url = '/topic/list/'
