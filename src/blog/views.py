from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Post, Category, Tag


class PostListView(ListView):
    """View for listing blog posts"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Get only published posts"""
        return Post.published_objects.published()
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:10]
        context['recent_posts'] = Post.published_objects.recent_posts()
        return context
    
class PostDetailView(DetailView):
    """View for displaying a single post"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        """Get only published posts"""
        return Post.published_objects.published()
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:10]
        context['recent_posts'] = Post.published_objects.recent_posts()
        return context
    
class CategoryPostListView(ListView):
    """View for listing posts in a specific category"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Get published posts for a specific category"""
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.published_objects.by_category(self.category.slug)
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:10]
        context['recent_posts'] = Post.published_objects.recent_posts()
        return context
    
class TagPostListView(ListView):
    """View for listing posts with a specific tag"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Get published posts with a specific tag"""
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.published_objects.by_tag(self.tag.slug)
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:10]
        context['recent_posts'] = Post.published_objects.recent_posts()
        return context