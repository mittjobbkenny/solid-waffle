from django.views import generic
from django.urls import reverse_lazy
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

class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm


class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('home')
