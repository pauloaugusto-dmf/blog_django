from django.forms import ModelForm
from .models import Post, Comment

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'image', 'alt', 'article']

class PostCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']