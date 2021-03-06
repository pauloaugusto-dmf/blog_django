import json

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.views.generic.list import ListView


from .models import Topic, Post, Comment
from .form import PostCreateForm, PostCommentForm


class AdminStaffRequireMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class PublicationHomeView(View):
    template_name = "publication/home.html"
    paginate_by = 5
    topic = Topic
    post = Post

    def get(self, request):
        context = {
            "topics": self.topic.objects.all(),
            "posts": self.post.objects.all(),
        }

        return render(request, self.template_name, context)


# Topic Views


class TopicListView(AdminStaffRequireMixin, ListView):
    model = Topic
    paginate_by = 15


class TopicCreateView(AdminStaffRequireMixin, CreateView):
    model = Topic
    fields = ["name"]
    success_url = "/topic/list/"


class TopicUpdateView(AdminStaffRequireMixin, UpdateView):
    model = Topic
    fields = ["name"]
    template_name_suffix = "_update_form"
    success_url = "/topic/list/"


class TopicDeleteView(AdminStaffRequireMixin, DeleteView):
    model = Topic
    template_name_suffix = "_confirm_delete"
    success_url = "/topic/list/"


# Post Views


class PostListView(AdminStaffRequireMixin, ListView):
    model = Post
    paginate_by = 15


class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = PostCommentForm()
        return context


class PostCreateView(AdminStaffRequireMixin, CreateView):
    model = Post
    topic = Topic
    form = PostCreateForm
    fields = ["title", "topic", "image", "article"]
    template_name = "publication/post_form.html"
    success_url = "/post/list/"

    def get(self, request):
        context = {
            "topics": self.topic.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        model = Post()
        model.author = request.user
        if request.FILES:
            model.image = request.FILES["image"]

        form = self.form(request.POST, instance=model)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return redirect("publication:create_post")


class PostUpdateView(AdminStaffRequireMixin, UpdateView):
    model = Post
    topic = Topic
    fields = ["title", "topic", "image", "alt", "article"]
    template_name_suffix = "_update_form"
    form = PostCreateForm
    success_url = "/post/list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = self.topic.objects.all()
        return context


class PostDeleteView(AdminStaffRequireMixin, DeleteView):
    model = Post
    template_name_suffix = "_confirm_delete"
    success_url = "/post/list/"


class PostSearchView(View):
    model = Post
    template_name = "publication/post_search.html"

    def get(self, request):
        search = request.GET.get("search")
        object = self.model.objects.filter(title__icontains=search)
        context = {"posts": object}

        return render(request, self.template_name, context)


class PostLikeView(LoginRequiredMixin, View):
    model = Post

    def post(self, request, pk):
        # TODO refactor
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            post = get_object_or_404(self.model, id=pk)
            data_from_post = json.load(request)["data"]
            if data_from_post == 1:
                if post.dislike.filter(id=request.user.id).exists():
                    post.like.add(request.user)
                    post.dislike.remove(request.user)
                elif post.like.filter(id=request.user.id).exists():
                    post.like.remove(request.user)
                else:
                    post.like.add(request.user)

                return self.return_json_data(post)

            else:
                if post.like.filter(id=request.user.id).exists():
                    post.dislike.add(request.user)
                    post.like.remove(request.user)
                elif post.dislike.filter(id=request.user.id).exists():
                    post.dislike.remove(request.user)
                else:
                    post.dislike.add(request.user)

                return self.return_json_data(post)

    def return_json_data(self, post):
        data = json.dumps(
            {
                "like": post.get_sum_likes(),
                "dislike": post.get_sum_dislikes(),
            },
            indent=4,
        )
        return JsonResponse(data, safe=False)


class PostCommentView(LoginRequiredMixin, CreateView):
    fields = "__all__"
    form = PostCommentForm

    def post(self, request, pk):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            models = Comment()

            data_from_post = json.load(request)["data"]

            models.post = Post.objects.get(id=pk)
            models.user = request.user
            models.text = data_from_post
            models.save()

            data = json.dumps(
                {
                    "comment": models.text,
                    "user": request.user.username,
                    "comment_time": models.get_time(),
                },
                indent=4,
            )

            return JsonResponse(data, safe=False)
