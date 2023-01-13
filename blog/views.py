from django.views import generic
from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/post.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostAdd(generic.CreateView):
    model = Post
    template_name = 'blog/post_add.html'
    form_class = PostForm
