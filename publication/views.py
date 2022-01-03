from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.views.generic.list import ListView


from .models import Topic, Post
from .form import PostCreateForm

class PublicationHomeView(View):
    template_name = 'publication/home.html'
    paginate_by = 5
    topic = Topic
    post = Post

    
    def get(self, request):
        context = {
            'topics': self.topic.objects.all(),
            'posts': self.post.objects.all(),
        }
        
        return render(request, self.template_name, context)

# Topic Views

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

# Post Views

class PostListView(ListView):
    model = Post
    paginate_by = 15

class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostCreateView(CreateView):
    model = Post
    topic = Topic
    form = PostCreateForm
    fields = ['title', 'topic', 'image', 'article']
    template_name = 'publication/post_form.html'
    success_url = '/post/list/'


    def get(self, request):
        context = {
            'topics': self.topic.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        model = Post()
        model.author = request.user
        if request.FILES:
            model.image = request.FILES['image']

        form = self.form(request.POST, instance=model)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return redirect('publication:create_post')

class PostUpdateView(UpdateView):
    model = Post
    topic = Topic
    fields = ['title', 'topic', 'image', 'alt', 'article']
    template_name_suffix = '_update_form'
    form = PostCreateForm
    success_url = '/post/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] =  self.topic.objects.all()
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = '_confirm_delete'
    success_url = '/post/list/'

class PostSearchView(View):
    model = Post
    template_name = 'publication/post_search.html'

    def get(self, request):
        search = request.GET.get('search')
        object = self.model.objects.filter(title__icontains=search)
        context = {
            'posts': object
        }

        return render(request, self.template_name, context)

class PostLikeView(View):
    model = Post
    
    def post(self, request, pk):
        post = get_object_or_404(self.model, id=request.POST.get('post_id'))
        if post.dislike.filter(id=request.user.id).exists():
            post.like.add(request.user)
            post.dislike.remove(request.user)
        elif post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        return redirect('publication:home')

class PostDislikeView(View):
    model = Post
    
    def post(self, request, pk):
        post = get_object_or_404(self.model, id=request.POST.get('post_id'))
        if post.like.filter(id=request.user.id).exists():
            post.dislike.add(request.user)
            post.like.remove(request.user)
        elif post.dislike.filter(id=request.user.id).exists():
            post.dislike.remove(request.user)
        else:
            post.dislike.add(request.user)
        return redirect('publication:home')