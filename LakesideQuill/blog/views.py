from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blog})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')