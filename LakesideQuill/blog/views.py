from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.messages import get_messages
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
    list(get_messages(request))
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
    list(get_messages(request))
    # access targeted object
    selected_blog = get_object_or_404(Blog, pk=id)
    # get form values
    if request.method == 'POST':
        ttl = request.POST['title']
        img = request.FILES['blog-img']
        para = request.POST['blog-content']

        # upadte object
        selected_blog.title = ttl
        selected_blog.image = img
        selected_blog.paragraph = para
        selected_blog.date = timezone.now()

        # save updates/changes
        selected_blog.save()

        # update success message
        messages.success(request, f'Blog "{selected_blog.title}" Updated')
        # return to blog
        return redirect('update_blog', id=selected_blog.id)
    return render(request, 'update-blog.html', {'selected_blog':selected_blog})

def delete_blog(request, id):
    list(get_messages(request))
    selected_blog = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        selected_blog.delete()
        # not calling save after delete, it may prevent deletion
        return redirect('blog')
    return render(request, 'delete-blog.html', {'selected_blog': selected_blog})
