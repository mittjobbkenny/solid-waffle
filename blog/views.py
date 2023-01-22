from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
import json
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
from django.db.models import Q
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
        messages.success(self.request, 'Post added')
        return super().form_valid(form)

class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, 'Post updated')
        return super().form_valid(form)


class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, 'Post deleted')
        return super(PostDelete, self).delete(request, *args, **kwargs)


class SearchResults(generic.ListView):
    model = Post
    template_name = 'blog/search_results.html'
    allow_empty = False

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            if not object_list:
                messages.info(self.request, 'No matches found for this search')
                object_list = Post.objects.none
            return object_list

    def dispatch(self, *args, **kwargs):
        try:
            return super().dispatch(*args, **kwargs)
        except Http404:
            messages.info(self.request, "You didn't enter any search criteria")
            return redirect('home')


class SearchAuto(generic.ListView):
    model = Post
  
    def get(self, request):
        if request.is_ajax():
            q = request.GET.get('term', '')
            posts = Post.objects.filter(title__contains=q)
            results=[]
            for post in posts:
                post_json = {}
                post_json['label'] = post.title
                results.append(post_json)
            data = json.dumps(results)
        else:
            return redirect('home')
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
