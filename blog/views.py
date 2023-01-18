from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
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

    def form_valid(self, form):
        messages.info(self.request, 'Post added')
        return super().form_valid(form)

class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm

    def form_valid(self, form):
        messages.info(self.request, 'Post updated')
        return super().form_valid(form)


class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, 'Post deleted')
        return super(PostDelete, self).delete(request, *args, **kwargs)
