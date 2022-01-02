from django.forms import ModelForm
from .models import Post

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'image', 'alt', 'article']