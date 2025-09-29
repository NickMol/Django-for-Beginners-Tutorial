from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = BlogPost.objects.all().order_by('-created_on')
    blogscount = blogs.count()

    context = {
        'blogs':blogs,
        'blogscount':blogscount
    }
    return render(request,'posts/home.html',context)


@login_required
def blogposts(request):
    blogs = BlogPost.objects.filter(created_by=request.user).order_by('-created_on')
    blogscount = blogs.count()

    context = {
        'blogs':blogs,
        'blogscount':blogscount
    }
    return render(request,'posts/blogposts.html',context)

@login_required
def create(request):
    form = BlogForm()

    if request.method == "POST": 
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid(): 
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']

            blog = BlogPost(
                title=title, 
                content = content, 
                image = image,
                category = category
            )

            blog.save()
            blog.tags.set(tags)

            return redirect('blogposts')

    context = {'form':form}
    return render(request,'posts/create.html',context)

@login_required
def edit(request,pk):
    blog = BlogPost.objects.get(id=pk)

    if request.user != blog.created_by: 
        return redirect('home')

    form = BlogForm(instance=blog)

    if request.method == "POST": 
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'posts/edit.html',context )


@login_required
def delete(request,pk): 
    blog = BlogPost.objects.get(id=pk)

    if request.user != blog.created_by: 
        return redirect('home')

    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    context = {'blog':blog}
    return render(request,'posts/delete.html',context )


def details(request,pk): 
    blog = BlogPost.objects.get(id=pk)
    context = {'blog':blog}
    return render(request,'posts/details.html',context )