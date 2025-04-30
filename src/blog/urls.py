from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page (post list)
    path('', views.PostListView.as_view(), name='post_list'),
    
    # Post detail page
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Category detail page
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_detail'),
    
    # Tag detail page
    path('tag/<slug:slug>/', views.TagPostListView.as_view(), name='tag_detail'),
]