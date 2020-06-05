from django.views.generic.list import ListView
from posts.models import Post
# Create your views here.

class PostList(ListView):
    model = Post
