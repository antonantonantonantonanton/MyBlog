"""It defines url schemes for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page with a list of posts.
    path('posts/', views.posts, name='posts'),
    # Create a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Edit post.
    path('edit_post/<int:title_id>/', views.edit_post, name='edit_post')
    ]