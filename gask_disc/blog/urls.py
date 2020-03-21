from django.urls import path

from . import views
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('post/new/', PostCreateView.as_view(), name='posts-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete')
]
