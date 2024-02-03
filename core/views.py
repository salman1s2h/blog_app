from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .models import Post, Comment,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .forms import CommentForm,CreatePost
from django.http import HttpResponseRedirect


def LikeView(request,pk):
    print("request.POST------------------------>",request.POST)
    print("equest.POST.get('post_id')----------------->",request.POST.get('post_id'))
    post_obj = get_object_or_404(Post,id=request.POST.get('post_id'))
    post_obj.likes.add(request.user)
    print("post_obj.slug------------------->",post_obj.slug)
    return HttpResponseRedirect(reverse_lazy('core:post',args=[str(post_obj.id),post_obj.slug]))
    # return HttpResponseRedirect(reverse_lazy('core:post'),kwargs={'pk': pk, 'slug': post_obj.slug})

class HomeView(ListView):
    template_name = 'core/home.html'
    queryset = Post.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post

        print("context-------------------->",context)#testing
        return context

class PostView(DetailView):
    model = Post
    template_name = 'core/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        like_count = post.total_likes()
        context['like_count'] = like_count
        return context

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        print("post------------------------->",post)
        comments = post.comment_set.all()
        print("comments------------------->",comments)
        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print("user--request------->",request.user)

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post,author=request.user
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePost
    # fields = ["title", "content","tags","cat_id"]#"category_id"
    # fields = ["title", "content","tags","category_id"]#"category_id"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['category_id'] = Category.objects.all()
        # context['form'] = CreatePost()
        print("context-------of create post-------------->",context)
        return context
    
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("core:home")

    # ## TEST
 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        # print("form clean data ----------->",form.cleaned_data['category_id'])
        # obj.category_id = form.cleaned_data['cat_id']
        # print("form clean data ----------->",form.cleaned_data['category_id'])
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form_invalid--------->',form) 
        return super().form_invalid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "tags","category_id"]# "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("core:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("core:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)