from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from .models import Post,Comment
from .forms import PostForm,CommentForm,EditForm
from account.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)


class PostView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status='published').order_by('-date')
        context = {'post':post,}
        return render(request, "post/post_list.html", context)

def Draft(LoginRequiredMixin,request):
    post = Post.objects.filter(status='draft')
    context = {'post': post,}
    return render(request, 'post/post_list.html', context)

def Hidden(LoginRequiredMixin,request):

    post = Post.objects.filter(status='hidden')
    context = {'post': post,}
    return render(request, 'Post_list.html', context)
    
def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
    context = {'form': form,}
    return render(request, 'post.html', context)

class PostDetailView(LoginRequiredMixin,View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title, status='published')
        count_hit = True
        comment = post.comment_set.all()
        context = {'post':post,'comment': comment,}
        return render(request, "post/post_detail.html", context)

def comment(request,pk):
    post= get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post
            comment.author = request.user
            comment.save()
            return redirect('/posts')
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'comment.html', context)

    def get_object(self):
        title = self.kwargs.get("title")
        if title is None:
            raise Http404
        return get_object_or_404(Post, title__iexact=title)


class CreatePostView(View):
    def get(self, request):
        create = Post.objects.all()
        context = {'create' : create,'form' : PostForm,}
        return render(request, "post.html", context)

    def get(self, request):
        form = PostForm(request.POST)
        post = Post.objects.all()
        if form.is_valid():
            form.save()
            return redirect('index')            
        context = {'form' : form,'post' : post,}        
        return render(request, "post.html", context)


class UserDetail(View):
    def get(self, request,  pk, *args, **kwargs): 
        users = User.objects.get(pk=pk)
        post = Post.objects.filter(user=pk)
        context = {'users':users,}
        return render(request, "user_detail.html", context)

def post_edit(request,title):
    post = get_object_or_404(Post,title=title,user=request.user)
    if request.method == "POST":
        form = EditForm(request.POST, instance=post)
        if posts.user == request.user: 
            if form.is_valid():           
                post = form.save(commit=False)
                post.author = request.user
                post.save()
            return redirect('/posts', pk=post.pk)
    else:
        form = EditForm(instance=post)
    return render(request, 'edit.html', {'form': form})