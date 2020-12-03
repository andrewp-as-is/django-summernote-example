from django.views.generic.list import ListView

from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = "post_list" # default is "object_list"
