from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogPost

def home(request):
    title = "this is my title"
    context = {'title': title}
    return render(request,'posts/home.html',context)


def blogposts(request):
    context = {}
    return render(request,'posts/blogposts.html',context)


def create(request):
    form = BlogForm()

    if request.method == "POST": 
        form = BlogForm(request.POST)
        if form.is_valid(): 
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            blog = BlogPost(
                title=title, 
                content = content
            )

            blog.save()

            return redirect('blogposts')

    context = {'form':form}
    return render(request,'posts/create.html',context)