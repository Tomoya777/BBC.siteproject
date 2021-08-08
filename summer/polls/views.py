from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blog.html', {'blogs': blogs})