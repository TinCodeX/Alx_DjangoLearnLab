from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, register, profile, logout_view,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # ALX-required CRUD URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),           # singular "post"
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # "update" instead of "edit"
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
