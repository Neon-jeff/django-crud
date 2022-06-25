from pyexpat import model
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView



from I4G002209LU4.blog.models import Post

class PostListView(ListView):
    model=Post
class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostUpdateView(DetailView):
    model = Post
class PostDeleteView()