from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def blog(request):
    blogs = Blog.objects.all().order_by('-date', '-id')
    return render(request, 'blog.html', {'blogs': blogs})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blog})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def add_new_blog(request):
    if request.method == 'POST':
        ttl = request.POST['title']
        img = request.FILES['blog-img']
        content = request.POST['blog-content']

        new_blog = Blog(title=ttl, image=img, paragraph=content)
        new_blog.save()
        messages.success(request, f'Added the blog "{new_blog.title}"')
        return redirect('add_blog')
    return render(request, 'add-blog.html')