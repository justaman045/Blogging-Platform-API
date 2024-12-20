from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def create_blog_post(request):
    return HttpResponse("Create Blog Post")

def update_blog_post(request):
    return HttpResponse("Update Blog Post")

def delete_blog_post(request):
    return HttpResponse("Delete Blog Post")

def get_a_single_blog_post(request):
    return HttpResponse("Get a Single Blog Post")

def get_all_blog_posts(request):
    return HttpResponse("Get All Blog Posts")

def filter_blog_post_by_search(request):
    return HttpResponse("Filter Blog Post by Search")