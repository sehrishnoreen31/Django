from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

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
        # return success message
        messages.success(request, f'Added the blog "{new_blog.title}"')
        return redirect('add_new_blog')
    return render(request, 'add-blog.html')

def update_blog(request, id):
    # access targeted object
    updated_blog = get_object_or_404(Blog, pk=id)
    # get form values
    if request.method == 'POST':
        ttl = request.POST['title']
        img = request.FILES['blog-img']
        para = request.POST['blog-content']

        # upadte object
        updated_blog.title = ttl
        updated_blog.image = img
        updated_blog.paragraph = para
        updated_blog.date = timezone.now()

        # save updates/changes
        updated_blog.save()

        # update success message
        messages.success(request, f'Blog "{updated_blog.title}" Updated')
        # return to blog
        return redirect('update_blog', id=updated_blog.id)
    return render(request, 'update-blog.html', {'updated_blog':updated_blog})

