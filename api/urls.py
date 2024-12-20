"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [

    # Authentication and Authorisation
    path('auth/register', views.create_blog_post),
    path('auth/login', views.create_blog_post),
    path('auth/logout', views.create_blog_post),
    path('auth/user', views.create_blog_post),

    # Blog Posts
    path('posts', views.get_all_blog_posts),
    path('posts/create/postid', views.create_blog_post),
    path('posts/delete/postid', views.delete_blog_post),
    path('posts/update/postid', views.update_blog_post),
    path('posts/postid', views.get_a_single_blog_post),
    path('posts/search/keyword=', views.filter_blog_post_by_search),

    # Comments
    path('posts/postid/comments/create', views.create_blog_post),
    path('posts/postid/comments/update/commentid', views.create_blog_post),
    path('posts/postid/comments/delete/commentid', views.create_blog_post),
    path('posts/postid/comments/commentid', views.create_blog_post),

    # Ratings and Reviews
    path('posts/postid/ratings/increase', views.create_blog_post),
    path('posts/postid/ratings/decrease', views.create_blog_post),
    path('posts/postid/ratings', views.create_blog_post),

    # Tags
    path('tags/create', views.create_blog_post),
    path('tags/delete', views.create_blog_post),
    path('tags', views.create_blog_post),

    # User Profile
    path('users/userid/create', views.create_blog_post),
    path('users/userid/delete', views.create_blog_post),
    path('users/userid/update', views.create_blog_post),
    path('users/userid', views.create_blog_post),
]
